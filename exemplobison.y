%{
#include <stdio.h>
%}

%token NUMERO

%%

expressao: termo
         | expressao '+' termo { printf("+ "); }
         | expressao '-' termo { printf("- "); }
termo: fator
     | termo '*' fator { printf("* "); }
     | termo '/' fator { printf("/ "); }
fator: NUMERO { printf("%s ", yytext); }
     | '(' expressao ')' 

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *msg) {
    fprintf(stderr, "Erro de sintaxe: %s\n", msg);
    return 1;
}
