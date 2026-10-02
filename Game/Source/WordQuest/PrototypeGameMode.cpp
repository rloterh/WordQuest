#include "PrototypeGameMode.h"
#include "ContextScreen.h"
#include "Engine/GameViewportClient.h"
#include "Engine/World.h"
#include "Misc/CommandLine.h"
#include "Misc/Parse.h"
#include "Misc/Paths.h"
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
    auto KeyStep = [this, &Step](const FKey& Key)
    {
        // Route real Slate key-down/up events to the focused widget. These
        // checks must not call Choose/Hint/Submit/TogglePause directly.
        const FKeyEvent Event(Key, FModifierKeysState(), uint32(0), false, 0, 0);
        const bool Down = FSlateApplication::Get().ProcessKeyDownEvent(Event);
        const bool Up = FSlateApplication::Get().ProcessKeyUpEvent(Event);
        const auto& A = Screen->GetAttempt();
        UE_LOG(LogTemp, Display, TEXT("WQ_KEY_STEP proof=%s step=%d key=%s down=%d up=%d selected=%d submitted=%d correct=%d hint=%d paused=%d evaluations=%d"),
            *ProofName, ++Step, *Key.GetFName().ToString(), Down, Up,
            A.SelectedIndex, A.bSubmitted, A.bCorrect, A.bHintUsed, A.bPaused, A.EvaluationCount);
    };
    if (ProofName == TEXT("keyswitch"))
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

void APrototypeController::RunProof()
{
    if (ProofName.StartsWith(TEXT("key"))) RunKeyboardProof();
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
    else if (ProofName == TEXT("long") || ProofName == TEXT("longfocus"))
    {
        Screen->SetProofTextScale(2);
        Screen->SetProofLongText();
        if (ProofName == TEXT("longfocus"))
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
    IFileManager::Get().MakeDirectory(*FPaths::GetPath(CapturePath), true);
    FScreenshotRequest::RequestScreenshot(CapturePath, true, false);
    if (FParse::Param(FCommandLine::Get(), TEXT("WQExit")))
        GetWorldTimerManager().SetTimer(ProofTimer, []() { FGenericPlatformMisc::RequestExit(false); }, 2.f, false);
}
#endif
