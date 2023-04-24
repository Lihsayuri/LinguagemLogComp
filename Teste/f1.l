%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() 
%}


%%
[a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][0-9a-zA-Z_]*[a-zA-Z][a-zA-Z0-9_]*|[a-zA-Z_]*[a-zA-Z][a-zA-Z0-9_]* SAVE_TOKEN; return IDENTIFIER;
[0-9]+ SAVE_TOKEN; return INT;
[0-9]+.[0-9]* SAVE_TOKEN; return FLOAT;
"driver"|"driver_engineer"|"team"|"grand_prix"|"expected_sc"|"rain_probability"|"drs_usage"|"aggressive_overtaking"|"conservative_overtaking"|"sets_of_tyres"|"lap"|"tyre" return VAR_TYPE;
"type"| "status"|"availability"|"sector"|"start_lap"|"end_lap" return ATRIBUTE;
"EngineOn" return LOOP_ON;
"EngineOff" return LOOP_OFF;
"SetUp" return SETUP;
"Radio_on" return RADIO_ON;
"Radio_off" return RADIO_OFF;
"radio_check" return RADIO_CHECK;
"no_response >>" return SILENCE;
"-Copy!" return COPY;
"call" return CALL;
"in" return IN;
"and"|"or" return LOGICAL;
"then >>" return THEN;
"need" return NEED;
"+"|"-"|">="|"<="|">"|"<" return OPERATOR;
"soft"|"hard"|"medium" return TYRE_TYPE;
"fresh"|"lil_used"|"too_used" return TYRE_STATUS;
"sector1"|"sector2"|"sector3" return SECTOR;
"True"|"False" return BOOLEAN;
"ITS LIGHTS OUT AND AWAY WE GO" return BEGIN_PROGRAM;
"CHECKERED FLAG" return END_PROGRAM;
"\n" return NEWLINE;
"{" return OPEN_BRACES;
"}" return CLOSE_BRACES;
"(" return OPEN_PARENTHESIS;
")" return CLOSE_PARENTHESIS;
"[" return OPEN_BRACKETS;
"]" return CLOSE_BRACKETS;
"," return COMMA;
"of." return OF;
"is" return IS;
printf("Unknown token!n"); yyterminate();

%%
