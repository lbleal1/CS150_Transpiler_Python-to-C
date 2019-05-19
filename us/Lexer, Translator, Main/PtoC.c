#include <stdio.h>
#include<string.h>
#include<stdlib.h>

 int add ( int x , int y ) { 
int sum = x + y ;
return sum ;
} 

 int main ( ) { 
char* temp = "string_test hehe" ;
int tempI = 6 ;

printf ( "I'M MAKING" ) ;
printf ( "THE P LANGUAGE :D" ) ;

if( tempI <= 10 && tempI > 5 ) { 
tempI += 3 ;
} 
else if( tempI == 9 ) { 
printf ( "NINE LIVES BOI!" ) ;
} 
else { 
printf ( "SAD." ) ;
} 

while ( tempI < 15 ) { 
printf ( "I'm almost there..." ) ;
tempI += 1 ;
if( tempI == 12 ) { 
continue ;
} 
else if( tempI == 13 ) { 
break ;
} 
} 

} 
