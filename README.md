# Linguagem de Fórmula 1 - f1Strategy <img src="https://img.shields.io/static/v1?label=ConceitoA&message=Finalizado&color=success&style=flat-square&logo=ghost"/>


## Created by :raising_hand_woman:

- Lívia Sayuri Makuta.

## Project Goals :round_pushpin: :

- 27/Mar/2023: Structured language according to EBNF - Task #1 on the list. Structure the language according to the EBNF standard.  :heavy_check_mark:
- 08/Mai/2023: Lexical and Syntax Analysis (without semantic analysis and compilation) - Task #2 on the list. Use tools like Flex and Bison (or similar) to perform the Lexical and Syntax Analysis steps. :heavy_check_mark:


## First Task

The first task of the project is to develop ideas for the language that will be refined based on EBNF.

In this sense, I thought about developing a Formula 1 language that aims to build the race strategy of a driver or team. Additionally, to make it more fun, the final objective of the program is to return a possible radio conversation based on the strategy created by the user programmer.

Therefore, there are some limitations imposed mainly due to the context. For example, a list cannot be constructed—since this type of variable doesn't exist. However, there are variables specifically defined for the context, such as `tyre` and `sets_of_tyres`.

## Second task

The second task of the project is to use tools to perform lexical and syntax analysis. In this case, with Flex, I returned all the tokens of the language, and with Bison, I ordered them. Additionally, we have some changes:

It is possible to create a program using only the end markers of the blocks. For example:

``` txt
ITS LIGHTS OUT AND AWAY WE GO
Radio_off
EngineOff
CHECKRED FLAG
```

This indicates that everything is off and that no strategy has been defined.

**Note:** Before submitting stage 2, I switched everything to rply; both versions are the same, but from the next stage on, I will only use Rply. This submission is in the `RplyVersion` folder.

## Third task

For the third task—specifically for Concept B—I implemented the language compiler in Python based on what we learned from the compiler developed in the course. The language underwent significant changes:

- There are now only 3 types of variables: lap (INT), driver (String), tyre ({type of tyre, status of tyre}).
- The goal is to create tyre change strategies for a race. For this, we have conditions that can be executed with `radio_check`, and we have `Setups` that can be constructed and called during specific laps of the race.
- We have operations like +, -, >, <, and equality ("equals").
- Additionally, we have the main loop of the race, which is initialized with the starting lap and the final lap.

In the end, the program will amusingly indicate to the programmer in which position their driver finished, considering scenarios such as safety cars and crashes.

**Note**: This submission is in the ConceitoB folder.

An example of a program can be seen below:

- `teste.txt`:
``` 
START
driver piloto1 is 'Leclerc'
tyre pneu_atual is {soft, fresh}
lap voltas is 0
lap total_voltas is 32
SetUp tyre Pitstop need (tyre pneu)
Radio_on
lap voltinha is 10
radio_check pneu equals {soft, fresh} then >> pneu is {medium, fresh} Copy!
no_response >> pneu is {hard, used} Copy!
checked => pneu
Radio_off
EngineOn[voltas, total_voltas]
radio_check voltas equals 10 then >> pneu_atual is call Pitstop need(pneu_atual) Copy!
radio_check voltas + 2 > 30 then >> pneu_atual is call Pitstop need(pneu_atual) Copy!
EngineOff
FINISH
```

- The output for the previous input: 

