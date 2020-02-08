#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        string z[numRows];
        if (numRows == 1) return s;
        int index[(numRows - 1) * 2];
        int j = 0;
        for (int i = 0; i < numRows; i++, j++) {
            index[j] = i;
        }
        for (int i = numRows - 2; i >= 1; i--, j++) {
            index[j] = i;
        }
        int i = 0;
        for (auto c : s) {
            z[index[i]].push_back(c);
            i++;
            i %= (numRows - 1) * 2;
        }
        string ans;
        for (auto s : z) {
            ans.append(s);
        }
        return ans;
    }
};

int main(void) {
    Solution s;
    cout << s.convert("PAYPALISHIRING", 4);
}