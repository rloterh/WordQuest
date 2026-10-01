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
void APrototypeController::RunProof()
{
    if (ProofName == TEXT("selected")) Screen->Choose(2);
    else if (ProofName == TEXT("correct")) { Screen->Choose(0); Screen->Submit(); Screen->Submit(); }
    else if (ProofName == TEXT("wrong")) { Screen->Choose(1); Screen->Submit(); }
    else if (ProofName == TEXT("hint")) { Screen->Hint(); Screen->Choose(0); Screen->Submit(); }
    else if (ProofName == TEXT("empty")) Screen->Submit();
    else if (ProofName == TEXT("paused")) { Screen->Choose(1); Screen->TogglePause(); Screen->Choose(0); Screen->Submit(); }
    else if (ProofName == TEXT("large")) Screen->SetProofTextScale(2);
    else if (ProofName == TEXT("long")) { Screen->SetProofTextScale(2); Screen->SetProofLongText(); }
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
