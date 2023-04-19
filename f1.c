#include <stdio.h>
#include "f1.tab.h"
// #include "lex.yy.c"
extern int yyparse();
extern int yylex();

void yyerror(const char* s) {}


int main(void) {
    // Realiza a análise sintática da entrada padrão
    int token;
    while ((token = yylex())) {
        // printf("Token encontrado: %d\n", token); 
        /* não faz nada */
    }    
    
    yyparse();

    return 0;
}
