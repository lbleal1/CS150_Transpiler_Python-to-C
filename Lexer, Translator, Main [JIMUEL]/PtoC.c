#include <stdio.h>
#include <string.h>
#include <stdlib.h>










 BOOL isALeapYear(int year) {
	BOOL result = FALSE;

	if( year % 4 == 0 ) {
		if( year %  100 == 0 ) {
			if( year % 400 == 0 ) {
				result = TRUE;
			}
		}
	}

	return result;
}

 int main() {
	int year1 = 0;
	int year2 = 0;

	printf("This program lists all leap years from year1 to year2.\n");
	scanf("year1: ", &year1);
	scanf("year2: ", &year2);

	while year1 <= year2 {
		if( isALeapYear(year1) ) {
			printf("%d\n", year1);
		}

		year += 1;
	}

	return 0;
}
