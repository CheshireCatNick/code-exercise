#include <stdio.h>
#include <string.h>

char res[200000];
int main(void){
	char s[] = "abc";
    int len = strlen(s);
    int i;
    int count = 0;
    for (i = len - 1; i >= 0; i--){
		res[count] = s[i];
        count++;		
    }
    res[count] = '\0';
    puts(res);
}