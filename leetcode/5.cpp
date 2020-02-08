#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// the optimal solution is O(n) but it's complicated
// anther way is to find lcs(s, reverse(s))
/* // directly find
int getPalindromeLength(char* s, int l, int r) {
    int sl = strlen(s);
    int len = 0;
    while (l >= 0 && r < sl && s[l] == s[r]) {
        l--;
        r++;
        len++;
    }
    return len;
}
char* longestPalindrome(char* s) {
    int l = strlen(s);
    if (l == 0) {
        char *ans = (char*)malloc(sizeof(char));
        ans[0] = '\0';
        return ans;
    }
    int best = 0, start = 0, tBest = 0, tStart = 0;
    for (float axis = 0; axis < l; axis += 0.5) {
        if (floor(axis) == axis) {
            tBest = getPalindromeLength(s, (int)(axis - 1), (int)(axis + 1)) * 2 + 1;
            tStart = (int)axis - (tBest - 1) / 2;
        }
        else {
            tBest = getPalindromeLength(s, (int)(axis - 0.5), (int)(axis + 0.5)) * 2;
            tStart = (int)(axis + 0.5) - tBest / 2;
        }
        if (tBest > best) {
            best = tBest;
            start = tStart;
        }
    }
    char *ans = (char*)malloc(sizeof(char) * best + 1);
    strncpy(ans, &s[start], best);
    ans[best] = '\0';
    return ans;
}
*/
// dp
char* longestPalindrome(char* s) {
    int l = strlen(s);
    if (l == 0) {
        char *ans = (char*)malloc(sizeof(char));
        ans[0] = '\0';
        return ans;
    }
    int isPal[l][l];
    memset(isPal, 0, l * l * sizeof(int));
    for (int i = 0; i < l; i++) {
        isPal[i][i] = 1;
        if (s[i] == s[i + 1]) isPal[i][i + 1] = 1;        
    }
    for (int j = 2; j < l; j++) {
        for (int i = 0; i <= j - 2; i++) {
            isPal[i][j] = (isPal[i + 1][j - 1]) && (s[i] == s[j]);
        }
    }
    int start = 0, best = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < l; j++) {
            //printf("%d", isPal[i][j]);
            if (isPal[i][j] && j - i + 1 > best) {
                start = i;
                best = j - i + 1;
            }
        }
        //puts("");
    }
    char *ans = (char*)malloc(sizeof(char) * best + 1);
    strncpy(ans, &s[start], best);
    ans[best] = '\0';
    return ans;
}

int main(void) {
    printf("%s\n", longestPalindrome("babad"));
    return 0;
}