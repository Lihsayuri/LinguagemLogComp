# Linguagem de Fórmula 1 <img src="https://img.shields.io/static/v1?label=Etapa2&message=Finalizado&color=success&style=flat-square&logo=ghost"/>


## Feito por :raising_hand_woman:

- Lívia Sayuri Makuta.

## Objetivos do projeto :round_pushpin: :

- 27/Mar/2023: Linguagem estruturada segundo a EBNF - Tarefa #1 da lista. Estruturar a linguagem segundo o padrão EBNF.  :heavy_check_mark:
- 08/Mai/2023: Análise Léxica e Sintática (sem análise semântica e compilação) - Tarefa #2 da lista. Utilizar as ferramentas Flex e Bison (ou semelhantes) para realizar as etapas de Análise Léxica e Sintática. :heavy_check_mark:


## Primeira tarefa

A primeira tarefa do projeto é desenvolver ideias para a linguagem que ainda vai ser lapidada a partir da EBNF.

Nesse sentido pensei em desenvolver uma linguagem de fórmula1 que busca montar a estratégia de corrida de um piloto ou time de fórmula1.
Além disso, para ficar mais divertido, o objetivo final do programa é retornar uma possível conversa de rádio a partir da estratégia montada pelo usuário programador. 

Sendo assim existem algumas limitações impostas principalmente por conta do contexto, por exemplo, uma lista não pode ser montada - já que esse tipo de variável nem existe. Todavia, existem variáveis definidas propriamente para o contexto, como tyre e sets_of_tyres.

## Segunda tarefa

A segunda tarefa do projeto é utilizar ferramentas para fazer as análises léxicas e sintática. Nesse caso, com o flex retornei todos os Tokens da linguagem e no Bison os ordenei. Além disso, temos algumas mudanças:

É possível fazer um programa somente com as marcações de end dos blocos. Por exemplo:

``` txt
ITS LIGHTS OUT AND AWAY WE GO
Radio_off
EngineOff
CHECKRED FLAG
```

Indicando que tudo está desligado e que nenhuma estratégia foi definida. 

Observação: Troquei tudo para o rply, ambas as versões são iguais, mas a partir da próxima etapa só utilizarei o Rply.

## Terceira tarefa

Para fazer a terceira tarefa - no caso, para o conceito B - implementei o compilador da linguagem em Python com base no que aprendemos com o compilador desenvolvido na disciplina. A linguagem sofreu alterações importantes:

- Agora existem apenas 3 tipos de variáveis: lap (INT), driver (String), tyre ({tipo do pneu, status do pneu})
- O objetivo é criar estratégias de troca de pneu. Para isso temos condições que podem ser feitas com o `radio_check` e temos `Setup`s que podem ser construídos e chamados durantes voltas específicas da corrida.
- Além disso, temos o loop principal da corrida que possui a volta inicial e a volta final.
- Temos operações como +, -, >, < , igualdade.

No final, o programa vai de maneira divertida indicar ao programador em que posição seu piloto terminou, considerando alguns cenários como safety car e batidas.

Um exemplo de programa pode ser visto abaixo:

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


Exemplo de output para o input apresentado: 

```
AS LUZES SE APAGAM E LÁ VAMOS NÓS!
Engenheiro : Radio check para o piloto  Leclerc
Engenheiro : Definindo pneu do tipo:  soft e no estado  fresh para o piloto
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
James : Alô piloto! Bom trabalho! P2 pra você!! Somamos  18  pontos! Parabéns!
Equipe : A corrida de hoje foi incrível! Na próxima vamos para o primeiro lugar!
Piloto : É isso equipe! Vamos para a próxima!
```

## EBNF da linguagem

``` lua
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

OPERACAO = (INT | IDENTIFIER), {("+" | "-" | "<" | ">" | ">=" | "<="), (INT | IDENTIFIER)}

STRUCTURE = "ITS LIGHTS OUT AND AWAY WE GO", PROGRAM , "CHECKERED FLAG"
 


PROGRAM = {VAR_TYPE, IDENTIFIER, "is",  VALUE, "\n" | "EngineOn", RaceLoop, PROGRAM, "EngineOff", "\n"| "SetUp", SetUpFunction, PROGRAM, "Radio_off", "\n"| "radio_check", radiocheckCondition, PROGRAM, "-Copy!", "\n" ,  ["no_response >>", PROGRAM, "-Copy!", "\n"] |
"call", callSetUp, "-Copy!","\n"}

RaceLoop = "[", INT, "]"

SetUpFunction = IDENTIFIER, "need", VAR_TYPE, IDENTIFIER, {",", VAR_TYPE, IDENTIFIER}, "\n", "Radio_on"

radiocheckCondition = (IDENTIFIER | REF_VAR_ATRIBUTE), ("is"| "in") , (VALUE | IDENTIFIER | REF_VAR_ATRIBUTE), {("and" | "or"), (IDENTIFIER | REF_VAR_ATRIBUTE), ("is"| "in") , (VALUE | IDENTIFIER | REF_VAR_ATRIBUTE)}, "then >>"

callSetUp = IDENTIFIER, "need", VAR_TYPE, IDENTIFIER, {",", VAR_TYPE, IDENTIFIER}

```

## Diagrama Sintático da linguagem

<img src="diagrama_sintatico.drawio.png" width="800" height="600">



## Exemplo do uso da linguagem

```lua

ITS LIGHTS OUT AND AWAY WE GO

driver piloto1 is Leclerc
driver_engineer engenheiro_piloto1 is Martin Whitmarsh
team time_piloto1 is Ferrari
grand_prix corrida is Bahrain
expected_sc SC is False
rain_probability chance_chuva is 0.2
drs_usage uso_drs is (sector1, 3)
aggressive_overtaking agressivo is (31,50)
conservative_overtaking conservador is (1,28)
sets_of_tyres conjunto is {{soft, fresh}, {medium, fresh}, {hard, fresh}, {medium, used}}
lap voltas is 0
tyres pneu_atual is {soft, fresh}


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

```

## Flex : análise léxica

Para analisar os tokens que fazem parte do código, foi feito um programa em flex que identifica se o token pertence a linguagem ou não. Esse programa está em `f1.l`. Para compilá-lo e executá-lo basta:

``` bash
flex f1.l
gcc lex.yy.c -o seu_programa -lfl
./seu_programa < teste.txt 
```

## Bison : análise sintática

```bash
bison -d f1.y
gcc -o parser f1.tab.c main.c
./parser < entrada.txt
```

## Linkando tudo

bison -d f1.y
flex f1.l
cc -o f1 f1.tab.c lex.yy.c -lfl -DYYDEBUG
./f1 < teste.txt

## Para rodar o código de exemplo no llvm:

clang++ -o hello hello.cpp `llvm-config --cxxflags --ldflags --system-libs --libs core`

