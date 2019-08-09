#include <stdio.h>

// implement a + b without +

int getSum(int a, int b){
    if (b == 0)
        return a;
    return getSum(a ^ b, (a & b) << 1);
}

int main(void){
	
	printf("%d\n", getSum(2, 3));
	return 0;
}