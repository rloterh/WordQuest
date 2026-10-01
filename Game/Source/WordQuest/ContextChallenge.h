#pragma once

#include "CoreMinimal.h"

// Presentation-free prototype state. No campaign rewards or mastery are granted.
struct FContextQuestion
{
    FString Id, Word, Clue, Prompt, Hint, Explanation;
    TArray<FString> Choices;
    int32 CorrectIndex = INDEX_NONE;
    bool Load(const FString& Filename, FString& Error);
};

enum class EContextResult : uint8 { NoSelection, Paused, AlreadySubmitted, Correct, Incorrect };

struct FContextAttempt
{
    int32 SelectedIndex = INDEX_NONE;
    int32 EvaluationCount = 0;
    bool bHintUsed = false;
    bool bSubmitted = false;
    bool bPaused = false;
    bool bCorrect = false;

    bool Select(int32 Index, int32 ChoiceCount)
    {
        if (bPaused || bSubmitted || Index < 0 || Index >= ChoiceCount) return false;
        SelectedIndex = Index;
        return true;
    }
    bool UseHint()
    {
        if (bPaused || bSubmitted || bHintUsed) return false;
        bHintUsed = true;
        return true;
    }
    EContextResult Submit(int32 CorrectIndex)
    {
        if (bPaused) return EContextResult::Paused;
        if (bSubmitted) return EContextResult::AlreadySubmitted;
        if (SelectedIndex == INDEX_NONE || CorrectIndex == INDEX_NONE) return EContextResult::NoSelection;
        bSubmitted = true;
        bCorrect = SelectedIndex == CorrectIndex;
        ++EvaluationCount;
        return bCorrect ? EContextResult::Correct : EContextResult::Incorrect;
    }
};
