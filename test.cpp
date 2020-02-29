#include <iostream>
 
using namespace std;
 
int main(void)
 
{
	int n,input,i;
	
	const double EPS = 1.111111111;
	
	cin >> n;
	
	for(i=0;i!=n;i++)
	{
		cin >> input;
		
		cout << int(input*EPS) << "\n";
		
	}
	
	return 0;
}