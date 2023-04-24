%{
#include "node.h"
NBlock *programBlock; /* the top level root node of our final AST */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
extern int yylex();
void yyerror(const char *s) { printf("ERROR: %sn", s); }

%}


/* Represents the many different ways we can access our data */
%union {
    Node *node;
    Structure *structure;
    Program *program;
    VarDefinition *vardef;
    RaceLoop *raceloop;
    SetUpFunction *setup;
    RadioCheckCondition *radiocheck;
    callSetUp *callsetup;
    Value *value;
    Identifier *identifier;
    std::string *string;
    int token;
}


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
%start beginning

%%

tuple_int: OPEN_PARENTHESIS INT COMMA INT CLOSE_PARENTHESIS {new TupleInt(*$2, *$4)};



tuple_drs:  OPEN_PARENTHESIS SECTOR COMMA INT CLOSE_PARENTHESIS {new TupleDRS(*$2, *$4)}
           | OPEN_PARENTHESIS SECTOR COMMA SECTOR COMMA INT CLOSE_PARENTHESIS {new TupleDRS(*$2, *$4, *$6)}
           | OPEN_PARENTHESIS SECTOR COMMA SECTOR COMMA SECTOR COMMA INT CLOSE_PARENTHESIS {new TupleDRS(*$2, *$4, *$6, *$8)}
           ;

tyre: OPEN_BRACES TYRE_TYPE COMMA TYRE_STATUS CLOSE_BRACES {new Tyre(*$2, *$4)};

tyre_set: OPEN_BRACES tyre CLOSE_BRACES {new TyreSet(*$2)}
        | OPEN_BRACES tyre manytires CLOSE_BRACES { new TyreSet([$2].concat($3)) }
        ;

manytires : COMMA tyre { [$2] }
          | COMMA tyre manytires  { [$2].concat($3) }
          ;

manyidentifiers: COMMA VAR_TYPE IDENTIFIER { [$2, $3] }
                | COMMA VAR_TYPE IDENTIFIER manyidentifiers { [$2, $3].concat($4) }
                ;

termo: INT {new Integer(*$1)}
     | IDENTIFIER {new Identifier(*$1)}
     ;

operacao: termo 
        | operacao OPERATOR termo {new Operation(*$1, *$2, *$3)}
        ;

value: STRING {new String(*$1)}
     /* | INT  consigo pegar o int atraves de operacao - termo - int*/ 
     | FLOAT {new Float(*$1)}
     | BOOLEAN {new Boolean(*$1)}
     | tuple_int 
     | tuple_drs
     | tyre
     | tyre_set
     | operacao
     ;


beginning : BEGIN_PROGRAM NEWLINE program END_PROGRAM {new Structure(*$3)};
            {
                    printf("Seja bem vindo a mais uma corrida de fórmula 1!\n");
            }
           ;

program : var_declaration program {new Program($1, nullptr, nullptr, nullptr, nullptr);}
         | loop program {new Program(nullptr, $1, nullptr, nullptr, nullptr);}
         | setup program  {new Program(nullptr, nullptr, $1, nullptr, nullptr);}
         | radiocheck program {new Program(nullptr, nullptr, nullptr, $1, nullptr);}
         | call program {new Program(nullptr, nullptr, nullptr, nullptr, $1);}
         | /* vazio, sem produção */
         ;

var_declaration: VAR_TYPE IDENTIFIER IS value NEWLINE {new VarDefinition($1, $2, $4); printf("Característica setada! O %s está setado!", $1);}
     ;

loop: LOOP_ON race_loop program LOOP_OFF NEWLINE {new RaceLoop($2, $3); }
     ;

race_loop: OPEN_BRACKETS INT CLOSE_BRACKETS {new Integer($2); }
         ;

setup: SETUP setupfunction RADIO_OFF NEWLINE  
     ;

setupfunction: IDENTIFIER NEED VAR_TYPE IDENTIFIER  NEWLINE RADIO_ON program {new SetUpFunction($1, new FunctionVarDefinition($3, $4), $7) ;}
               | IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers NEWLINE RADIO_ON program {new SetUpFunction($1, [new FunctionVarDefinition($3, $4), $5], $9) ;}
       ;


radiocheck: RADIO_CHECK radiocheckcondition program COPY NEWLINE else {new RadioCheckCondition($2, $3, $5) ;}
           ;
         ;

radiocheckcondition: ident_or_ref IN ident_or_ref manyconditions; 
                    | ident_or_ref IS value_ident_ref manyconditions
                  ;

manyconditions:  LOGICAL ident_or_ref IN ident_or_ref manyconditions
                | LOGICAL ident_or_ref IS value_ident_ref manyconditions
                | THEN
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




call : CALL callsetup COPY NEWLINE
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

