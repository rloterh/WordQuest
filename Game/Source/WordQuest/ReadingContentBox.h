#pragma once

#include "CoreMinimal.h"
#include "Components/SizeBox.h"
#include "ReadingContentBox.generated.h"

// Static learning content can remain readable inside an unavailable control.
// This changes painting only; the parent still controls input and navigation.
UCLASS(NotBlueprintable)
class WORDQUEST_API UReadingContentBox : public USizeBox
{
    GENERATED_BODY()
protected:
    virtual TSharedRef<SWidget> RebuildWidget() override;
};
