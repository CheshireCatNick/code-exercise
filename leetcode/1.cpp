#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int s = nums.size();
        vector<int> r;
        unordered_map<int, int> table;
        for (int i = 0; i < s; i++) {
            table[nums[i]] = i;
        }
        unordered_map<int, int>::iterator it;
        for (int i = 0; i < s; i++) {
            int rest = target - nums[i];
            it = table.find(rest);
            if (it != table.end() && it->second != i) {
                r.push_back(i);
                r.push_back(it->second);
                return r;
            }
        }
        return r;
    }
};