```
AS LUZES SE APAGAM E LÁ VAMOS NÓS!
Engenheiro : Radio check para o piloto  Leclerc
Engenheiro : Definindo pneu do tipo:  soft e no estado  fresh para o piloto
Engenheiro : Lap check para o piloto  0
Engenheiro : Lap check para o piloto  32
James : Alô piloto! Vamos começar a corrida! Temos que fazer  32  voltas!
Engenheiro : Boa sorte! Estratégia de pneus já definida!
Equipe : 3, 2, 1, GO!
James : Continuamos na volta  0  . Tenha paciência!
James : Alô! Estamos na volta  1  . Segura a posição!
James : Alô! Estamos na volta  2  . Segura a posição!
James : Alô! Estamos na volta  3  . Segura a posição!
James : Alô! Estamos na volta  4  . Segura a posição!
James : Alô! Estamos na volta  5  . Segura a posição!
James : Alô! Estamos na volta  6  . Segura a posição!
James : Alô! Estamos na volta  7  . Segura a posição!
James : Alô! Estamos na volta  8  . Segura a posição!
James : Alô! Estamos na volta  9  . Segura a posição!
James : Alô! Estamos na volta  10  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  Pitstop ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
Binotto : Estratégia A é o foco! Trocando o pneu para o tipo medium e no estado fresh na troca de número 1
James : Alô! Estamos na volta  11  . Segura a posição!
James : Alô! Estamos na volta  12  . Segura a posição!
James : Alô! Estamos na volta  13  . Segura a posição!
James : Alô! Estamos na volta  14  . Segura a posição!
James : Alô! Estamos na volta  15  . Segura a posição!
James : Alô! Estamos na volta  16  . Segura a posição!
James : Alô! Estamos na volta  17  . Segura a posição!
James : Alô! Estamos na volta  18  . Segura a posição!
James : Alô! Estamos na volta  19  . Segura a posição!
James : Alô! Estamos na volta  20  . Segura a posição!
James : Alô! Estamos na volta  21  . Segura a posição!
James : Alô! Estamos na volta  22  . Segura a posição!
James : Alô! Estamos na volta  23  . Segura a posição!
James : Alô! Estamos na volta  24  . Segura a posição!
James : Alô! Estamos na volta  25  . Segura a posição!
James : Alô! Estamos na volta  26  . Segura a posição!
James : Alô! Estamos na volta  27  . Segura a posição!
James : Alô! Estamos na volta  28  . Segura a posição!
James : Alô! Estamos na volta  29  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  Pitstop ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Negativo!
Binotto : Estratégia A é o foco! Trocando o pneu para o tipo hard e no estado used na troca de número 2
James : Alô! Estamos na volta  30  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  Pitstop ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Negativo!
James : Pneu  hard  no estado  used  continua na pista!
James : Alô! Estamos na volta  31  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  Pitstop ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Negativo!
James : Pneu  hard  no estado  used  continua na pista!
[CHECKRED FLAG]
Binotto : Corrida finalizada
[Som da Opera Carmem de Georges Bizet ao fundo e champagne sendo aberto]
James : YESSSSS!!! P1 ! P1 ! Somamos  25  pontos! Parabéns!
Binotto : Ainda ganhamos o ponto extra da volta mais rápida! Parabéns!
Equipe : Você foi incrível! Rumo ao título!
Piloto : É isso equipe! Vamos para a próxima!
```

- Another input - `teste2.txt`:

```
START
driver piloto1 is 'Hamilton'
tyre pneu_atual is {soft, fresh}
lap voltas is 0
lap total_voltas is 22
SetUp driver PitDriver need (driver piloto)
Radio_on
radio_check piloto equals 'Hamilton' then >> piloto is 'Verstappen' Copy!
checked => piloto
Radio_off
SetUp tyre PitStop need (tyre pneu)
Radio_on
radio_check pneu equals {soft, fresh} then >> pneu is {medium, used} Copy!
checked => pneu
Radio_off
EngineOn[voltas, total_voltas]
radio_check voltas equals 10 then >> piloto1 is call PitDriver need(piloto1) Copy!
radio_check voltas + 2 > 20 then >> pneu_atual is call PitStop need(pneu_atual) Copy!
EngineOff
FINISH
```

- Output of `teste2.txt`:

