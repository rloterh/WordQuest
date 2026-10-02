#include "ContextScreen.h"
#include "Blueprint/WidgetTree.h"
#include "Brushes/SlateRoundedBoxBrush.h"
#include "Brushes/SlateImageBrush.h"
#include "Components/Border.h"
#include "Components/Button.h"
#include "Components/ButtonSlot.h"
#include "Components/CanvasPanel.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/Image.h"
#include "Components/HorizontalBox.h"
#include "Components/HorizontalBoxSlot.h"
#include "Components/SafeZone.h"
#include "Components/ScrollBox.h"
#include "Components/ScrollBoxSlot.h"
#include "Components/SizeBox.h"
#include "Components/TextBlock.h"
#include "Engine/Texture2D.h"
#include "Engine/Font.h"
#include "Engine/FontFace.h"
#include "GameFramework/PlayerController.h"
#include "Input/Reply.h"
#include "InputCoreTypes.h"
#include "Misc/Paths.h"
#include "HAL/FileManager.h"
#include "Styling/CoreStyle.h"

namespace
{
const FLinearColor Ink = FLinearColor::FromSRGBColor(FColor(24, 20, 83));
const FLinearColor Pearl = FLinearColor::FromSRGBColor(FColor(225, 220, 255));
const FLinearColor Violet = FLinearColor::FromSRGBColor(FColor(69, 40, 157));
const FLinearColor Gold = FLinearColor::FromSRGBColor(FColor(218, 181, 121));
const FLinearColor BadgeFill = FLinearColor::FromSRGBColor(FColor(181, 178, 248));
const FLinearColor BadgeEdge = FLinearColor::FromSRGBColor(FColor(158, 153, 230));

void Bounds(UWidget* Widget, float X, float Y, float W, float H)
{
    if (auto* Slot = Cast<UCanvasPanelSlot>(Widget->Slot))
    {
        Slot->SetPosition(FVector2D(X, Y));
        Slot->SetSize(FVector2D(W, H));
    }
}
void Fill(UWidget* Widget)
{
    auto* Slot = CastChecked<UCanvasPanelSlot>(Widget->Slot);
    Slot->SetAnchors(FAnchors(0, 0, 1, 1));
    Slot->SetOffsets(FMargin(0));
}
void Font(UTextBlock* Text, float Pixels, bool Bold = false, UObject* Face = nullptr)
{
    auto Info = FCoreStyle::GetDefaultFontStyle(Bold ? "Bold" : "Regular", FMath::Max(1, FMath::RoundToInt(Pixels * .75f)));
    if (Face) Info.FontObject = Face;
    Text->SetFont(Info);
}
void Accessible(UWidget* Widget, const FString& Label)
{
#if WITH_ACCESSIBILITY
    Widget->TakeWidget()->SetAccessibleBehavior(EAccessibleBehavior::Custom, FText::FromString(Label));
#endif
}
}

template<typename T> T* UContextScreen::Make(const TCHAR* Name)
{
    return WidgetTree->ConstructWidget<T>(T::StaticClass(), FName(Name));
}

UTextBlock* UContextScreen::Text(const TCHAR* Name, const FString& Value)
{
    auto* Label = Make<UTextBlock>(Name);
    Label->SetText(FText::FromString(Value));
    Label->SetColorAndOpacity(Ink);
    Label->SetJustification(ETextJustify::Center);
    Label->SetVisibility(ESlateVisibility::HitTestInvisible);
    return Label;
}

UButton* UContextScreen::Button(const TCHAR* Name, const FString& Label)
{
    auto* Result = Make<UButton>(Name);
    auto* ContentSlot = CastChecked<UButtonSlot>(Result->AddChild(Text(*(FString(Name) + TEXT("Label")), Label)));
    ContentSlot->SetHorizontalAlignment(HAlign_Fill);
    ContentSlot->SetVerticalAlignment(VAlign_Center);
    Result->SetToolTipText(FText::FromString(Label));
    Result->OnReceivedFocus.BindWeakLambda(this, [this, Result]()
    {
        StyleButtons();
        if (!Attempt.bPaused) Scroll->ScrollWidgetIntoView(Result, false);
    });
    Result->OnLostFocus.BindWeakLambda(this, [this]() { StyleButtons(); });
    return Result;
}

UImage* UContextScreen::Picture(const TCHAR* Name, const TCHAR* Path)
{
    auto* Result = Make<UImage>(Name);
    Result->SetBrushFromTexture(LoadObject<UTexture2D>(nullptr, Path), true);
    Result->SetVisibility(ESlateVisibility::HitTestInvisible);
    return Result;
}

UImage* UContextScreen::VectorPicture(const TCHAR* Name, const TCHAR* File, FVector2D Dimensions)
{
    auto* Image = Make<UImage>(Name);
    const FString Path = FPaths::ProjectContentDir() / TEXT("UI/G/Vector") / File;
    const bool Present = IFileManager::Get().FileExists(*Path);
    if (Present) Image->SetBrush(FSlateVectorImageBrush(Path, Dimensions));
    Image->SetVisibility(Present ? ESlateVisibility::HitTestInvisible : ESlateVisibility::Collapsed);
#if WITH_ACCESSIBILITY
    Image->TakeWidget()->SetAccessibleBehavior(EAccessibleBehavior::NotAccessible);
#endif
    return Image;
}

TSharedRef<SWidget> UContextScreen::RebuildWidget()
{
    if (!WidgetTree) WidgetTree = NewObject<UWidgetTree>(this, TEXT("WidgetTree"));
    if (!WidgetTree->RootWidget) Build();
    return Super::RebuildWidget();
}

