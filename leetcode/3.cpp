#include <stdio.h>
#include <string.h>
/* O(2n) solution
int lengthOfLongestSubstring(char * s){
    int i = 0, j = 0, l = strlen(s), maxL = 0, curL = 0;
    int hasAppear[256];
    memset(hasAppear, 0, 256 * sizeof(int));
    while (j != l) {
        if (!hasAppear[s[j]]) {
            hasAppear[s[j]] = 1;
            j++;
            curL++;
            maxL = (curL > maxL) ? curL : maxL;
        }
        else {
            hasAppear[s[i]] = 0;
            i++;
            curL--;
        }
    }
    return maxL;
}
*/
// O(n) solution
int lengthOfLongestSubstring(char * s){
    int l = strlen(s), maxL = 0, curL = 0;
    int appearPos[256];
    memset(appearPos, -1, 256 * sizeof(int));
    for (int j = 0; j < l; j++) {
        if (appearPos[s[j]] == -1 || appearPos[s[j]] < j - curL) {
            appearPos[s[j]] = j;
            curL++;
            maxL = (curL > maxL) ? curL : maxL;
        }
        else {
            curL = j - appearPos[s[j]];
            appearPos[s[j]] = j;
        }
    }
    return maxL;
}
int main(void) {
    printf("%d\n", lengthOfLongestSubstring("tmmzuxt"));
    return 0;
}