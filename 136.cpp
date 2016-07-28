#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
    int a = nums[0];
    for (int i = 1; i < numsSize; i++)
        a ^= nums[i];
    return a;
}

int main(void){
	int array[] = {1, 2, 3, 3, 4, 2, 1};
	printf("%d\n", singleNumber(array, 7));

	return 0;
}