%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// extern int yylex();

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
%start structure

%%

tuple_int: OPEN_PARENTHESIS INT COMMA INT CLOSE_PARENTHESIS ;

manysector: COMMA SECTOR
          | manysector COMMA SECTOR
          ;

tuple_drs:  OPEN_PARENTHESIS SECTOR COMMA INT CLOSE_PARENTHESIS 
           | OPEN_PARENTHESIS SECTOR manysector COMMA INT CLOSE_PARENTHESIS 
           ;

tyre: OPEN_BRACES TYRE_TYPE COMMA TYRE_STATUS CLOSE_BRACES ;
tyre_set: OPEN_BRACES tyre CLOSE_BRACES
        | OPEN_BRACES tyre manytires CLOSE_BRACES
        ;

manytires : COMMA tyre
          | COMMA tyre manytires
          ;

manyidentifiers: COMMA VAR_TYPE IDENTIFIER
                | COMMA VAR_TYPE IDENTIFIER manyidentifiers
                ;

termo: INT
     | IDENTIFIER
     ;

operacao: termo
        | operacao OPERATOR termo
        ;

value: STRING
     /* | INT  consigo pegar o int atraves de operacao - termo - int*/ 
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

var_declaration: VAR_TYPE IDENTIFIER IS value NEWLINE;

loop: LOOP_ON race_loop program LOOP_OFF NEWLINE;

race_loop: OPEN_BRACKETS INT CLOSE_BRACKETS
         ;

setup: SETUP setupfunction program RADIO_OFF NEWLINE ;

setupfunction: IDENTIFIER NEED VAR_TYPE IDENTIFIER  NEWLINE RADIO_ON
               | IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers NEWLINE RADIO_ON
       ;


radiocheck: RADIO_CHECK radiocheckcondition program COPY NEWLINE else
         ;

else: SILENCE program COPY NEWLINE
     | /* vazio, sem produção */
     ;
ident_or_ref : IDENTIFIER
             | REF_VAR_ATRIBUTE
             ;

/* is_in : IS | IN MUDAR ISSO NO DIAGRAMA
      ; */

value_ident_ref : value 
                /* | IDENTIFIER  */
                | REF_VAR_ATRIBUTE
                ;

radiocheckcondition: ident_or_ref IN ident_or_ref manyconditions; 
                    | ident_or_ref IS value_ident_ref manyconditions
                  ;

manyconditions:  LOGICAL ident_or_ref IN ident_or_ref manyconditions
                | LOGICAL ident_or_ref IS value_ident_ref manyconditions
                | THEN
                ;


call : CALL callsetup COPY NEWLINE
     ;

callsetup: IDENTIFIER NEED VAR_TYPE IDENTIFIER 
          | IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers
       ;

%%

