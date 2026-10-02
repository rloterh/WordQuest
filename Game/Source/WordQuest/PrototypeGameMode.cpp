#include "PrototypeGameMode.h"
#include "ContextScreen.h"
#include "Engine/GameViewportClient.h"
#include "Engine/World.h"
#include "Misc/CommandLine.h"
#include "Misc/Parse.h"
#include "Misc/Paths.h"
#include "Misc/CoreDelegates.h"
#include "HAL/FileManager.h"
#include "UnrealClient.h"
#include "TimerManager.h"
#if !UE_BUILD_SHIPPING
#include "Framework/Application/SlateApplication.h"
#include "Input/Events.h"
#include "InputCoreTypes.h"
#endif

APrototypeGameMode::APrototypeGameMode()
{
    PlayerControllerClass = APrototypeController::StaticClass();
    DefaultPawnClass = nullptr;
    HUDClass = nullptr;
}

void APrototypeController::BeginPlay()
{
    Super::BeginPlay();
    if (!IsLocalController()) return;
    Screen = CreateWidget<UContextScreen>(this, UContextScreen::StaticClass());
    Screen->AddToViewport();
    SetShowMouseCursor(true);
    FInputModeUIOnly Input;
    Input.SetWidgetToFocus(Screen->TakeWidget());
    Input.SetLockMouseToViewportBehavior(EMouseLockMode::DoNotLock);
    SetInputMode(Input);
#if !UE_BUILD_SHIPPING
    FParse::Value(FCommandLine::Get(), TEXT("WQProof="), ProofName);
    FParse::Value(FCommandLine::Get(), TEXT("WQCapture="), CapturePath);
    if (!ProofName.IsEmpty() || !CapturePath.IsEmpty())
        GetWorldTimerManager().SetTimer(ProofTimer, this, &APrototypeController::RunProof, 1.f, false);
#endif
}

#if !UE_BUILD_SHIPPING
void APrototypeController::RunKeyboardProof()
{
    int32 Step = 0;
    auto KeyStep = [this, &Step](const FKey& Key, bool Shift = false)
    {
        // Route real Slate key-down/up events to the focused widget. These
        // checks must not call Choose/Hint/Submit/TogglePause directly.
        const FModifierKeysState Modifiers(Shift, false, false, false, false, false, false, false, false);
        const FKeyEvent Event(Key, Modifiers, uint32(0), false, 0, 0);
        const bool Down = FSlateApplication::Get().ProcessKeyDownEvent(Event);
        const bool Up = FSlateApplication::Get().ProcessKeyUpEvent(Event);
        const auto& A = Screen->GetAttempt();
        UE_LOG(LogTemp, Display, TEXT("WQ_KEY_STEP proof=%s step=%d key=%s down=%d up=%d selected=%d submitted=%d correct=%d hint=%d paused=%d evaluations=%d shift=%d focus=%s textpercent=%d"),
            *ProofName, ++Step, *Key.GetFName().ToString(), Down, Up,
            A.SelectedIndex, A.bSubmitted, A.bCorrect, A.bHintUsed, A.bPaused, A.EvaluationCount,
            Shift, *Screen->GetProofFocusName(), Screen->GetProofTextPercent());
    };
    if (ProofName == TEXT("keyback"))
    {
        KeyStep(EKeys::Tab, true); KeyStep(EKeys::Tab);
        KeyStep(EKeys::Tab, true); KeyStep(EKeys::Tab, true);
    }
    else if (ProofName == TEXT("keyskip"))
    {
        KeyStep(EKeys::H);
        for (int32 I = 0; I < 6; ++I) KeyStep(EKeys::Tab);
        KeyStep(EKeys::Tab, true); KeyStep(EKeys::Tab, true);
    }
    else if (ProofName == TEXT("keytab"))
    {
        for (int32 I = 0; I < 8; ++I) KeyStep(EKeys::Tab);
        for (int32 I = 0; I < 3; ++I) KeyStep(EKeys::Tab, true);
    }
    else if (ProofName == TEXT("keymodal"))
    {
        KeyStep(EKeys::P); KeyStep(EKeys::Tab); KeyStep(EKeys::SpaceBar);
        KeyStep(EKeys::Tab); KeyStep(EKeys::Tab);
        KeyStep(EKeys::Tab, true); KeyStep(EKeys::Tab, true); KeyStep(EKeys::Tab, true);
        KeyStep(EKeys::Tab); // Leave the enlarged modal on TextSize.
    }
    else if (ProofName == TEXT("keyretry"))
    {
        KeyStep(EKeys::H); KeyStep(EKeys::One); KeyStep(EKeys::Enter); KeyStep(EKeys::P);
        KeyStep(EKeys::Tab); KeyStep(EKeys::SpaceBar); // Real text-size toggle.
        KeyStep(EKeys::Tab); KeyStep(EKeys::SpaceBar); // Real retry button.
        KeyStep(EKeys::Tab); KeyStep(EKeys::SpaceBar); // First answer after reset.
    }
    else if (ProofName == TEXT("keydisabled"))
    {
        KeyStep(EKeys::One); KeyStep(EKeys::Enter);
        KeyStep(EKeys::Tab); KeyStep(EKeys::Tab); KeyStep(EKeys::Tab, true);
        KeyStep(EKeys::P); KeyStep(EKeys::SpaceBar);
    }
    else if (ProofName == TEXT("keyswitch"))
    {
        KeyStep(EKeys::One); KeyStep(EKeys::Three); KeyStep(EKeys::Four); KeyStep(EKeys::Two);
    }
    else if (ProofName == TEXT("keyempty")) KeyStep(EKeys::Enter);
    else if (ProofName == TEXT("keysubmit"))
    {
        KeyStep(EKeys::One); KeyStep(EKeys::Enter); KeyStep(EKeys::Enter);
    }
    else if (ProofName == TEXT("keyhint"))
    {
        KeyStep(EKeys::H); KeyStep(EKeys::One); KeyStep(EKeys::Enter);
    }
    else if (ProofName == TEXT("keybuttons"))
    {
        // Focus setup is explicit; Space must activate the real UButton route.
        // This is not a Tab-navigation or manual-keyboard qualification.
        Screen->FocusProofAnswer(); KeyStep(EKeys::SpaceBar);
        Screen->FocusProofAction(); KeyStep(EKeys::SpaceBar);
        KeyStep(EKeys::Enter);
    }
    else if (ProofName == TEXT("keypaused") || ProofName == TEXT("keyresumed"))
    {
        KeyStep(EKeys::Two); KeyStep(EKeys::P);
        KeyStep(EKeys::One); KeyStep(EKeys::H);
        if (ProofName == TEXT("keyresumed")) KeyStep(EKeys::SpaceBar);
    }
}