void UContextScreen::Build()
{
    SetIsFocusable(true);
    bReady = Question.Load(FPaths::ProjectContentDir() / TEXT("Data/G-Equivocal-Prototype.json"), ContentError);
    if (auto* Face = LoadObject<UFontFace>(nullptr, TEXT("/Game/UI/G/G_Display.G_Display")))
    {
        auto* RuntimeFont = NewObject<UFont>(this);
        RuntimeFont->FontCacheType = EFontCacheType::Runtime;
        FTypefaceEntry Entry(TEXT("Regular"));
        Entry.Font = FFontData(Face);
        RuntimeFont->GetMutableInternalCompositeFont().DefaultTypeface.Fonts.Add(Entry);
        DisplayFont = RuntimeFont;
    }
    Root = Make<UCanvasPanel>(TEXT("Root"));
    WidgetTree->RootWidget = Root;
    Background = Picture(TEXT("Background"), TEXT("/Game/UI/G/G_Background.G_Background"));
    Root->AddChild(Background);
    auto* Safe = Make<USafeZone>(TEXT("SafeArea"));
    Root->AddChild(Safe);
    CastChecked<UCanvasPanelSlot>(Safe->Slot)->SetZOrder(1);
    Fill(Safe);
    Scroll = Make<UScrollBox>(TEXT("ReadingScroll"));
    Scroll->SetScrollBarVisibility(ESlateVisibility::Collapsed);
    Scroll->SetScrollWhenFocusChanges(EScrollWhenFocusChanges::InstantScroll);
    Safe->AddChild(Scroll);
    ContentSize = Make<USizeBox>(TEXT("ContentSize"));
    Scroll->AddChild(ContentSize);
    Canvas = Make<UCanvasPanel>(TEXT("Composition"));
    ContentSize->AddChild(Canvas);
    Panel = Picture(TEXT("ReadingPanel"), TEXT("/Game/UI/G/G_Panel.G_Panel"));
    PanelBody = Picture(TEXT("ReadingPanelBody"), TEXT("/Game/UI/G/G_Panel.G_Panel"));
    PanelBottom = Picture(TEXT("ReadingPanelBottom"), TEXT("/Game/UI/G/G_Panel.G_Panel"));
    // Fixed-height UV slices keep ornaments out of the stretchable reading surface.
    auto Slice = [](UImage* Part, float Top, float Bottom)
    {
        auto Brush = Part->GetBrush();
        Brush.SetUVRegion(FBox2f(FVector2f(0, Top), FVector2f(1, Bottom)));
        Part->SetBrush(Brush);
    };
    Slice(Panel, 0, .22f);
    Slice(PanelBody, .22f, .88f);
    Slice(PanelBottom, .88f, 1);
    for (auto* Part : {Panel.Get(), PanelBody.Get(), PanelBottom.Get()}) Canvas->AddChild(Part);
    Spirit = Picture(TEXT("Spirit"), TEXT("/Game/UI/G/G_Spirit.G_Spirit"));
    // Keep the unchanged v001 master; frame its alpha core plus a small margin.
    // Faint generated gutter specks are excluded, not edited out of the source.
    auto SpiritBrush = Spirit->GetBrush();
    SpiritBrush.SetUVRegion(FBox2f(FVector2f(106.f / 1405, 54.f / 1119), FVector2f(1251.f / 1405, 1)));
    Spirit->SetBrush(SpiritBrush);
    Canvas->AddChild(Spirit);
    Brand = Text(TEXT("Brand"), TEXT("WordQuest"));
    Brand->SetColorAndOpacity(FLinearColor::FromSRGBColor(FColor(255, 238, 211)));
    Brand->SetShadowOffset(FVector2D(1, 2));
    Brand->SetShadowColorAndOpacity(Violet);
    Canvas->AddChild(Brand);
    BrandMark = VectorPicture(TEXT("BrandMark"), TEXT("G_Wordmark.svg"), FVector2D(430, 140));
    if (BrandMark->GetVisibility() != ESlateVisibility::Collapsed)
    {
        Accessible(BrandMark, TEXT("WordQuest"));
        Brand->SetVisibility(ESlateVisibility::Collapsed);
    }
    Canvas->AddChild(BrandMark);
    ProgressPlaque = Picture(TEXT("ProgressPlaque"), TEXT("/Game/UI/G/G_ProgressPlaque.G_ProgressPlaque"));
    auto PlaqueBrush = ProgressPlaque->GetBrush();
    // Frame the generated core without editing its raster master.
    PlaqueBrush.SetUVRegion(FBox2f(FVector2f(34.f / 2141, 94.f / 734), FVector2f(2108.f / 2141, 608.f / 734)));
    ProgressPlaque->SetBrush(PlaqueBrush);
    Canvas->AddChild(ProgressPlaque);
    Progress = Text(TEXT("Progress"), TEXT("3 / 7"));
    Progress->SetColorAndOpacity(FLinearColor::White);
    Progress->SetShadowOffset(FVector2D(1, 2));
    Progress->SetShadowColorAndOpacity(Violet);
    Canvas->AddChild(Progress);
    Mode = Text(TEXT("Mode"), TEXT("C O N T E X T   D E T E C T I V E"));
    Word = Text(TEXT("Word"), bReady ? Question.Word : TEXT("Question unavailable"));
    Word->SetWrappingPolicy(ETextWrappingPolicy::AllowPerCharacterWrapping);
    Clue = Text(TEXT("Clue"), bReady ? Question.Clue : ContentError);
    Prompt = Text(TEXT("Prompt"), Question.Prompt);
    Divider = VectorPicture(TEXT("Divider"), TEXT("G_ReadingDivider.svg"), FVector2D(314, 29));
    HeaderDivider = VectorPicture(TEXT("HeaderDivider"), TEXT("G_HeaderDivider.svg"), FVector2D(214, 29));
    Feedback = Text(TEXT("Feedback"), TEXT(""));
    for (auto* Label : {Mode.Get(), Word.Get(), Clue.Get(), Prompt.Get(), Feedback.Get()}) Canvas->AddChild(Label);
    Canvas->AddChild(Divider);
    Canvas->AddChild(HeaderDivider);
    for (int32 I = 0; I < 4; ++I)
    {
        const FString Name = FString::Printf(TEXT("Answer%d"), I);
        FContextAnswerWidgets Answer;
        Answer.Skin = Picture(*(Name + TEXT("Skin")), TEXT("/Game/UI/G/G_AnswerSkin.G_AnswerSkin"));
        auto SkinBrush = Answer.Skin->GetBrush();
        SkinBrush.DrawAs = ESlateBrushDrawType::Box;
        SkinBrush.Margin = FMargin(.085f, .45f);
        // This UV window excludes the generated export's empty margin and stray fringe.
        // The source PNG remains intact; coordinates are recorded in its provenance.
        SkinBrush.SetUVRegion(FBox2f(FVector2f(50.f / 2172, 168.f / 724), FVector2f(2125.f / 2172, 528.f / 724)));
        Answer.Skin->SetBrush(SkinBrush);
        Answer.Skin->SetRenderTransformPivot(FVector2D::ZeroVector);
        if (!SkinBrush.GetResourceObject()) Answer.Skin->SetVisibility(ESlateVisibility::Collapsed);
        Answer.Button = Button(*Name, bReady ? Question.Choices[I] : TEXT("Unavailable"));
        Answer.Label = CastChecked<UTextBlock>(Answer.Button->GetContent());
        Answer.Label->SetJustification(ETextJustify::Left);
        Answer.Label->SetWrappingPolicy(ETextWrappingPolicy::AllowPerCharacterWrapping);
        Answer.Letter = Text(*(Name + TEXT("Letter")), FString::Chr(TCHAR('A' + I)));
        Answer.Badge = Make<UBorder>(*(Name + TEXT("Badge")));
        Answer.Badge->SetPadding(FMargin(0));
        Answer.Badge->SetHorizontalAlignment(HAlign_Center);
        Answer.Badge->SetVerticalAlignment(VAlign_Center);
        Answer.Badge->AddChild(Answer.Letter);
        Answer.BadgeSize = Make<USizeBox>(*(Name + TEXT("BadgeSize")));
        Answer.BadgeSize->AddChild(Answer.Badge);
        Answer.Marker = Text(*(Name + TEXT("Selection")), TEXT(""));
        Answer.MarkerSize = Make<USizeBox>(*(Name + TEXT("SelectionSize")));
        Answer.MarkerSize->AddChild(Answer.Marker);
        auto* Row = Make<UHorizontalBox>(*(Name + TEXT("Row")));
        Row->AddChildToHorizontalBox(Answer.BadgeSize)->SetVerticalAlignment(VAlign_Center);
        Row->AddChildToHorizontalBox(Answer.MarkerSize)->SetVerticalAlignment(VAlign_Center);
        auto* LabelSlot = Row->AddChildToHorizontalBox(Answer.Label);
        LabelSlot->SetSize(FSlateChildSize(ESlateSizeRule::Fill));
        LabelSlot->SetVerticalAlignment(VAlign_Center);
        Answer.Button->SetContent(Row);
        auto* ContentSlot = CastChecked<UButtonSlot>(Row->Slot);
        ContentSlot->SetHorizontalAlignment(HAlign_Fill);
        ContentSlot->SetVerticalAlignment(VAlign_Center);
        Canvas->AddChild(Answer.Skin);
        Canvas->AddChild(Answer.Button);
        Answers.Add(Answer);
    }
    Answers[0].Button->OnClicked.AddDynamic(this, &UContextScreen::ChooseA);
    Answers[1].Button->OnClicked.AddDynamic(this, &UContextScreen::ChooseB);
    Answers[2].Button->OnClicked.AddDynamic(this, &UContextScreen::ChooseC);
    Answers[3].Button->OnClicked.AddDynamic(this, &UContextScreen::ChooseD);
    HintButton = Button(TEXT("Hint"), TEXT("Hint"));
    SubmitButton = Button(TEXT("Submit"), TEXT("Check answer"));
    HintLabel = CastChecked<UTextBlock>(HintButton->GetContent());
    SubmitLabel = CastChecked<UTextBlock>(SubmitButton->GetContent());
    HintIcon = VectorPicture(TEXT("HintIcon"), TEXT("G_HintBulb.svg"), FVector2D(40, 56));
    SubmitIcon = VectorPicture(TEXT("SubmitIcon"), TEXT("G_CheckStar.svg"), FVector2D(48, 48));
    auto GroupAction = [this](UButton* Target, UTextBlock* Label, UImage* Icon, const TCHAR* Name)
    {
        auto* IconSize = Make<USizeBox>(*(FString(Name) + TEXT("IconSize")));
        IconSize->AddChild(Icon);
        IconSize->SetVisibility(Icon->GetVisibility());
        auto* Row = Make<UHorizontalBox>(*(FString(Name) + TEXT("Row")));
        Row->AddChildToHorizontalBox(IconSize)->SetVerticalAlignment(VAlign_Center);
        Row->AddChildToHorizontalBox(Label)->SetVerticalAlignment(VAlign_Center);
        Target->SetContent(Row);
        auto* Slot = CastChecked<UButtonSlot>(Row->Slot);
        Slot->SetHorizontalAlignment(HAlign_Center);
        Slot->SetVerticalAlignment(VAlign_Center);
        return IconSize;
    };
    HintIconSize = GroupAction(HintButton, HintLabel, HintIcon, TEXT("Hint"));
    SubmitIconSize = GroupAction(SubmitButton, SubmitLabel, SubmitIcon, TEXT("Submit"));
    PauseButton = Button(TEXT("Pause"), TEXT("II"));
    PauseButton->SetToolTipText(FText::FromString(TEXT("Pause")));
    PauseLabel = CastChecked<UTextBlock>(PauseButton->GetContent());
    PauseIcon = VectorPicture(TEXT("PauseIcon"), TEXT("G_PauseBars.svg"), FVector2D(24, 30));
    if (PauseIcon->GetVisibility() != ESlateVisibility::Collapsed)
    {
        PauseIconSize = Make<USizeBox>(TEXT("PauseIconSize"));
        PauseIconSize->AddChild(PauseIcon);
        PauseButton->SetContent(PauseIconSize);
        auto* PauseContentSlot = CastChecked<UButtonSlot>(PauseIconSize->Slot);
        PauseContentSlot->SetHorizontalAlignment(HAlign_Center);
        PauseContentSlot->SetVerticalAlignment(VAlign_Center);
    }
    HintSkin = Picture(TEXT("HintSkin"), TEXT("/Game/UI/G/G_HintSkin.G_HintSkin"));
    SubmitSkin = Picture(TEXT("SubmitSkin"), TEXT("/Game/UI/G/G_CheckSkin.G_CheckSkin"));
    PauseSkin = Picture(TEXT("PauseSkin"), TEXT("/Game/UI/G/G_PauseSkin.G_PauseSkin"));
    auto ActionBox = [](UImage* Image, float HorizontalMargin)
    {
        auto Brush = Image->GetBrush();
        Brush.DrawAs = ESlateBrushDrawType::Box;
        Brush.Margin = FMargin(HorizontalMargin, .45f);
        Image->SetBrush(Brush);
        Image->SetRenderTransformPivot(FVector2D::ZeroVector);
    };
    ActionBox(HintSkin, .195f);
    ActionBox(SubmitSkin, .145f);
    auto FrameSkin = [](UImage* Image, FVector2f TopLeft, FVector2f BottomRight)
    {
        auto Brush = Image->GetBrush();
        Brush.SetUVRegion(FBox2f(TopLeft, BottomRight));
        Image->SetBrush(Brush);
    };
    // Runtime framing excludes export padding; unchanged masters/provenance live in ArtSource.
    FrameSkin(HintSkin, FVector2f(86.f / 1998, 125.f / 787), FVector2f(1908.f / 1998, 646.f / 787));
    FrameSkin(SubmitSkin, FVector2f(108.f / 1983, 151.f / 793), FVector2f(1876.f / 1983, 627.f / 793));
    FrameSkin(PauseSkin, FVector2f(96.f / 1254, 100.f / 1254), FVector2f(1159.f / 1254, 1129.f / 1254));
    Canvas->AddChild(HintSkin);
    Canvas->AddChild(HintButton);
    Canvas->AddChild(SubmitSkin);
    Canvas->AddChild(SubmitButton);
    Canvas->AddChild(PauseSkin);
    Canvas->AddChild(PauseButton);
    HintButton->OnClicked.AddDynamic(this, &UContextScreen::Hint);
    SubmitButton->OnClicked.AddDynamic(this, &UContextScreen::Submit);
    PauseButton->OnClicked.AddDynamic(this, &UContextScreen::TogglePause);
    Modal = Make<UCanvasPanel>(TEXT("PauseModal"));
    Root->AddChild(Modal);
    CastChecked<UCanvasPanelSlot>(Modal->Slot)->SetZOrder(10);
    Fill(Modal);
    ModalShade = Make<UImage>(TEXT("PauseShade"));
    ModalShade->SetColorAndOpacity(FLinearColor(.015f, .008f, .04f, .97f));
    Modal->AddChild(ModalShade);
    Fill(ModalShade);
    PauseTitle = Text(TEXT("PauseTitle"), TEXT("Paused"));
    PauseTitle->SetColorAndOpacity(FLinearColor::White);
    Modal->AddChild(PauseTitle);
    ResumeButton = Button(TEXT("Resume"), TEXT("Resume"));
    TextSizeButton = Button(TEXT("TextSize"), TEXT("Text size: 100%"));
    ResetButton = Button(TEXT("Reset"), TEXT("Try this question again"));
    for (auto* B : {ResumeButton.Get(), TextSizeButton.Get(), ResetButton.Get()}) Modal->AddChild(B);
    ResumeButton->OnClicked.AddDynamic(this, &UContextScreen::TogglePause);
    TextSizeButton->OnClicked.AddDynamic(this, &UContextScreen::ToggleTextSize);
    ResetButton->OnClicked.AddDynamic(this, &UContextScreen::ResetAttempt);
    ResumeButton->SetNavigationRuleExplicit(EUINavigation::Next, TextSizeButton);
    TextSizeButton->SetNavigationRuleExplicit(EUINavigation::Next, ResetButton);
    ResetButton->SetNavigationRuleExplicit(EUINavigation::Next, ResumeButton);
    ResumeButton->SetNavigationRuleExplicit(EUINavigation::Previous, ResetButton);
    TextSizeButton->SetNavigationRuleExplicit(EUINavigation::Previous, ResumeButton);
    ResetButton->SetNavigationRuleExplicit(EUINavigation::Previous, TextSizeButton);
}

