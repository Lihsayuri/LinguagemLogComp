ITS LIGHTS OUT AND AWAY WE GO

driver piloto1 Leclerc
driver_engineer engenheiro_piloto1 Martin Whitmarsh
team time_piloto1 Ferrari
grand_prix corrida Bahrain
expected_sc SC False
rain_probability chance_chuva 0.2
drs_usage uso_drs (sector1, 3)
aggressive_overtaking agressivo (31,50)
conservative_overtaking conservador (1,28)
setsOfTyres conjunto {{soft, fresh}, {medium, fresh}, {hard, fresh}, {medium, used}}
lap voltas 0
tyres pneu_atual {soft, fresh}


SetUp Pitstop need tyres pneu, driver piloto
Radio_on
radio_check typeof.pneu is soft then >> typeof.pneu is medium and statusof.pneu is used -Copy!
radio_check typeof.pneu is medium and statusof.pneu is used then >> typeof.pneu is hard and statusof.pneu is fresh -Copy!
radio_check typeof.pneu is hard then >> typeof.pneu is medium and statusof.pneu is fresh -Copy!
Radio_off


SetUp expectedRain need rain_probability chance_of_rain, conservative_overtaking coservador
Radio_on
radio_check chance_of_rain is 0.2 then >> conservador is (1,20) -Copy!
no_responde >> conservador is (1,30) -Copy!
Radio_off

SetUp use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo
Radio_on
radio_check uso_drs > 0 and voltas in agressivo then >> availabilityof.uso_drs is availabilityof.uso_drs-1
Radio_off

EngineOn[voltas]
radio_check voltas is 10 then >> call Pitstop need tyres pneu_atual, driver piloto1 -Copy!
radio_check voltas is 16 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
radio_check voltas is 21 then >> call Pitstop need tyres pneu_atual, driver piloto1 -Copy!
radio_check voltas is 41 then >> call Pitstop need tyres pneu_atual, driver piloto1 -Copy!
radio_check voltas is 42 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
radio_check voltas is 45 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
EngineOff


CHECKERED FLAG



-----------------------------------------------------------------------------------------------------------------


-- ID      ::= (letter | "_") , { letter | digit | "_" } ;
-- STRING  ::= '"' , { any_character - '"' } , '"' ;
-- NUM     ::= [ "-" ] , integer , [ "." , integer ] ;
-- letter = "A" | "B" | "C" | ... | "X" | "Y" | "Z" | "a" | "b" | "c" | ... | "x" | "y" | "z" ;
-- digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
-- any_character = letter | digit | "_" | "-" | "." | ":" | "+" | "*" | "/" | "=" | "<" | ">" | "!" | "?" ;
-- integer = digit, { digit } ;


-- <start>            ::= "ITS LIGHTS OUT AND AWAY WE GO" <driver_stmt> <engineer_stmt> <team_stmt> <gp_stmt> <expected_sc_stmt> <rain_prob_stmt> <drs_usage_stmt> <aggressive_overtaking_stmt> <conservative_overtaking_stmt> <sets_of_tyres_stmt> <lap_stmt> <tyres_stmt> <setup_stmt>* <engine_stmt> <checkred_flag_stmt>
-- <driver_stmt>      ::= "driver" ID ID
-- <engineer_stmt>    ::= "driver_engineer" ID ID
-- <team_stmt>        ::= "team" ID ID
-- <gp_stmt>          ::= "grand_prix" ID ID
-- <expected_sc_stmt> ::= "expected_sc" ID BOOL
-- <rain_prob_stmt>   ::= "rain_probability" ID "=" FLOAT
-- <drs_usage_stmt>   ::= "drs_usage" ID "(" STRING "," NUM ")" 
-- <aggressive_overtaking_stmt> ::= "aggressive_overtaking" ID "(" NUM "," NUM ")"
-- <conservative_overtaking_stmt> ::= "conservative_overtaking" ID "(" NUM "," NUM ")"
-- <sets_of_tyres_stmt> ::= "setsOfTyres" ID "{" "{" STRING "," STRING "}" "," "{" STRING "," STRING "}" "," "{" STRING "," STRING "}" "," "{" STRING "," STRING "}" "}"
-- <lap_stmt>         ::= "lap" ID "is" NUM
-- <tyres_stmt>       ::= "tyres" ID "{" STRING "," STRING "}"
-- <setup_stmt>       ::= "setup" ID "need" ID ID "," ID ID <radio_on_stmt> <radio_check_stmt>+ <radio_off_stmt>
-- <radio_on_stmt>    ::= "Radio_on"
-- <radio_off_stmt>   ::= "Radio_off"
-- <radio_check_stmt> ::= "radio_check" ID "is" (NUM | STRING) "then" ">>" ID "is" (NUM | STRING) ( "and" ID "is" (NUM | STRING))? | "no_responde" ">>" ID "is" (NUM | STRING)
-- <engine_stmt>      ::= "EngineOn" "[" ID "]" <radio_check_stmt>*
-- <checkred_flag_stmt> ::= "CHECKRED FLAG"



