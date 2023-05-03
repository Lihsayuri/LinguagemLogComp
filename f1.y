%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void yyerror(char *s);
int yylex(void);
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

%start beggining

%%

tuple_int: OPEN_PARENTHESIS INT COMMA INT CLOSE_PARENTHESIS ;

manysector: COMMA SECTOR
          | manysector COMMA SECTOR
          ;

tuple_drs:  OPEN_PARENTHESIS SECTOR COMMA INT CLOSE_PARENTHESIS 
           | OPEN_PARENTHESIS SECTOR manysector COMMA INT CLOSE_PARENTHESIS 
           ;

tyre: OPEN_BRACES TYRE_TYPE COMMA TYRE_STATUS CLOSE_BRACES ;
tyre_set: OPEN_BRACES tyre CLOSE_BRACES {printf("Regra tyre_set foi processada! 1 tyre\n");}
        | OPEN_BRACES tyre manytires CLOSE_BRACES {printf("Regra tyre_set foi processada! many tyres\n");}
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
     | TYRE_STATUS
     | TYRE_TYPE
     ;


beggining: BEGIN_PROGRAM NEWLINE structure {printf("Regra beggining foi processada!\n");}

structure: END_PROGRAM  
           | program structure {printf("Regra structure foi processada!\n");}
           ;

program :  var_declaration {printf("Regra var_declaration foi processada!\n");}
         | loop  {printf("Regra loop foi processada!\n");}
         | setup       {printf("Regra setup foi processada!\n");}
         | radiocheck  {printf("Regra radiocheck foi processada!\n");}
         | call  {printf("Regra call foi processada!\n");} 
         | LOOP_OFF NEWLINE {printf("Regra loop off processada!\n");}
         | RADIO_OFF NEWLINE {printf("Processei tudo no Setup");}
         ;




var_declaration: VAR_TYPE IDENTIFIER IS value NEWLINE {printf("Característica setada! \n");}
     ;

loop: LOOP_ON race_loop 
     ;

race_loop: OPEN_BRACKETS INT CLOSE_BRACKETS NEWLINE {printf("Definido o número de voltas!\n");}
           | OPEN_BRACKETS IDENTIFIER CLOSE_BRACKETS NEWLINE {printf("Definido o número de voltas com identifier!\n");}
         ;

setup: SETUP setupfunction ;

setupfunction: IDENTIFIER NEED VAR_TYPE IDENTIFIER  NEWLINE RADIO_ON NEWLINE
               | IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers NEWLINE RADIO_ON NEWLINE
       ;


ident_or_ref : IDENTIFIER
             | REF_VAR_ATRIBUTE
             ;

value_ident_ref : value 
                /* | IDENTIFIER  */
                | REF_VAR_ATRIBUTE
                ;

radiocheck: RADIO_CHECK radiocheckcondition var_declaration COPY NEWLINE else {printf("Regra radiocheck processada!\n");}
            | RADIO_CHECK radiocheckcondition call COPY NEWLINE else {printf("Regra radiocheck processada! ENTREI NO REF MANO\n");}
            | RADIO_CHECK radiocheckcondition radiocheckcondition COPY NEWLINE else {printf("Regra radiocheck processada! ENTREI NO REF MANO\n");}
         ;

else: SILENCE radiocheckcondition COPY NEWLINE {printf("Regra else processada! ENTREI NO REF MANO\n");}
     | {printf ("Não tem else");}/* vazio, sem produção */
     ;

radiocheckcondition: ident_or_ref IN ident_or_ref manyconditions; 
                    | ident_or_ref IS value_ident_ref manyconditions
                    | ident_or_ref OPERATOR value_ident_ref manyconditions
                    | ident_or_ref IS ident_or_ref OPERATOR value_ident_ref manyconditions 
                  ;

manyconditions:  LOGICAL ident_or_ref IN ident_or_ref manyconditions
                | LOGICAL ident_or_ref IS value_ident_ref manyconditions
                | LOGICAL ident_or_ref OPERATOR value_ident_ref manyconditions
                | THEN
                | {printf("Não tem manyconditions");}/* vazio, sem produção */
                ;


call : CALL callsetup 
     ;

callsetup: IDENTIFIER NEED VAR_TYPE IDENTIFIER 
          | IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers
       ;

%%


yyerror(char *s)
{
  printf("Erro: %s\n", s);
}

int main(void)
{
  yyparse();
  return 0;
}