void UContextScreen::NativeConstruct()
{
    Super::NativeConstruct();
    Accessible(PauseButton, TEXT("Pause"));
    Accessible(Progress, TEXT("Prototype question 3 of 7"));
    Refresh();
}

void UContextScreen::NativeTick(const FGeometry& Geometry, float DeltaTime)
{
    Super::NativeTick(Geometry, DeltaTime);
    const FVector2D Size = Scroll->GetCachedGeometry().GetLocalSize();
    if (Size.X > 1 && Size.Y > 1 && (bLayoutDirty || !Size.Equals(LastSize, .5)))
    {
        Layout(Size);
        LastSize = Size;
        bLayoutDirty = false;
    }
}

void UContextScreen::Layout(FVector2D Size)
{
    const float Width = Size.X > Size.Y ? FMath::Min(float(Size.X), 884.f) : float(Size.X);
    Scale = Width / 884.f;
    const float S = Scale;
    const float X = (Size.X - Width) * .5f;
    const float Hero = Size.X > Size.Y ? 235.f : 521.f;
    const float PanelY = Hero * S;
    auto Place = [X, S](UWidget* Widget, float Left, float Top, float W, float H)
    { Bounds(Widget, X + Left * S, Top * S, W * S, H * S); };
    // Cover the viewport without distorting the backdrop's moon or architecture.
    const FVector2D RootSize = GetCachedGeometry().GetLocalSize();
    const float BGScale = FMath::Max(float(RootSize.X) / 884.f, float(RootSize.Y) / 1779.f);
    Bounds(Background, (RootSize.X - 884 * BGScale) / 2, 0, 884 * BGScale, 1779 * BGScale);
    Place(Brand, 211, 16, 465, 137);
    // The live fallback must fit its title region beside the minimum-size Pause.
    Font(Brand, 95 * S, false, DisplayFont);
    Place(BrandMark, 229, 23, 430, 140);
    Place(ProgressPlaque, 352, 169, 178, 61);
    Font(Progress, 35 * S, true);
    Progress->ForceLayoutPrepass();
    const float ProgressHeight = Progress->GetDesiredSize().Y;
    Bounds(Progress, X + 352 * S, 169 * S + FMath::Max(0.f, (61 * S - ProgressHeight) * .5f), 178 * S, ProgressHeight);
    const float PauseW = FMath::Max(71 * S, 48.f);
    Bounds(PauseButton, X + Width - PauseW - 25 * S, 31 * S, PauseW, FMath::Max(75 * S, 48.f));
    Bounds(PauseSkin, X + Width - PauseW - 25 * S, 31 * S, PauseW, FMath::Max(75 * S, 48.f));
    Font(PauseLabel, FMath::Max(36 * S, 14.f), true);
    if (PauseIconSize)
    {
        PauseIconSize->SetWidthOverride(FMath::Max(24 * S, 14.f));
        PauseIconSize->SetHeightOverride(FMath::Max(30 * S, 18.f));
    }
    // Contain the framed 1145x1065 export in the reference's 207x185 region.
    // Preserve its aspect rather than stretching the companion/lantern.
    const float SpiritAspect = 1145.f / 1065;
    const float SpiritW = FMath::Min(207.f, 185.f * SpiritAspect);
    const float SpiritH = SpiritW / SpiritAspect;
    Place(Spirit, 82 + (207 - SpiritW) * .5f, (Hero == 521 ? 276 : 85) + (185 - SpiritH) * .5f, SpiritW, SpiritH);
    Spirit->SetVisibility(Hero == 521 ? ESlateVisibility::HitTestInvisible : ESlateVisibility::Collapsed);
    ProgressPlaque->SetVisibility(Hero == 521 && ProgressPlaque->GetBrush().GetResourceObject()
        ? ESlateVisibility::HitTestInvisible : ESlateVisibility::Collapsed);
    Progress->SetVisibility(Hero == 521 ? ESlateVisibility::HitTestInvisible : ESlateVisibility::Collapsed);
    auto Measure = [this, S](UTextBlock* Label, float Pixels, float W, float MinHeight, bool Bold = false)
    {
        Font(Label, FMath::Max(Pixels * S * TextScale, 14.f), Bold);
        Label->SetWrapTextAt(W);
        Label->ForceLayoutPrepass();
        return FMath::Max(MinHeight, Label->GetDesiredSize().Y + 4 * S);
    };
    auto PutText = [X, this](UTextBlock* Label, float Left, float Y, float W, float H)
    { Bounds(Label, X + Left, Y, W, H); };
    float Y = PanelY + 89 * S;
    Mode->SetText(FText::FromString(TEXT("C O N T E X T   D E T E C T I V E")));
    Font(Mode, FMath::Max(28 * S * TextScale, 14.f));
    Mode->SetWrapTextAt(0);
    Mode->ForceLayoutPrepass();
    // Drop decorative letter spacing when it would split words across lines.
    if (Mode->GetDesiredSize().X > 660 * S)
        Mode->SetText(FText::FromString(TEXT("CONTEXT DETECTIVE")));
    float H = Measure(Mode, 28, 660 * S, 40 * S);
    PutText(Mode, 112 * S, Y, 660 * S, H);
    Bounds(HeaderDivider, X + 335 * S, Y + H - 4 * S, 214 * S, 29 * S);
    Y += H + 29 * S;
    H = Measure(Word, 80, 670 * S, 90 * S, true);
    PutText(Word, 107 * S, Y, 670 * S, H);
    Y += H + 14 * S;
    H = Measure(Clue, 37, 580 * S, 90 * S);
    PutText(Clue, 152 * S, Y, 580 * S, H);
    Y += H + 8 * S;
    Bounds(Divider, X + 285 * S, Y - 2 * S, 314 * S, 29 * S);
    Y += 32 * S;
    H = Measure(Prompt, 35, 650 * S, 55 * S, true);
    PutText(Prompt, 117 * S, Y, 650 * S, H);
    Y += H + 12 * S;
    for (const auto& Answer : Answers)
    {
        const float BadgeDiameter = FMath::Max(70 * S * TextScale, 32.f);
        const float MarkerWidth = FMath::Max(37 * S * TextScale, 18.f);
        Answer.BadgeSize->SetWidthOverride(BadgeDiameter);
        Answer.BadgeSize->SetHeightOverride(BadgeDiameter);
        Answer.MarkerSize->SetWidthOverride(MarkerWidth);
        Font(Answer.Letter, FMath::Max(35 * S * TextScale, 14.f), true);
        Font(Answer.Marker, FMath::Max(24 * S * TextScale, 14.f), true);
        const auto SlotPadding = CastChecked<UButtonSlot>(Answer.Button->GetContent()->Slot)->GetPadding();
        const float LabelWidth = 666 * S - 48 * S - BadgeDiameter - MarkerWidth - SlotPadding.Left - SlotPadding.Right;
        H = Measure(Answer.Label, 35, LabelWidth, FMath::Max(95 * S, 48.f));
        H = FMath::Max3(H, float(Answer.Label->GetDesiredSize().Y) + 30 * S, BadgeDiameter + 12 * S);
        Bounds(Answer.Button, X + 109 * S, Y, 666 * S, H);
        if (const auto* Texture = Cast<UTexture2D>(Answer.Skin->GetBrush().GetResourceObject()))
        {
            // Slate texture-box borders use actual texture pixels, not Brush.ImageSize.
            // Scale a texture-sized image so borders keep their reference size as rows grow.
            const float TextureWidth = FMath::Max(Texture->GetSizeX(), 1);
            const float TextureHeight = FMath::Max(Texture->GetSizeY(), 1);
            const FVector2D SkinScale(666 * S / TextureWidth, 95 * S / TextureHeight);
            Bounds(Answer.Skin, X + 109 * S, Y, TextureWidth, H / SkinScale.Y);
            Answer.Skin->SetRenderScale(SkinScale);
        }
        Y += H + 17 * S;
    }
    Y += 16 * S;
    Font(HintLabel, FMath::Max(34 * S * TextScale, 16.f), true, DisplayFont);
    Font(SubmitLabel, FMath::Max(34 * S * TextScale, 16.f), true, DisplayFont);
    HintIconSize->SetWidthOverride(40 * S * TextScale);
    HintIconSize->SetHeightOverride(56 * S * TextScale);
    SubmitIconSize->SetWidthOverride(48 * S * TextScale);
    SubmitIconSize->SetHeightOverride(48 * S * TextScale);
    CastChecked<UHorizontalBoxSlot>(HintLabel->Slot)->SetPadding(FMargin(HintIcon->GetVisibility() == ESlateVisibility::Collapsed ? 0 : 20 * S * TextScale, 0, 0, 0));
    CastChecked<UHorizontalBoxSlot>(SubmitLabel->Slot)->SetPadding(FMargin(SubmitIcon->GetVisibility() == ESlateVisibility::Collapsed ? 0 : 20 * S * TextScale, 0, 0, 0));
    HintButton->GetContent()->ForceLayoutPrepass();
    SubmitButton->GetContent()->ForceLayoutPrepass();
    const FVector2D HintDesired = HintButton->GetContent()->GetDesiredSize();
    const FVector2D SubmitDesired = SubmitButton->GetContent()->GetDesiredSize();
    auto ButtonPadding = [S](UButton* B)
    {
        const FMargin Padding = CastChecked<UButtonSlot>(B->GetContent()->Slot)->GetPadding();
        return FVector2D(48 * S + Padding.Left + Padding.Right, 10 * S + Padding.Top + Padding.Bottom);
    };
    const FVector2D HintPadding = ButtonPadding(HintButton);
    const FVector2D SubmitPadding = ButtonPadding(SubmitButton);
    const float ActionHeight = FMath::Max(FMath::Max(113 * S, 48.f),
        float(FMath::Max(HintDesired.Y + HintPadding.Y, SubmitDesired.Y + SubmitPadding.Y)));
    // Stack when enlarged type or either complete icon/label group cannot fit.
    const bool StackActions = TextScale > 1.2f || HintDesired.X + HintPadding.X > 287 * S
        || SubmitDesired.X + SubmitPadding.X > 388 * S;
    Bounds(HintButton, X + 99 * S, Y, (StackActions ? 688 : 287) * S, ActionHeight);
    Bounds(SubmitButton, X + (StackActions ? 99 : 399) * S, Y + (StackActions ? ActionHeight + 15 * S : 0), (StackActions ? 688 : 388) * S, ActionHeight);
    auto PlaceActionSkin = [S](UImage* Image, float Left, float Top, float W, float H, float ReferenceWidth)
    {
        if (const auto* Texture = Cast<UTexture2D>(Image->GetBrush().GetResourceObject()))
        {
            const float TextureWidth = FMath::Max(Texture->GetSizeX(), 1);
            const float TextureHeight = FMath::Max(Texture->GetSizeY(), 1);
            const FVector2D DrawingScale(ReferenceWidth * S / TextureWidth, 113 * S / TextureHeight);
            Bounds(Image, Left, Top, W / DrawingScale.X, H / DrawingScale.Y);
            Image->SetRenderScale(DrawingScale);
        }
    };
    PlaceActionSkin(HintSkin, X + 99 * S, Y, (StackActions ? 688 : 287) * S, ActionHeight, 287);
    PlaceActionSkin(SubmitSkin, X + (StackActions ? 99 : 399) * S,
        Y + (StackActions ? ActionHeight + 15 * S : 0), (StackActions ? 688 : 388) * S, ActionHeight, 388);
    Y += ActionHeight + (StackActions ? ActionHeight + 15 * S : 0);
    if (!Feedback->GetText().IsEmpty())
    {
        Y += 24 * S;
        H = Measure(Feedback, 29, 630 * S, 0);
        PutText(Feedback, 127 * S, Y, 630 * S, H);
        Y += H;
    }
    // Compensate for transparent export padding, keeping top and bottom fixed.
    const float PanelTop = PanelY - 12 * S;
    const float PanelEnd = Y + 62 * S;
    Bounds(Panel, X + 47 * S, PanelTop, 790 * S, 160 * S);
    Bounds(PanelBody, X + 47 * S, PanelTop + 160 * S, 790 * S, PanelEnd - PanelTop - 260 * S);
    Bounds(PanelBottom, X + 47 * S, PanelEnd - 100 * S, 790 * S, 100 * S);
    ContentSize->SetHeightOverride(FMath::Max(float(Size.Y), Y + 214 * S));
    const float ModalWidth = FMath::Min(float(RootSize.X) - 32.f, 470.f);
    const float ModalX = (RootSize.X - ModalWidth) / 2;
    const float ModalY = FMath::Max(16.f, float(RootSize.Y) / 2 - 150.f);
    Bounds(PauseTitle, ModalX, ModalY, ModalWidth, 52);
    Font(PauseTitle, 32, true, DisplayFont);
    int32 Row = 0;
    for (auto* B : {ResumeButton.Get(), TextSizeButton.Get(), ResetButton.Get()})
    {
        Bounds(B, ModalX, ModalY + 66 + Row++ * 66, ModalWidth, 54);
        Font(CastChecked<UTextBlock>(B->GetContent()), 22, true);
    }
    StyleButtons();
    if (bRevealFeedback)
    {
        Scroll->ScrollWidgetIntoView(Feedback, false);
        bRevealFeedback = false;
    }
}

