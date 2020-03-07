#include <vector>
#include <iostream>
using namespace std;
#define int long long
vector <int> prime;
const int m = 33005;
bool p[m];
vector <int> arr;
signed main()
{
	//ios::sync_with_stdio(0);
	//cin.tie(0);
	
	prime.emplace_back(2);
	for (int i = 3; i <= 33000; i+=2){
		if (p[i] == 0){
			prime.emplace_back(i);
			p[i] = 1;
			for (int j = i*2; j <= 33000; j+=i){
				p[j] = 1;
			}
		}
	}
	int n;
	while(true){
		cin >> n;
		if (n == 0) break;
		arr.clear();
		
		for (int i = 1; i <= n; i++){
			arr.emplace_back(i);
		}
		int now = 0;
		for (int i = 0; i < n - 1; i++){
			now = (now + prime[i]) % arr.size() - 1;
			arr.erase(arr.begin() + now);
		}
		cout << arr[0] << '\n';
	}
	return 0;
}