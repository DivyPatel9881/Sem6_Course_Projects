%{
    #include<stdio.h>

    void yyerror(char *s);
%}

%token ONE ZERO

%% 
BIN     : LEFT {printf("%d", $$);}
        ;
LEFT    : LEFT RIGHT {$$=$1*2+$2;}
        | RIGHT {$$=$1;}
        ;
RIGHT   : ZERO {$$=$1;}
        | ONE {$$=$1;}
        ;
%%

int main(){
    return yyparse();
}

void yyerror(char *s){
    printf("%s",s);
}