UTextBlock* UContextScreen::ButtonLabel(UButton* Target) const
{
    if (Target == HintButton) return HintLabel;
    if (Target == SubmitButton) return SubmitLabel;
    if (Target == PauseButton) return PauseLabel;
    for (const auto& Answer : Answers) if (Answer.Button == Target) return Answer.Label;
    return CastChecked<UTextBlock>(Target->GetContent());
}

UImage* UContextScreen::ButtonSkin(UButton* Target) const
{
    if (Target == HintButton) return HintSkin;
    if (Target == SubmitButton) return SubmitSkin;
    if (Target == PauseButton) return PauseSkin;
    for (const auto& Answer : Answers) if (Answer.Button == Target) return Answer.Skin;
    return nullptr;
}

void UContextScreen::SetButtonLabel(UButton* Target, const FString& Label)
{
    ButtonLabel(Target)->SetText(FText::FromString(Label));
    Accessible(Target, Label);
}

void UContextScreen::StyleButtons()
{
    if (!SubmitButton) return;
    auto Apply = [this](UButton* B, bool Primary, bool Selected)
    {
        const bool Focused = B->HasKeyboardFocus();
        auto* Skin = ButtonSkin(B);
        const bool HasSkin = Skin && Skin->GetBrush().GetResourceObject();
        if (Skin)
        {
            Skin->SetVisibility(HasSkin ? ESlateVisibility::HitTestInvisible : ESlateVisibility::Collapsed);
            Skin->SetIsEnabled(B->GetIsEnabled());
        }
        const auto FillColor = HasSkin ? FLinearColor::Transparent : (Primary ? Violet : Pearl);
        const auto Border = Focused ? Ink : (Selected ? Violet : (Primary ? Gold : FLinearColor::White));
        const bool SkinnedAction = HasSkin && (B == HintButton || B == SubmitButton || B == PauseButton);
        float Radius = FMath::Max(35 * Scale, 12.f);
        if (SkinnedAction)
        {
            const auto* Slot = CastChecked<UCanvasPanelSlot>(B->Slot);
            Radius = .5f * FMath::Min(float(Slot->GetSize().X), float(Slot->GetSize().Y));
        }
        const float NormalOutline = SkinnedAction && !Focused ? 0.f : (Focused || Selected ? 4.f : 2.f);
        FButtonStyle Style;
        Style.SetNormal(FSlateRoundedBoxBrush(FillColor, Radius, Border, NormalOutline));
        Style.SetHovered(FSlateRoundedBoxBrush(HasSkin ? FLinearColor(.9f, .86f, 1, .16f) : (Primary ? Violet * .8f : FLinearColor(.78f, .73f, 1)), Radius, Gold, 3.f));
        Style.SetPressed(FSlateRoundedBoxBrush(HasSkin ? FLinearColor(.22f, .16f, .5f, .16f) : (Primary ? Violet * .6f : FLinearColor(.64f, .58f, .91f)), Radius, Ink, 3.f));
        Style.SetDisabled(FSlateRoundedBoxBrush(FillColor, Radius, Border, SkinnedAction ? 0.f : 2.f));
        const float HorizontalPadding = (B == PauseButton ? 8 : 24) * Scale;
        Style.SetNormalPadding(FMargin(HorizontalPadding, 5 * Scale));
        Style.SetPressedPadding(FMargin(HorizontalPadding, 6 * Scale, HorizontalPadding, 4 * Scale));
        B->SetStyle(Style);
        ButtonLabel(B)->SetColorAndOpacity(Primary || (B == PauseButton && HasSkin) ? FLinearColor::White : Ink);
        if (B == PauseButton) PauseIcon->SetColorAndOpacity(HasSkin ? FLinearColor::White : Ink);
    };
    for (int32 I = 0; I < Answers.Num(); ++I)
    {
        const auto& Answer = Answers[I];
        const bool Selected = Attempt.SelectedIndex == I;
        Apply(Answer.Button, false, Selected);
        const float Radius = FMath::Max(70 * Scale * TextScale, 32.f) * .5f;
        Answer.Badge->SetBrush(FSlateRoundedBoxBrush(BadgeFill, Radius, Selected ? Ink : BadgeEdge, Selected ? 3.f : 1.f));
        Answer.Marker->SetText(Selected ? FText::FromString(TEXT(">")) : FText::GetEmpty());
    }
    Apply(SubmitButton, true, false);
    for (auto* B : {HintButton.Get(), PauseButton.Get(), ResumeButton.Get(), TextSizeButton.Get(), ResetButton.Get()}) Apply(B, false, false);
}

