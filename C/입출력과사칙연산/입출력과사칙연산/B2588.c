#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

// °ö¼À

int main(void) {
	int a;
	int b;

	scanf("%d", &a);
	scanf("%d", &b);

	printf("%d\n", a * (b%10));
	printf("%d\n", a * ((b / 10) % 10));
	printf("%d\n", a * ((b / 10) / 10));

	printf("%d\n", a * b);
}