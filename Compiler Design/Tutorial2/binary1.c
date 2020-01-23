#include <stdio.h>
#include <stdlib.h>
#include "tokens.h"

extern int yylex();

int decimal = 0;

int main(){
    int tokenValue = yylex();
    while(tokenValue){
        if(tokenValue==ONE){
            decimal = decimal*2 + 1;
        }
        else{
            decimal = decimal*2;
        }
        tokenValue = yylex();
    }
    printf("Decimal value of the following binary string is %d.\n",decimal);
    return 0;
}