void APrototypeController::RunInterruptionProof()
{
    int32 Step = 0;
    auto Trace = [this, &Step](const TCHAR* Event)
    {
        const auto& A = Screen->GetAttempt();
        UE_LOG(LogTemp, Display, TEXT("WQ_INTERRUPT_STEP proof=%s step=%d event=%s selected=%d submitted=%d correct=%d hint=%d paused=%d evaluations=%d focus=%s"),
            *ProofName, ++Step, Event, A.SelectedIndex, A.bSubmitted, A.bCorrect,
            A.bHintUsed, A.bPaused, A.EvaluationCount, *Screen->GetProofFocusName());
    };
    auto Key = [](const FKey& Value)
    {
        const FKeyEvent Event(Value, FModifierKeysState(), uint32(0), false, 0, 0);
        FSlateApplication::Get().ProcessKeyDownEvent(Event);
        FSlateApplication::Get().ProcessKeyUpEvent(Event);
    };
    Key(EKeys::H); Key(EKeys::Two);
    if (ProofName == TEXT("interruptsubmitted"))
    {
        Key(EKeys::Enter);
        Screen->FocusProofPause();
    }
    else Screen->FocusProofAnswer();
    if (ProofName == TEXT("interruptmanual")) Key(EKeys::P);
    // Drive the engine notification routes, not the screen's pause handler.
    // This is synthetic lifecycle evidence, not OS/phone interruption testing.
    FSlateApplication::Get().OnApplicationActivationChanged(true);
    Trace(TEXT("start"));
    auto Inactive = [&Trace]() { FSlateApplication::Get().OnApplicationActivationChanged(false); Trace(TEXT("slateinactive")); };
    auto Deactivate = [&Trace]() { FCoreDelegates::ApplicationWillDeactivateDelegate.Broadcast(); Trace(TEXT("deactivate")); };
    auto Background = [&Trace]() { FCoreDelegates::ApplicationWillEnterBackgroundDelegate.Broadcast(); Trace(TEXT("background")); };
    // Each notification must independently pause an active attempt in one mode.
    if (ProofName == TEXT("interruptresumed")) { Deactivate(); Background(); Inactive(); }
    else if (ProofName == TEXT("interruptsubmitted")) { Background(); Inactive(); Deactivate(); }
    else { Inactive(); Deactivate(); Background(); }
    FSlateApplication::Get().OnApplicationActivationChanged(true); Trace(TEXT("slateactive"));
    FCoreDelegates::ApplicationHasEnteredForegroundDelegate.Broadcast(); Trace(TEXT("foreground"));
    FCoreDelegates::ApplicationHasReactivatedDelegate.Broadcast(); Trace(TEXT("reactivate"));
    // Enter/Space on focused Resume are deliberate modal actions. Only the
    // gameplay selection and Hint shortcuts must remain blocked here.
    Key(EKeys::One); Key(EKeys::H); Trace(TEXT("blockedinput"));
    if (ProofName == TEXT("interruptresumed") || ProofName == TEXT("interruptsubmitted"))
    {
        Key(EKeys::SpaceBar); Trace(TEXT("resume"));
    }
}

