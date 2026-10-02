#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "ContextChallenge.h"
#include "ContextScreen.generated.h"

class UButton;
class UBorder;
class UCanvasPanel;
class UImage;
class UScrollBox;
class USizeBox;
class UTextBlock;

USTRUCT()
struct FContextAnswerWidgets
{
    GENERATED_BODY()
    UPROPERTY(Transient) TObjectPtr<UButton> Button;
    UPROPERTY(Transient) TObjectPtr<UImage> Skin;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Label;
    UPROPERTY(Transient) TObjectPtr<UBorder> Badge;
    UPROPERTY(Transient) TObjectPtr<UImage> BadgeSkin;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Letter;
    UPROPERTY(Transient) TObjectPtr<USizeBox> BadgeSize;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Marker;
    UPROPERTY(Transient) TObjectPtr<USizeBox> MarkerSize;
};

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
    void FocusProofAction();
    void FocusProofPause();
    FString GetProofFocusName() const;
    int32 GetProofTextPercent() const { return FMath::RoundToInt(TextScale * 100); }
    bool GetProofFocusedControlVisible() const;
    bool GetProofFocusedAnswerStartVisible() const;
    bool GetProofFocusedAnswerOversized() const;
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
    UImage* VectorPicture(const TCHAR* Name, const TCHAR* File, FVector2D Dimensions);
    void Build();
    void Layout(FVector2D Size);
    void Refresh();
    TArray<UButton*> EnabledGameplayControls() const;
    void StyleButtons();
    void RevealFocusedControl(UButton* Target);
    UTextBlock* ButtonLabel(UButton* Target) const;
    UImage* ButtonSkin(UButton* Target) const;
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
    bool bRevealFocusAfterLayout = false;
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
    UPROPERTY(Transient) TObjectPtr<UImage> ProgressPlaque;
    UPROPERTY(Transient) TObjectPtr<UImage> HintSkin;
    UPROPERTY(Transient) TObjectPtr<UImage> SubmitSkin;
    UPROPERTY(Transient) TObjectPtr<UImage> PauseSkin;
    UPROPERTY(Transient) TObjectPtr<UImage> HintIcon;
    UPROPERTY(Transient) TObjectPtr<UImage> SubmitIcon;
    UPROPERTY(Transient) TObjectPtr<UImage> PauseIcon;
    UPROPERTY(Transient) TObjectPtr<USizeBox> PauseIconSize;
    UPROPERTY(Transient) TObjectPtr<USizeBox> HintIconSize;
    UPROPERTY(Transient) TObjectPtr<USizeBox> SubmitIconSize;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> HintLabel;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> SubmitLabel;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> PauseLabel;
    UPROPERTY(Transient) TObjectPtr<UImage> ModalShade;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Brand;
    UPROPERTY(Transient) TObjectPtr<UImage> BrandMark;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Progress;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Mode;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Word;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Clue;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Prompt;
    UPROPERTY(Transient) TObjectPtr<UImage> Divider;
    UPROPERTY(Transient) TObjectPtr<UImage> HeaderDivider;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> Feedback;
    UPROPERTY(Transient) TObjectPtr<UTextBlock> PauseTitle;
    UPROPERTY(Transient) TObjectPtr<UButton> PauseButton;
    UPROPERTY(Transient) TObjectPtr<UButton> HintButton;
    UPROPERTY(Transient) TObjectPtr<UButton> SubmitButton;
    UPROPERTY(Transient) TObjectPtr<UButton> ResumeButton;
    UPROPERTY(Transient) TObjectPtr<UButton> TextSizeButton;
    UPROPERTY(Transient) TObjectPtr<UButton> ResetButton;
    UPROPERTY(Transient) TArray<FContextAnswerWidgets> Answers;
    UPROPERTY(Transient) TObjectPtr<UWidget> PreviousFocus;
    UPROPERTY(Transient) TObjectPtr<UObject> DisplayFont;
};
