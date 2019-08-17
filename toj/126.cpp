#include <stdio.h>
#define MAX_SCORE_NUM 100
#define MAX_SCORE 10000
using namespace std;

bool isAvailableSum[2][2 * MAX_SCORE + 10];
int ans[MAX_SCORE_NUM + 10];

void calcAns(int maxScore, int scoreNum) {
    int closestScore;
    for (int i = maxScore; i >= 0; i--) {
        if (isAvailableSum[scoreNum % 2][i]) {
            closestScore = i;
        }
        ans[i] = closestScore;
    }
    return;
}
void calcSubsetSum(int* scores, int maxScore, int scoreNum) {
    for (int i = 0; i < 2; i++) {
        isAvailableSum[i][0] = true;
    }
    for (int j = 1; j <= maxScore; j++) {
        isAvailableSum[0][j] = false;
    }
    // only store two rows to save memory usage
    for (int i = 1; i <= scoreNum; i++) {
        for (int j = 1; j <= maxScore; j++) {
            if (isAvailableSum[(i - 1) % 2][j] || 
                scores[i - 1] == j || 
                isAvailableSum[(i - 1) % 2][j - scores[i - 1]]) isAvailableSum[i % 2][j] = true;
            else isAvailableSum[i % 2][j] = false;
        }
    }
    return;
}
int main(void) {
    int scoreNum, queryNum;
    scanf("%d%d", &scoreNum, &queryNum);
    int scores[scoreNum], shift = 0, score;
    for (int i = 0; i < scoreNum; i++) {
        scanf("%d", &score);
        scores[i] = score * 2;
        shift += score;
    }
    calcSubsetSum(scores, shift * 2, scoreNum);
    calcAns(shift * 2, scoreNum);
    for (int i = 0; i < queryNum; i++) {
        int query;
        scanf("%d", &query);
        printf("%d\n", ans[query + shift] - shift);
    }
    return 0;
}