%{
#include <stdio.h>
#include <stdlib.h>
#include "f1.tab.h"
extern int yywrap();
int is_identified = 0;
%}

%{
#define YYEOF 0
%}

NUMBER [0-9]
LETTER [a-zA-Z]
VAR_TYPE driver|driver_engineer|team|grand_prix|expected_sc|rain_probability|drs_usage|aggressive_overtaking|conservative_overtaking|sets_of_tyres|lap|tyre
ATRIBUTE type|status|availability|sector|start_lap|end_lap
LOOP_ON EngineOn
LOOP_OFF EngineOff
SETUP SetUp
RADIO_ON Radio_on
RADIO_OFF Radio_off
RADIO_CHECK radio_check
SILENCE "no_response >>"
COPY -Copy!
CALL call
IN in
LOGICAL and|or
THEN "then >>"
NEED need
ID  [a-zA-Z_][a-zA-Z0-9_]*
OPERATOR "+"|"-"|">="|"<="|">"|"<"
TYRE_TYPE soft|hard|medium
TYRE_STATUS fresh|lil_used|too_used
SECTOR sector1|sector2|sector3
BOOLEAN True|False 
BEGIN_PROGRAM "ITS LIGHTS OUT AND AWAY WE GO"
END_PROGRAM "CHECKRED FLAG"

%%

"\n"                    { return NEWLINE; }
{BEGIN_PROGRAM}         { printf("BEGIN_PROGRAM: %s \n", yytext); return BEGIN_PROGRAM; }
{END_PROGRAM}           { printf("END_PROGRAM: %s \n", yytext); return END_PROGRAM; }
{ATRIBUTE}"of."{ID}     { printf("REF_VAR_ATRIBUTE: %s\n", yytext); return REF_VAR_ATRIBUTE; }
{VAR_TYPE}              { printf("VAR_TYPE: %s\n", yytext); return VAR_TYPE; }
{LOOP_ON}               { printf("LOOP_ON: %s\n", yytext); return LOOP_ON; }
{LOOP_OFF}              { printf("LOOP_OFF: %s\n", yytext); return LOOP_OFF; }
{SETUP}                 { printf("SETUP: %s\n", yytext); return SETUP; }
{RADIO_ON}              { printf("RADIO_ON: %s\n", yytext); return RADIO_ON; }
{RADIO_OFF}             { printf("RADIO_OFF: %s\n", yytext); return RADIO_OFF; }
{RADIO_CHECK}           { printf("RADIO_CHECK: %s\n", yytext); return RADIO_CHECK; }
{SILENCE}               { printf("SILENCE: %s\n", yytext); return SILENCE; }
{COPY}                  { printf("COPY: %s\n", yytext); return COPY; }
{CALL}                  { printf("CALL: %s\n", yytext); return CALL; }
{IN}                    { printf("IN: %s\n", yytext); return IN; }
{LOGICAL}               { printf("LOGICAL: %s\n", yytext); return LOGICAL; }
{THEN}                  { printf("THEN: %s\n", yytext); return THEN; }
{NEED}                  { printf("NEED: %s\n", yytext); return NEED; }
{BOOLEAN}               { printf("BOOLEAN: %s\n", yytext); return BOOLEAN; }
{OPERATOR}              { printf("OPERATOR: %s \n", yytext); return OPERATOR; }
{SECTOR}                { printf("SECTOR: %s \n", yytext); return SECTOR; }
{TYRE_TYPE}             { printf("TYRE_TYPE: %s \n", yytext); return TYRE_TYPE; }
{TYRE_STATUS}           { printf("TYRE_STATUS: %s \n", yytext); return TYRE_STATUS; }
","                     { printf("COMMA: %s \n", yytext); return COMMA; }
"("                     { printf("OPEN_PARENTHESIS: %s \n", yytext); return OPEN_PARENTHESIS; }
")"                     { printf("CLOSE_PARENTHESIS: %s \n", yytext); return CLOSE_PARENTHESIS; }
"{"                     { printf("OPEN_BRACES: %s \n", yytext); return OPEN_BRACES; }
"}"                     { printf("CLOSE_BRACES: %s \n", yytext); return CLOSE_BRACES; }
"["                     { printf("OPEN_BRACKETS: %s \n", yytext); return OPEN_BRACKETS; }
"]"                     { printf("CLOSE_BRACKETS: %s \n", yytext); return CLOSE_BRACKETS; }


"is"                    { printf("IS: %s\n", yytext);  return IS; }  
\'([^\\\n]|(\\.))*\'    { printf("STRING: %s\n", yytext); return STRING; }
{ID}                    { printf("IDENTIFIER: %s\n", yytext);  return IDENTIFIER;  }
{NUMBER}+               { printf("INT: %s \n", yytext); return INT; }
{NUMBER}+[.]{NUMBER}+   { printf("FLOAT: %s \n", yytext); return FLOAT; }

[ \t]                   { /* ignora */ }

.                      { printf("ERRO: %s \n", yytext); return 404; }


%%

int yywrap() {
    return 1;
}

/* int main() {
    int token;
    while ((token = yylex())) {
        /* printf("Token encontrado: %d\n", token);  */
        /* não faz nada */
    /* }
    return 0; 
}   */ 

