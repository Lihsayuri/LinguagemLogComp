%{
#include <stdio.h>
int is_identified = 0;
%}

%option noyywrap

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
SILENCE no_response
COPY -Copy!
CALL call
IN in
LOGICAL and|or
THEN "then >>"
NEED need
ID  [a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][0-9a-zA-Z_]*[a-zA-Z][a-zA-Z0-9_]*|[a-zA-Z_]*[a-zA-Z][a-zA-Z0-9_]*
OPERATOR "+"|"-"|">="|"<="|">"|"<"
TYRE_TYPE soft|hard|medium
TYRE_STATUS fresh|lil_used|too_used
SECTOR sector1|sector2|sector3
BOOLEAN True|False 
BEGIN_PROGRAM "ITS LIGHTS OUT AND AWAY WE GO"
END_PROGRAM "CHECKERED FLAG"

%option noyywrap


%%

"\n"                    { is_identified = 0; return 1; }
{BEGIN_PROGRAM}         { printf("BEGIN_PROGRAM: %s \n", yytext); return 2; }
{END_PROGRAM}           { printf("END_PROGRAM: %s \n", yytext); return 3; }
{ATRIBUTE}"of."{ID}     { printf("REF_VAR_ATRIBUTE: %s\n", yytext); return 4; }
{VAR_TYPE}              { printf("VAR_TYPE: %s\n", yytext); return 5; }
{LOOP_ON}               { printf("LOOP_ON: %s\n", yytext); return 6; }
{LOOP_OFF}              { printf("LOOP_OFF: %s\n", yytext); return 7; }
{SETUP}                 { printf("SETUP: %s\n", yytext); return 8; }
{RADIO_ON}              { printf("RADIO_ON: %s\n", yytext); return 9; }
{RADIO_OFF}             { printf("RADIO_OFF: %s\n", yytext); return 10; }
{RADIO_CHECK}           { printf("RADIO_CHECK: %s\n", yytext); return 11; }
{SILENCE}               { printf("SILENCE: %s\n", yytext); return 12; }
{COPY}                  { printf("COPY: %s\n", yytext); return 13; }
{CALL}                  { printf("CALL: %s\n", yytext); return 14; }
{IN}                    { printf("IN: %s\n", yytext); return 15; }
{LOGICAL}               { printf("LOGICAL: %s\n", yytext); return 16; }
{THEN}                  { printf("THEN: %s\n", yytext); return 17; }
{NEED}                  { printf("NEED: %s\n", yytext); return 18; }
{BOOLEAN}               { printf("BOOLEAN: %s\n", yytext); return 19; }
{OPERATOR}              { printf("OPERACAO: %s \n", yytext); return 20; }
{SECTOR}                { printf("SECTOR: %s \n", yytext); return 21; }
{TYRE_TYPE}             { printf("TYRE_TYPE: %s \n", yytext); return 22; }
{TYRE_STATUS}           { printf("TYRE_STATUS: %s \n", yytext); return 23; }
","                     { printf("COMMA: %s \n", yytext); return 24; }
"("                     { printf("OPEN_PARENTHESIS: %s \n", yytext); return 25; }
")"                     { printf("CLOSE_PARENTHESIS: %s \n", yytext); return 26; }
"{"                     { printf("OPEN_BRACES: %s \n", yytext); return 27; }
"}"                     { printf("CLOSE_BRACES: %s \n", yytext); return 28; }
"["                     { printf("OPEN_BRACKETS: %s \n", yytext); return 29; }
"]"                     { printf("CLOSE_BRACKETS: %s \n", yytext); return 30; }


"is"                    { is_identified = 1; printf("IS: %s\n", yytext); yymore(); }  
{LETTER}+               { if(is_identified) { printf("STRING: %s\n", yytext); is_identified = 0; return 31; } else { printf("IDENTIFIER: %s\n", yytext); return 32; } }
{ID}                    { { printf("IDENTIFIER: %s\n", yytext);  return 32; } }
{NUMBER}+               { printf("INT: %s \n", yytext); return 33; }
{NUMBER}+[.]{NUMBER}+   { printf("FLOAT: %s \n", yytext); return 34; }

[ \t]                   { /* ignora */ }
.                      { printf("ERRO: %s \n", yytext); return 404; }


%%

int main() {
    int token;
    while ((token = yylex())) {
        /* printf("Token encontrado: %d\n", token); */
        /* não faz nada */
    }
    return 0;
}

