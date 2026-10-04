#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "GameFramework/PlayerController.h"
#include "PrototypeGameMode.generated.h"

class UContextScreen;
class FSlateVirtualUserHandle;

UCLASS()
class WORDQUEST_API APrototypeController : public APlayerController
{
    GENERATED_BODY()
protected:
    virtual void BeginPlay() override;
#if !UE_BUILD_SHIPPING
    virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;
#endif
private:
    UPROPERTY(Transient) TObjectPtr<UContextScreen> Screen;
#if !UE_BUILD_SHIPPING
    void RunProof();
    void RunKeyboardProof();
    void RunPointerProof();
    void TracePointerProof();
    void RunInterruptionProof();
    void RunScrollProof();
    void TraceScrollProof();
    void RunModalProof();
    void TraceModalProof();
    void CaptureProof();
    FTimerHandle ProofTimer;
    FTimerHandle ScrollTimer;
    FTimerHandle ModalTimer;
    FTimerHandle PointerTimer;
    TSharedPtr<FSlateVirtualUserHandle> PointerUser;
    TArray<TPair<FName, FName>> PointerSteps;
    TSet<FKey> PointerButtons;
    FVector2D LastPointerPosition = FVector2D::ZeroVector;
    int32 PointerStep = 0;
    bool bPointerTargetPrepared = false;
    int32 ScrollStep = 0;
    bool ScrollDown = false, ScrollUp = false;
    FString ProofName, CapturePath;
#endif
};

UCLASS()
class WORDQUEST_API APrototypeGameMode : public AGameModeBase
{
    GENERATED_BODY()
public:
    APrototypeGameMode();
};
