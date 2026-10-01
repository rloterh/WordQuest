#include "../ContextChallenge.h"
#include "Misc/AutomationTest.h"
#include "Misc/Paths.h"

#if WITH_DEV_AUTOMATION_TESTS
IMPLEMENT_SIMPLE_AUTOMATION_TEST(FContextAttemptTest, "WordQuest.Context.Attempt",
    EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)
bool FContextAttemptTest::RunTest(const FString&)
{
    FContextAttempt A;
    TestEqual(TEXT("No default selection"), A.SelectedIndex, INDEX_NONE);
    TestTrue(TEXT("Empty submit rejected"), A.Submit(0) == EContextResult::NoSelection);
    TestFalse(TEXT("Invalid option rejected"), A.Select(4, 4));
    A.bPaused = true;
    TestFalse(TEXT("Paused choice rejected"), A.Select(0, 4));
    TestFalse(TEXT("Paused hint rejected"), A.UseHint());
    TestTrue(TEXT("Paused submit rejected"), A.Submit(0) == EContextResult::Paused);
    A.bPaused = false;
    TestTrue(TEXT("Hint recorded"), A.UseHint());
    TestFalse(TEXT("Hint idempotent"), A.UseHint());
    A.Select(1, 4);
    A.Select(0, 4);
    TestTrue(TEXT("Changed selection evaluated"), A.Submit(0) == EContextResult::Correct);
    TestTrue(TEXT("Assistance retained"), A.bHintUsed);
    TestFalse(TEXT("Submitted answer immutable"), A.Select(2, 4));
    TestTrue(TEXT("Duplicate submit rejected"), A.Submit(0) == EContextResult::AlreadySubmitted);
    TestEqual(TEXT("Exactly one evaluation"), A.EvaluationCount, 1);
    for (int32 Index = 0; Index < 4; ++Index)
    {
        FContextAttempt B;
        B.Select(Index, 4);
        B.Submit(0);
        TestEqual(TEXT("Deterministic answer result"), B.bCorrect, Index == 0);
    }
    return true;
}

IMPLEMENT_SIMPLE_AUTOMATION_TEST(FContextFixtureTest, "WordQuest.Context.Fixture",
    EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)
bool FContextFixtureTest::RunTest(const FString&)
{
    FContextQuestion Q;
    FString Error;
    TestTrue(TEXT("Staged fixture loads"), Q.Load(FPaths::ProjectContentDir() / TEXT("Data/G-Equivocal-Prototype.json"), Error));
    TestEqual(TEXT("Four options"), Q.Choices.Num(), 4);
    TestEqual(TEXT("Expected reference answer"), Q.CorrectIndex, 0);
    TestFalse(TEXT("Missing content rejected"), Q.Load(FPaths::ProjectContentDir() / TEXT("Data/DoesNotExist.json"), Error));
    TestEqual(TEXT("Failure clears prior content"), Q.Choices.Num(), 0);
    return true;
}
#endif
