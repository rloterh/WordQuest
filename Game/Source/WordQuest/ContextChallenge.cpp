#include "ContextChallenge.h"
#include "Dom/JsonObject.h"
#include "Misc/FileHelper.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"

bool FContextQuestion::Load(const FString& Filename, FString& Error)
{
    *this = FContextQuestion();
    FString Source;
    TSharedPtr<FJsonObject> Json;
    if (!FFileHelper::LoadFileToString(Source, *Filename) ||
        !FJsonSerializer::Deserialize(TJsonReaderFactory<>::Create(Source), Json) || !Json.IsValid())
    {
        Error = TEXT("The prototype question could not be loaded.");
        return false;
    }
    FContextQuestion Parsed;
    FString Answer;
    const TArray<TSharedPtr<FJsonValue>>* Entries = nullptr;
    if (!Json->TryGetStringField(TEXT("id"), Parsed.Id) || Parsed.Id.IsEmpty() ||
        !Json->TryGetStringField(TEXT("display_word"), Parsed.Word) || Parsed.Word.IsEmpty() ||
        !Json->TryGetStringField(TEXT("clue"), Parsed.Clue) || Parsed.Clue.IsEmpty() ||
        !Json->TryGetStringField(TEXT("question"), Parsed.Prompt) || Parsed.Prompt.IsEmpty() ||
        !Json->TryGetStringField(TEXT("draft_hint"), Parsed.Hint) || Parsed.Hint.IsEmpty() ||
        !Json->TryGetStringField(TEXT("draft_explanation"), Parsed.Explanation) || Parsed.Explanation.IsEmpty() ||
        !Json->TryGetStringField(TEXT("correct_choice_id"), Answer) ||
        !Json->TryGetArrayField(TEXT("choices"), Entries) || Entries->Num() != 4)
    {
        Error = TEXT("The prototype question is incomplete.");
        return false;
    }
    TSet<FString> Ids;
    for (const auto& Entry : *Entries)
    {
        const TSharedPtr<FJsonObject>* Choice = nullptr;
        FString ChoiceId, Text;
        if (!Entry.IsValid() || !Entry->TryGetObject(Choice) || !Choice->IsValid() ||
            !(*Choice)->TryGetStringField(TEXT("id"), ChoiceId) || ChoiceId.IsEmpty() || Ids.Contains(ChoiceId) ||
            !(*Choice)->TryGetStringField(TEXT("text"), Text) || Text.IsEmpty())
        {
            Error = TEXT("The prototype answer options are invalid.");
            return false;
        }
        Ids.Add(ChoiceId);
        if (ChoiceId == Answer) Parsed.CorrectIndex = Parsed.Choices.Num();
        Parsed.Choices.Add(Text);
    }
    if (Parsed.CorrectIndex == INDEX_NONE)
    {
        Error = TEXT("The prototype answer key is invalid.");
        return false;
    }
    *this = MoveTemp(Parsed);
    Error.Reset();
    return true;
}
