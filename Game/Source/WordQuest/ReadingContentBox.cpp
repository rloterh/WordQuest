#include "ReadingContentBox.h"
#include "Components/SizeBoxSlot.h"
#include "Widgets/Layout/SBox.h"

namespace
{
class SReadingContentBox : public SBox
{
protected:
    virtual int32 OnPaint(const FPaintArgs& Args, const FGeometry& Geometry,
        const FSlateRect& CullingRect, FSlateWindowElementList& DrawElements,
        int32 LayerId, const FWidgetStyle& Style, bool bParentEnabled) const override
    {
        // Answer text and result symbols are still learning content after Check.
        // Ignore ancestor disabled shading during painting, without changing any
        // enabled state, hit testing, accessibility state or focus eligibility.
        return SBox::OnPaint(Args, Geometry, CullingRect, DrawElements, LayerId, Style, true);
    }
};
}

TSharedRef<SWidget> UReadingContentBox::RebuildWidget()
{
    MySizeBox = SNew(SReadingContentBox);
    if (GetChildrenCount() > 0)
        CastChecked<USizeBoxSlot>(GetContentSlot())->BuildSlot(MySizeBox.ToSharedRef());
    return MySizeBox.ToSharedRef();
}