void UContextScreen::Refresh()
{
    for (int32 I = 0; I < Answers.Num(); ++I)
    {
        Answers[I].Button->SetIsEnabled(bReady && !Attempt.bSubmitted);
        Answers[I].Skin->SetIsEnabled(bReady && !Attempt.bSubmitted);
        if (bReady)
        {
            const FString Prefix = Attempt.SelectedIndex == I ? TEXT("Selected. ") : TEXT("");
            SetButtonLabel(Answers[I].Button, Question.Choices[I]);
            Accessible(Answers[I].Button, FString::Printf(TEXT("%sOption %c. %s"), *Prefix, TCHAR('A' + I), *Question.Choices[I]));
        }
    }
    HintButton->SetIsEnabled(bReady && !Attempt.bSubmitted && !Attempt.bHintUsed);
    SubmitButton->SetIsEnabled(bReady && !Attempt.bSubmitted);
    SetButtonLabel(SubmitButton, Attempt.bSubmitted ? TEXT("Answer checked") : TEXT("Check answer"));
    SetButtonLabel(HintButton, Attempt.bHintUsed ? TEXT("Hint used") : TEXT("Hint"));
    SetButtonLabel(TextSizeButton, TextScale > 1 ? TEXT("Text size: 200%") : TEXT("Text size: 100%"));
    Scroll->SetIsEnabled(!Attempt.bPaused);
    Modal->SetVisibility(Attempt.bPaused ? ESlateVisibility::Visible : ESlateVisibility::Collapsed);
    StyleButtons();
    bLayoutDirty = true;
}

