class Solution {
    vector<int> pa;
    int find(int x)
    {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }
public:
    int maxEvents(vector<vector<int>>& events) {
        vector<array<int, 2>> vp;
        for (auto a : events)
            vp.push_back({a[1], a[0]});
        pa.resize(100000 + 5);
        for (int i = 0; i <= 100004; ++i)
            pa[i] = i;
        sort(vp.begin(), vp.end());
        int ans = 0;
        for (auto a : vp) {
            int l = a[1], r = a[0];
            int i = find(l);
            if (i <= r)
                pa[i] = i + 1, ++ans;
        }
        return ans;
    }
};
