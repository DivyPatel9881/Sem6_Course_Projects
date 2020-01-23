%{
    #include <stdio.h>
    #include <stdlib.h>
    #include "binary2.tab.h"
    extern int yylval;
%}

%%
"0"     {yylval = 0; return ZERO;}
"1"     {yylval = 1; return ONE;}
" \t"   ;
"\n"    return 0;
.       {printf("Not a binary string.");exit(EXIT_FAILURE);}
%%

int yywrap(void){
    return 1;
}