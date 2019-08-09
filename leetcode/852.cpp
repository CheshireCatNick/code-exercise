class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int li = 0, ri = A.size();
        while (li != ri - 1) {
            int mi = (ri + li) / 2;
            if (A[mi - 1] < A[mi]) {
                if (A[mi] < A[mi + 1]) {
                    li = mi;
                }
                else return mi;
            }
            else {
                if (A[mi] > A[mi + 1]) {
                    ri = mi + 1;
                }
                else return mi;
            }
        }
        return li;
    }
};