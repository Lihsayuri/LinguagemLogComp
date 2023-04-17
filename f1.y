%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lex.yy.h"
%}

%token BEGIN_PROGRAM
%token END_PROGRAM
%token REF_VAR_ATRIBUTE
%token VAR_TYPE
%token LOOP_ON
%token LOOP_OFF
%token SETUP
%token RADIO_ON
%token RADIO_OFF
%token RADIO_CHECK
%token SILENCE
%token COPY
%token CALL
%token IN
%token LOGICAL
%token THEN
%token NEED 
%token BOOLEAN
%token OPERATOR
%token SECTOR
%token TYRE_TYPE
%token TYRE_STATUS
%token COMMA
%token OPEN_PARENTHESIS
%token CLOSE_PARENTHESIS
%token OPEN_BRACKETS
%token CLOSE_BRACKETS
%token OPEN_BRACES
%token CLOSE_BRACES
%token IS
%token STRING
%token IDENTIFIER
%token INT
%token FLOAT
%token NEWLINE

%%


termo: INT
     | IDENTIFIER
     ;

tuple_int: '(' INT ',' INT ')'
tuple_drs: '(' SECTOR {',' SECTOR} ',' INT ')'
tyre: '{' TYRE_TYPE ',' TYRE_STATUS '}'
tyre_set: '{' tyre {',' tyre} '}'
operacao: termo
        | operacao OPERATOR termo
        ;
value: STRING
     | INT
     | FLOAT
     | BOOLEAN
     | tuple_int
     | tuple_drs
     | tyre
     | tyre_set
     | operacao
     ;

structure : BEGIN_PROGRAM program END_PROGRAM
          ;


program : var_declaration
         | loop
         | setup
         | radiocheck
         | call
         ;

var_declaration: VAR_TYPE IDENTIFIER IS value NEWLINE

loop: LOOP_ON race_loop program LOOP_OFF NEWLINE

race_loop: OPEN_BRACKETS INT CLOSE_BRACKETS
         ;

setup: SETUP setupfunction program RADIO_OFF NEWLINE

setupfunction: IDENTIFIER NEED VAR_TYPE IDENTIFIER {COMMA VAR_TYPE IDENTIFIER} NEWLINE RADIO_ON
       ;

radiocheck: RADIO_CHECK radiocheckcondition program COPY NEWLINE [SILENCE program COPY NEWLINE]


radiocheckcondition: (IDENTIFIER | REF_VAR_ATRIBUTE) (IS | IN) (value | IDENTIFIER | REF_VAR_ATRIBUTE) {LOGICAL (IDENTIFIER | REF_VAR_ATRIBUTE) (IS | IN) (value | IDENTIFIER | REF_VAR_ATRIBUTE)} THEN
                  ;

call : CALL callsetup COPY NEWLINE
     ;

callsetup: IDENTIFIER NEED VAR_TYPE IDENTIFIER {COMMA VAR_TYPE IDENTIFIER}
       ;


%%

int main() {
    yyparse();
    return 0;
}

void yyerror(char* s) {
    printf("Error: %s\n", s);
}