void UContextScreen::Choose(int32 Index)
{
    if (bReady && Attempt.Select(Index, Question.Choices.Num())) Refresh();
}

void UContextScreen::Submit()
{
    if (!bReady) return;
    const auto Result = Attempt.Submit(Question.CorrectIndex);
    if (Result == EContextResult::Paused || Result == EContextResult::AlreadySubmitted) return;
    FString Message;
    if (Result == EContextResult::NoSelection) Message = TEXT("Choose an answer before checking.");
    else Message = (Attempt.bCorrect ? TEXT("Correct. ") : TEXT("Not quite. ")) + Question.Explanation +
        (Attempt.bHintUsed ? TEXT(" Hint used for this attempt.") : TEXT("")) + TEXT(" Open Pause to try again.");
    Feedback->SetText(FText::FromString(Message));
    bRevealFeedback = true;
    Refresh();
    if (Attempt.bSubmitted) SetUserFocus(GetOwningPlayer());
}

void UContextScreen::Hint()
{
    if (bReady && Attempt.UseHint())
    {
        Feedback->SetText(FText::FromString(Question.Hint));
        bRevealFeedback = true;
        Refresh();
    }
}

void UContextScreen::TogglePause()
{
    if (!Attempt.bPaused)
    {
        PreviousFocus = PauseButton;
        for (const auto& Answer : Answers) if (Answer.Button->HasKeyboardFocus()) PreviousFocus = Answer.Button;
        if (HintButton->HasKeyboardFocus()) PreviousFocus = HintButton;
        if (SubmitButton->HasKeyboardFocus()) PreviousFocus = SubmitButton;
    }
    Attempt.bPaused = !Attempt.bPaused;
    Refresh();
    if (Attempt.bPaused) ResumeButton->SetUserFocus(GetOwningPlayer());
    else if (PreviousFocus && PreviousFocus->GetIsEnabled()) PreviousFocus->SetUserFocus(GetOwningPlayer());
    else SetUserFocus(GetOwningPlayer());
}

