#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "ContextChallenge.h"
#include "ContextScreen.generated.h"

class UButton;
class UCanvasPanel;
class UImage;
class UScrollBox;
class USizeBox;
class UTextBlock;

UCLASS()
class WORDQUEST_API UContextScreen : public UUserWidget
{
    GENERATED_BODY()
public:
    void Choose(int32 Index);
    UFUNCTION() void Submit();
    UFUNCTION() void Hint();
    UFUNCTION() void TogglePause();
    UFUNCTION() void ResetAttempt();
    UFUNCTION() void ToggleTextSize();
    const FContextAttempt& GetAttempt() const { return Attempt; }
#if !UE_BUILD_SHIPPING
    void SetProofTextScale(float Value);
    void SetProofLongText();
    void FocusProofAnswer();
#endif
protected:
    virtual TSharedRef<SWidget> RebuildWidget() override;
    virtual void NativeConstruct() override;
    virtual void NativeTick(const FGeometry& Geometry, float DeltaTime) override;
    virtual FReply NativeOnKeyDown(const FGeometry& Geometry, const FKeyEvent& Event) override;
private:
    template<typename T> T* Make(const TCHAR* Name);
    UTextBlock* Text(const TCHAR* Name, const FString& Value);
    UButton* Button(const TCHAR* Name, const FString& Label);
    UImage* Picture(const TCHAR* Name, const TCHAR* Path);
    void Build();
    void Layout(FVector2D Size);
    void Refresh();
    void StyleButtons();
    void SetButtonLabel(UButton* Target, const FString& Label);
    UFUNCTION() void ChooseA() { Choose(0); }
    UFUNCTION() void ChooseB() { Choose(1); }
    UFUNCTION() void ChooseC() { Choose(2); }
    UFUNCTION() void ChooseD() { Choose(3); }

    FContextQuestion Question;
    FContextAttempt Attempt;
    FString ContentError;
    FVector2D LastSize = FVector2D::ZeroVector;
    float TextScale = 1.f;
    float Scale = 1.f;
    bool bLayoutDirty = true;
    bool bReady = false;
    bool bRevealFeedback = false;
    UPROPERTY(Transient) TObjectPtr<UCanvasPanel> Root;
    UPROPERTY(Transient) TObjectPtr<UCanvasPanel> Canvas;
    UPROPERTY(Transient) TObjectPtr<UCanvasPanel> Modal;
    UPROPERTY(Transient) TObjectPtr<UScrollBox> Scroll;
    UPROPERTY(Transient) TObjectPtr<USizeBox> ContentSize;
    UPROPERTY(Transient) TObjectPtr<UImage> Background;
    UPROPERTY(Transient) TObjectPtr<UImage> Panel;
    UPROPERTY(Transient) TObjectPtr<UImage> PanelBody;
    UPROPERTY(Transient) TObjectPtr<UImage> PanelBottom;
    UPROPERTY(Transient) TObjectPtr<UImage> Spirit;
    UPROPERTY(Transient) TObjectPtr<UImage> ModalShade;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Brand;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Progress;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Mode;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Word;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Clue;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Prompt;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Divider;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> HeaderDivider;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Feedback;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> PauseTitle;
    UPROPERTY(Transient) TObjectPtr<UButton> PauseButton;
    UPROPERTY(Transient) TObjectPtr<UButton> HintButton;
    UPROPERTY(Transient) TObjectPtr<UButton> SubmitButton;
    UPROPERTY(Transient) TObjectPtr<UButton> ResumeButton;
    UPROPERTY(Transient) TObjectPtr<UButton> TextSizeButton;
    UPROPERTY(Transient) TObjectPtr<UButton> ResetButton;
    UPROPERTY(Transient) TArray<TObjectPtr<UButton>> AnswerButtons;
    UPROPERTY(Transient) TObjectPtr<UWidget> PreviousFocus;
    UPROPERTY(Transient) TObjectPtr<UObject> DisplayFont;
};
