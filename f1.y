%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lex.yy.h"
%}

%token<name> IDENTIFIER
%token<value> IS
%token<value> STRING
%token<value> INT
%token<value> FLOAT
%token<value> BOOLEAN
%token<value> TUPLE_INT
%token<value> TUPLE_DRS
%token<value> TYRE
%token<value> TYRE_SET
%token<value> VAR_TYPE
%token<sector> SECTOR
%token<tyre_type> TYRE_TYPE
%token<tyre_status> TYRE_STATUS
%token<value> ATRIBUTE
%token<operation> PLUS MINUS LESS GREATER LESS_EQUAL GREATER_EQUAL
%token STRUCTURE ENGINE_ON RACE_LOOP ENGINE_OFF SET_UP RADIO_OFF RADIO_ON RADIO_CHECK REF_VAR_ATRIBUTE CALL THEN ELSE IN NEED COMMA

%left OR
%left AND
%nonassoc NOT
%nonassoc LOWER_THAN_ELSE
%nonassoc ELSE

%%
program : STRUCTURE
        | program statement STRUCTURE
        ;

statement : variable_declaration
          | engine_on
          | race_loop
          | engine_off
          | set_up
          | radio_off
          | radio_check
          | call_set_up
          ;

variable_declaration : VAR_TYPE IDENTIFIER IS value
                      ;

engine_on : ENGINE_ON
          ;

race_loop : RACE_LOOP
          ;

engine_off : ENGINE_OFF
           ;

set_up : SET_UP IDENTIFIER NEED VAR_TYPE IDENTIFIER set_up_parameters RADIO_ON
       ;

set_up_parameters : /* empty */
                   | COMMA VAR_TYPE IDENTIFIER set_up_parameters
                   ;

radio_off : RADIO_OFF
          ;

radio_check : radio_check_condition THEN
            | radio_check_condition THEN program ELSE program
            | radio_check_condition THEN program LOWER_THAN_ELSE program
            ;

radio_check_condition : IDENTIFIER IS value
                      | REF_VAR_ATRIBUTE IS value
                      | IDENTIFIER IN IDENTIFIER
                      | REF_VAR_ATRIBUTE IN IDENTIFIER
                      | radio_check_condition AND radio_check_condition
                      | radio_check_condition OR radio_check_condition
                      | NOT radio_check_condition
                      ;

call_set_up : CALL IDENTIFIER NEED VAR_TYPE IDENTIFIER call_set_up_parameters
            ;

call_set_up_parameters : /* empty */
                        | COMMA VAR_TYPE IDENTIFIER call_set_up_parameters
                        ;

value : STRING
      | INT
      | FLOAT
      | BOOLEAN
      | TUPLE_INT
      | TUPLE_DRS
      | TYRE
      | TYRE_SET
      | operation
      ;

operation : INT op INT
          | IDENTIFIER op IDENTIFIER
          ;

op : PLUS
   | MINUS
   | LESS
   | GREATER
   | LESS_EQUAL
   | GREATER_EQUAL
   ;

%%

int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s input_file\n", argv[0]);
    exit(1);
  }

  FILE *input_file = fopen(argv[1], "r");
  if (!input_file) {
    perror("fopen");
    exit(1);
  }

  yyin = input_file;
  yyparse();

  return 0;
}

void yyerror(const char *s) {
  printf("Error: %s\n", s   );
}
