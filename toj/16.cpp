// @topics: two sum
#include <stdio.h>
#define MAX_SCORE 15000

int main(void) {
    int testCaseNum;
    scanf("%d", &testCaseNum);
    while (testCaseNum--) {
        int studentNum;
        scanf("%d", &studentNum);
        int moodScores[studentNum];
        for (int i = 0; i < studentNum; i++) {
            scanf("%d", &moodScores[i]);
        }
        // calculate
        int possibleWeight = MAX_SCORE * 2;
        bool isGoodWeight[possibleWeight + 1];
        for (int i = 0; i < possibleWeight + 1; i++) {
            isGoodWeight[i] = false;
        }
        for (int i = 0; i < studentNum; i++) {
            if (moodScores[i] == 0) continue;
            for (int j = 0; j < studentNum; j++) {
                if (i == j) continue;
                if (moodScores[j] == 0) continue;
                int weight = moodScores[i] + moodScores[j];
                isGoodWeight[weight] = true;
            }
        }
        // ans
        int queryNum;
        scanf("%d", &queryNum);
        while (queryNum--) {
            int weight;
            scanf("%d", &weight);
            if (weight > possibleWeight || weight < 0) puts("So Bad!");
            else if (isGoodWeight[weight]) puts("Good!");
            else puts("So Bad!");
        }
    }
    return 0;
}