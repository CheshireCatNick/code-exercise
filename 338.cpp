#include <stdio.h>
#include <stdlib.h>

int getBits(int* ans, int i, int phase){
	if (i == 0) return 0;
	if (i == 1)	return 1;
	if (i == 2) return 1;
	if (i == 3) return 2;
	phase /= 4;
	// printf("i = %d phase = %d\n", i, phase);
	if (i / phase == 2){
		return ans[phase + i % phase];
	}
	else if (i / phase == 3){
		return ans[phase + i % phase] + 1;
	}
}

int* countBits(int num, int* returnSize){
	*returnSize = num + 1;
	int* ans = (int*) malloc(sizeof(int) * (*returnSize));
	// printf("%d\n", *returnSize);
	int phase = 1;
	for (int i = 0; i <= num; i++){
		if (phase == i)
			phase *= 2;
		ans[i] = getBits(ans, i, phase);
	}
	return ans;
}

int main(void){
	int num = 2;
	int returnSize;

	int* ans = countBits(num, &returnSize);

	for (int i = 0; i < returnSize; i++){
		printf("%d\n", ans[i]);
	}
	return 0;
}
