#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

// 1998년생인 내가 태국에서는 2541년생?!
int main(void) {
	// 서기: 현재 년도
	// 불기: 현재 년도(서기) + 544(기원전) 
	int year;

	scanf("%d", &year);
	printf("%d", year - 543);
}