void APrototypeController::RunProof()
{
    if (ProofName.StartsWith(TEXT("key"))) RunKeyboardProof();
    else if (ProofName.StartsWith(TEXT("interrupt"))) RunInterruptionProof();
    else if (ProofName == TEXT("selected")) Screen->Choose(2);
    else if (ProofName == TEXT("correct")) { Screen->Choose(0); Screen->Submit(); Screen->Submit(); }
    else if (ProofName == TEXT("wrong")) { Screen->Choose(1); Screen->Submit(); }
    else if (ProofName == TEXT("hint")) { Screen->Hint(); Screen->Choose(0); Screen->Submit(); }
    else if (ProofName == TEXT("empty")) Screen->Submit();
    else if (ProofName == TEXT("paused")) { Screen->Choose(1); Screen->TogglePause(); Screen->Choose(0); Screen->Submit(); }
    else if (ProofName == TEXT("resumed"))
    {
        Screen->Choose(1); Screen->TogglePause(); Screen->Choose(0); Screen->Submit(); Screen->TogglePause();
    }
    else if (ProofName == TEXT("pausefocus")) Screen->FocusProofPause();
    else if (ProofName == TEXT("large")) Screen->SetProofTextScale(2);
    else if (ProofName == TEXT("actions") || ProofName == TEXT("actionfocus"))
    {
        if (ProofName == TEXT("actions")) Screen->SetProofTextScale(2);
        FTimerHandle FocusTimer;
        GetWorldTimerManager().SetTimer(FocusTimer, FTimerDelegate::CreateWeakLambda(this,
            [this]() { Screen->FocusProofAction(); }), .5f, false);
    }
    else if (ProofName == TEXT("long") || ProofName == TEXT("longfocus") || ProofName == TEXT("longselectedfocus"))
    {
        Screen->SetProofTextScale(2);
        Screen->SetProofLongText();
        if (ProofName == TEXT("longselectedfocus")) Screen->Choose(1);
        if (ProofName != TEXT("long"))
        {
            // Focus after enlarged content has laid out, before the native capture.
            FTimerHandle FocusTimer;
            GetWorldTimerManager().SetTimer(FocusTimer, FTimerDelegate::CreateWeakLambda(this,
                [this]() { Screen->FocusProofAnswer(); }), .5f, false);
        }
    }
    else if (ProofName == TEXT("focus")) Screen->FocusProofAnswer();
    const auto& A = Screen->GetAttempt();
    UE_LOG(LogTemp, Display, TEXT("WQ_STATE proof=%s selected=%d submitted=%d correct=%d hint=%d paused=%d evaluations=%d"),
        *ProofName, A.SelectedIndex, A.bSubmitted, A.bCorrect, A.bHintUsed, A.bPaused, A.EvaluationCount);
    if (!CapturePath.IsEmpty()) GetWorldTimerManager().SetTimer(ProofTimer, this, &APrototypeController::CaptureProof, 1.f, false);
}

void APrototypeController::CaptureProof()
{
    UE_LOG(LogTemp, Display, TEXT("WQ_FEEDBACK_CAPTURE proof=%s visibility=%d"),
        *ProofName, Screen->GetProofFeedbackVisibility());
    for (int32 I = 0; I < 4; ++I)
        UE_LOG(LogTemp, Display, TEXT("WQ_OPTION_CUE proof=%s option=%d codepoint=%d label=%s"),
            *ProofName, I, Screen->GetProofAnswerCueCode(I), *Screen->GetProofAnswerAccessibleText(I));
    if (ProofName == TEXT("longfocus") || ProofName == TEXT("longselectedfocus"))
        UE_LOG(LogTemp, Display, TEXT("WQ_ANSWER_START proof=%s focus=%s textpercent=%d visible=%d oversized=%d"),
            *ProofName, *Screen->GetProofFocusName(), Screen->GetProofTextPercent(),
            Screen->GetProofFocusedAnswerStartVisible(), Screen->GetProofFocusedAnswerOversized());
    if (ProofName.StartsWith(TEXT("key")))
        UE_LOG(LogTemp, Display, TEXT("WQ_FOCUS_CAPTURE proof=%s focus=%s visible=%d textpercent=%d"),
            *ProofName, *Screen->GetProofFocusName(), Screen->GetProofFocusedControlVisible(), Screen->GetProofTextPercent());
    if (ProofName.StartsWith(TEXT("interrupt")))
        UE_LOG(LogTemp, Display, TEXT("WQ_INTERRUPT_CAPTURE proof=%s focus=%s visible=%d"),
            *ProofName, *Screen->GetProofFocusName(), Screen->GetProofFocusedControlVisible());
    IFileManager::Get().MakeDirectory(*FPaths::GetPath(CapturePath), true);
    FScreenshotRequest::RequestScreenshot(CapturePath, true, false);
    if (FParse::Param(FCommandLine::Get(), TEXT("WQExit")))
        GetWorldTimerManager().SetTimer(ProofTimer, []() { FGenericPlatformMisc::RequestExit(false); }, 2.f, false);
}
#endif
