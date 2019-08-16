#include <bits/stdc++.h>
using namespace std;
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int yy ,mm, dd;
	string a, b;
	cin >> yy >> mm >> dd >> a >> b;
	printf("%d/%d/%d\n", yy+1997, mm, dd);
	//cout << "Doodle Name: " << a << "\n" << "Reviews: " << b << "\n";
    printf("Doodle Name: %s\nReviews: %s\n", a.c_str(), b.c_str());
	return 0;
}