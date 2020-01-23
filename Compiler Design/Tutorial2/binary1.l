%{
    #include "tokens.h"
%}

%%
"0"		return ZERO;
"1"		return ONE;
" \t"	;
"\n"	return 0;
.		{printf("Not a binary string.");exit(EXIT_FAILURE);}
%%

int yywrap(void){
	return 1;
}