void UContextScreen::ResetAttempt()
{
    Attempt = FContextAttempt();
    Feedback->SetText(FText::GetEmpty());
    Refresh();
    Scroll->ScrollToStart();
    SetUserFocus(GetOwningPlayer());
}

void UContextScreen::ToggleTextSize()
{
    TextScale = TextScale > 1 ? 1 : 2;
    Refresh();
}

FReply UContextScreen::NativeOnKeyDown(const FGeometry& Geometry, const FKeyEvent& Event)
{
    const FKey Key = Event.GetKey();
    if (Key == EKeys::Escape || Key == EKeys::P) { TogglePause(); return FReply::Handled(); }
    if (!Attempt.bPaused)
    {
        if (Key == EKeys::One) Choose(0);
        else if (Key == EKeys::Two) Choose(1);
        else if (Key == EKeys::Three) Choose(2);
        else if (Key == EKeys::Four) Choose(3);
        else if (Key == EKeys::H) Hint();
        else if (Key == EKeys::Enter) Submit();
        else return Super::NativeOnKeyDown(Geometry, Event);
        return FReply::Handled();
    }
    return Super::NativeOnKeyDown(Geometry, Event);
}

#if !UE_BUILD_SHIPPING
void UContextScreen::SetProofTextScale(float Value) { TextScale = FMath::Clamp(Value, 1.f, 2.f); Refresh(); }
void UContextScreen::FocusProofAnswer() { Answers[1].Button->SetUserFocus(GetOwningPlayer()); }
void UContextScreen::FocusProofAction() { SubmitButton->SetUserFocus(GetOwningPlayer()); }
void UContextScreen::FocusProofPause() { PauseButton->SetUserFocus(GetOwningPlayer()); }
void UContextScreen::SetProofLongText()
{
    if (!bReady) return;
    Question.Clue += TEXT(" When asked again, the witness carefully avoided giving a definite answer about whether the meeting had happened or whether anyone else had attended.");
    Clue->SetText(FText::FromString(Question.Clue));
    for (int32 I = 0; I < 4; ++I)
    {
        Question.Choices[I] += TEXT(" — consider the uncertainty expressed by the witness in this context.");
        SetButtonLabel(Answers[I].Button, Question.Choices[I]);
    }
    Refresh();
}
#endif
