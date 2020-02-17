#include <vector>
#include <iostream>
#define int long long
using namespace std;
const int Max = 1e7;
vector <pair <int, int> > a;
vector <pair <int, int> > b;
signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, x, y;
	cin >> n >> m;
	while(n--){
		cin >> x >> y;
		a.emplace_back(x, y);
	}
	sort (a.begin(), a.end());
	if (a[0].first != 0){
		cout << "NO";
	}else{
		bool c=0;
		while(a.size() > 1 && c == 0){
			if (a[1].first <= a[0].second){
				if (a[0].second <= a[1].second)
					a[0].second = a[1].second;
				a.erase(a.begin()+1);
			}else{
				c=1;
			}
		}
		if (a[0].second == m){
			cout << "YES";
		}else{
			cout << "NO";
		}
	}
}