```
AS LUZES SE APAGAM E LÁ VAMOS NÓS!
Engenheiro : Radio check para o piloto  Hamilton
Engenheiro : Definindo pneu do tipo:  soft e no estado  fresh para o piloto
Engenheiro : Lap check para o piloto  0
Engenheiro : Lap check para o piloto  22
James : Alô piloto! Vamos começar a corrida! Temos que fazer  22  voltas!
Engenheiro : Boa sorte! Estratégia de pneus já definida!
Equipe : 3, 2, 1, GO!
James : Continuamos na volta  0  . Tenha paciência!
James : Alô! Estamos na volta  1  . Segura a posição!
James : Alô! Estamos na volta  2  . Segura a posição!
James : Alô! Estamos na volta  3  . Segura a posição!
James : Alô! Estamos na volta  4  . Segura a posição!
James : Alô! Estamos na volta  5  . Segura a posição!
James : Alô! Estamos na volta  6  . Segura a posição!
James : Alô! Estamos na volta  7  . Segura a posição!
James : Alô! Estamos na volta  8  . Segura a posição!
James : Alô! Estamos na volta  9  . Segura a posição!
James : Alô! Estamos na volta  10  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  PitDriver ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Câmbio, aqui é o James! Trocando  piloto1  para Verstappen
James : Alô! Estamos na volta  11  . Segura a posição!
James : Alô! Estamos na volta  12  . Segura a posição!
James : Alô! Estamos na volta  13  . Segura a posição!
James : Alô! Estamos na volta  14  . Segura a posição!
James : Alô! Estamos na volta  15  . Segura a posição!
James : Alô! Estamos na volta  16  . Segura a posição!
James : Alô! Estamos na volta  17  . Segura a posição!
James : Alô! Estamos na volta  18  . Segura a posição!
James : Alô! Estamos na volta  19  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  PitStop ,  para você! Box box box!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
Binotto : Estratégia A é o foco! Trocando o pneu para o tipo medium e no estado used na troca de número 1
James : Alô! Estamos na volta  20  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  PitStop ,  para você! Box box box!
James : Pneu  medium  no estado  used  continua na pista!
James : Alô! Estamos na volta  21  . Segura a posição!
Engenheiro: Radio check para o piloto. Checagem feita. Positivo!
James : Piloto, na escuta? Temos um Setup novo, o  PitStop ,  para você! Box box box!
James : Pneu  medium  no estado  used  continua na pista!
[CHECKRED FLAG]
Binotto : Corrida finalizada
James : Alô piloto! Infelizmente não pontuamos hoje. Você bateu na volta  21  e isso custou a corrida. Espero que esteja tudo bem com você!
Equipe : Não foi dessa vez! Terminamos em  13 . Vamos para a próxima!
Piloto : É isso equipe! Vamos para a próxima!
```

- Finally, one more input from the third example `teste3.txt`:

```
START
lap volta is 12
lap volta_grande is 2 > 3
driver piloto1 is 'Hamilton'
FINISH
```

- Output of `teste3.txt`:
```
AS LUZES SE APAGAM E LÁ VAMOS NÓS!
Engenheiro : Lap check para o piloto  12
Engenheiro : Lap check para o piloto  0
Engenheiro : Radio check para o piloto  Hamilton
```

## EBNF of the language

``` lua
LETTER = (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)

NUMBER = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

TYRE_TYPE = ("soft" | "medium" | "hard" )

TYRE_STATUS = ("fresh" | "used" )

VAR_TYPE = ("driver" | "lap" | "tyre")

VALUE = STRING | INT | TYRE | OPERACAO

STRING = {LETTER}

INT = {NUMBER}+

TYRE = "{", TYRE_TYPE, ",", TYRE_STATUS, "}"

IDENTIFIER = (LETTER| "_") , {LETTER | "_" | NUMBER}

OPERACAO = (INT | IDENTIFIER), {("+" | "-" | "<" | ">", "equals" ), (INT | IDENTIFIER)}

STRUCTURE = "START", PROGRAM , "FINISH"
 
PROGRAM = {VAR_TYPE, IDENTIFIER, "is",  VALUE, "\n" | "EngineOn", RaceLoop, PROGRAM, "EngineOff", "\n"| "SetUp", SetUpFunction, PROGRAM, "Radio_off", "\n"| "radio_check", radiocheckCondition, PROGRAM, "Copy!", "\n" ,  ["no_response >>", PROGRAM, "Copy!", "\n"] |
"call", callSetUp, "\n"}

RaceLoop = "[", INT, ",", INT, "]"

SetUpFunction = VAR_TYPE, IDENTIFIER,  "need", "(", VAR_TYPE, IDENTIFIER, {",", VAR_TYPE, IDENTIFIER} , ")", "\n", "Radio_on"

radiocheckCondition = IDENTIFIER , ("equals"| ">"| "<") , (VALUE | IDENTIFIER ), "then >>"

callSetUp = IDENTIFIER, "need", "(", IDENTIFIER, {",",  IDENTIFIER}, ")"

```

## Syntax Diagram of the language [updated to version of task 3]

<img src="diagrama_sintatico.drawio.png" width="800" height="600">



