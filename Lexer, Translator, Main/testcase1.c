#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>










 bool isALeapYear(int year) {
	bool result = false ;

	;
	if( year % 4 == 0 ) {
		result = true ;

		;
		if( year % 100 == 0 && year % 400 != 0 ) {
			result = false;
		}
	}

	;
	return result;
}


 int main() {
	;
	int year1 = 0;
	int year2 = 0;

	;
	printf("This program lists all leap years from year1 to year2.\n");
	printf("year1: ");
	scanf("%i", &year1) ;
	printf("year2: ");
	scanf("%i", &year2) ;

	;
	while( year1 <= year2 ) {
		;
		if( isALeapYear(year1) ) {
			printf("%i\n", year1);
		}

		;
		year1 += 1;
	}

	;
	return 0;
}