LETTER = (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)

NUMBER = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

SECTOR = ("sector1" | "sector2" | "sector3")

TYRE_TYPE = ("soft" | "medium" | "hard" | "intermediate" | "wet")

TYRE_STATUS = ("fresh" | "lil_used" | "too_used")

VAR_TYPE = ("driver" | "driver_engineer" | "team" | "grand_prix" | "expected_sc" | "rain_probability" | "drs_usage" | 
"aggressive_overtaking" | "conservative_overtaking" | "sets_of_tyres" | "lap" | "tyre")

ATRIBUTE = ("type" | "status" | "availability" | "sector"| "start_lap"| "end_lap" )



VALUE = STRING | INT | FLOAT | BOOLEAN | TUPLE_INT | TUPLE_DRS | TYRE | TYRE_SET | OPERACAO

STRING = {LETTER}

INT = {NUMBER}+

FLOAT = INT, ".", INT

BOOLEAN = ("True" | "False")

TUPLE_INT = "(", INT, ",", INT, ")"

TUPLE_DRS = "(", SECTOR, {",",SECTOR}, ",", INT, ")"

TYRE = "{", TYRE_TYPE, ",", TYRE_STATUS, "}"

TYRE_SET = "{", TYRE, {",", TYRE}, "}"

IDENTIFIER = (LETTER| "_") , {LETTER | "_" | NUMBER}

REF_VAR_ATRIBUTE = ATRIBUTE, "of.", IDENTIFIER

OPERACAO = (INT | IDENTIFIER), {("+" | "-" | "<" | ">"), (INT | IDENTIFIER)}

STRUCTURE = "ITS LIGHTS OUT AND AWAY WE GO", PROGRAM , "CHECKERED FLAG"
 


PROGRAM = {VAR_TYPE, IDENTIFIER, VALUE, "\n" | "EngineOn", RaceLoop, PROGRAM, "EngineOff", "\n"| "SetUp", SetUpFunction, PROGRAM, "Radio_off", "\n"| "radio_check", radiocheckCondition, PROGRAM, "-Copy!", "\n" ,  ["no_response >>", PROGRAM, "-Copy!", "\n"] |
"call", callSetUp, "-Copy!","\n"}

RaceLoop = "[", INT, "]"

SetUpFunction = IDENTIFIER, "need", VAR_TYPE, IDENTIFIER, {",", VAR_TYPE, IDENTIFIER}, "\n", "Radio_on"

radiocheckCondition = (IDENTIFIER | REF_VAR_ATRIBUTE), ("is"| "in") , (VALUE | IDENTIFIER | REF_VAR_ATRIBUTE), {("and" | "or"), (IDENTIFIER | REF_VAR_ATRIBUTE), ("is"| "in") , (VALUE | IDENTIFIER | REF_VAR_ATRIBUTE)}, "then >>"

callSetUp = IDENTIFIER, "need", VAR_TYPE, IDENTIFIER, {",", VAR_TYPE, IDENTIFIER}