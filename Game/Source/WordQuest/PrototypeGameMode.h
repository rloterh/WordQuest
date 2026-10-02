#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "GameFramework/PlayerController.h"
#include "PrototypeGameMode.generated.h"

class UContextScreen;

UCLASS()
class WORDQUEST_API APrototypeController : public APlayerController
{
    GENERATED_BODY()
protected:
    virtual void BeginPlay() override;
private:
    UPROPERTY(Transient) TObjectPtr<UContextScreen> Screen;
#if !UE_BUILD_SHIPPING
    void RunProof();
    void RunKeyboardProof();
    void RunInterruptionProof();
    void RunScrollProof();
    void TraceScrollProof();
    void RunModalProof();
    void TraceModalProof();
    void CaptureProof();
    FTimerHandle ProofTimer;
    FTimerHandle ScrollTimer;
    FTimerHandle ModalTimer;
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
