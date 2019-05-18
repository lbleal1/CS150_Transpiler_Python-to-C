#include <stdio.h>
#define bool int
#define true 1
#define false 0

int input;
int copy;
int x;
x  = 0;
int i;
 printf("Input N: ");
 printf("%d",input);
scanf("%d",&input);
copy  = input;
for(i  = 0;i <input;i +=1)
{ 
if(!copy ==0)
{ 


x  = *10;
x  = +(copy  % 10);
copy  = /10;

 }
 }

int main(){

if(x ==input)
{ 
 printf("PALINDROME\n");
 }
if(!x ==input)
{ 
 printf("NOT PALINDROME\n");
 }

	return 0;
}