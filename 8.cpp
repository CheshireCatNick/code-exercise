#include <stdio.h>
#include <string.h>
#include <ctype.h>

int myAtoi(char* str){
	int i;
	int len = strlen(str);
	// remove space and cut string with non-digit
	int j = 0;
	for (i = 0; i < len; i++){
		if (str[i] == ' ')
			continue;
		if (!isdigit(str[i]) && (str[i] != '+' && str[i] != '-'))
			break;
		str[j] = str[i];
		j++;
	}
	str[j] = '\0';
	len = strlen(str);
	// sign
	int sign = 1;
	if (str[0] == '-'){
		sign = -1;
		strcpy(str, str + 1);
	}
	else if (str[0] == '+')
		strcpy(str, str + 1);
	len = strlen(str);

	// count
	int factor = 1;
	int ans = 0;
	for (i = len - 1; i >= 0; i--){
		if (!isdigit(str[i]))
			return 0;
		ans += (str[i] - '0') * factor;
		factor *= 10;
	}
	return ans * sign;
}

int main(void){
	char s[] = "+1";
	printf("%d\n", myAtoi(s));
	return 0;
}