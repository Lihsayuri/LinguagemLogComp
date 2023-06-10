# Linguagem de Fórmula 1 - f1Strategy <img src="https://img.shields.io/static/v1?label=ConceitoB&message=Finalizado&color=success&style=flat-square&logo=ghost"/>


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

**Observação:** Antes de entregar a etapa 2, troquei tudo para o rply, ambas as versões são iguais, mas a partir da próxima etapa só utilizarei o Rply. Essa entrega está na pasta `RplyVersion`

## Terceira tarefa

Para fazer a terceira tarefa - no caso, para o conceito B - implementei o compilador da linguagem em Python com base no que aprendemos com o compilador desenvolvido na disciplina. A linguagem sofreu alterações importantes:

- Agora existem apenas 3 tipos de variáveis: lap (INT), driver (String), tyre ({tipo do pneu, status do pneu})
- O objetivo é criar estratégias de troca de pneu para uma corrida. Para isso temos condições que podem ser feitas com o `radio_check` e temos `Setup`s que podem ser construídos e chamados durantes voltas específicas da corrida.
- Temos operações como +, -, >, < , igualdade("equals").
- Além disso, temos o loop principal da corrida que é inicializado com a volta inicial e a volta final.

No final, o programa vai de maneira divertida indicar ao programador em que posição seu piloto terminou, considerando alguns cenários como safety car e batidas.

**Observação**: Essa entrega está na pasta ConceitoB.

Um exemplo de programa pode ser visto abaixo:

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

- Output para o input apresentado: 

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

- Outro input - `teste2.txt`:

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

- Output do `teste2.txt`:

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

- Por fim, mais um input do terceiro exemplo `teste3.txt`:

```
START
lap volta is 12
lap volta_grande is 2 > 3
driver piloto1 is 'Hamilton'
FINISH
```

- Output do `teste3.txt`:
```
AS LUZES SE APAGAM E LÁ VAMOS NÓS!
Engenheiro : Lap check para o piloto  12
Engenheiro : Lap check para o piloto  0
Engenheiro : Radio check para o piloto  Hamilton
```

## EBNF da linguagem

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

## Diagrama Sintático da linguagem [atualizado para versão da tarefa 3]

<img src="diagrama_sintatico.drawio.png" width="800" height="600">



