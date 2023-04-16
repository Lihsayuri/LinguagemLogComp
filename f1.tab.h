/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_F1_TAB_H_INCLUDED
# define YY_YY_F1_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    IDENTIFIER = 258,
    IS = 259,
    STRING = 260,
    INT = 261,
    FLOAT = 262,
    BOOLEAN = 263,
    TUPLE_INT = 264,
    TUPLE_DRS = 265,
    TYRE = 266,
    TYRE_SET = 267,
    VAR_TYPE = 268,
    SECTOR = 269,
    TYRE_TYPE = 270,
    TYRE_STATUS = 271,
    ATRIBUTE = 272,
    PLUS = 273,
    MINUS = 274,
    LESS = 275,
    GREATER = 276,
    LESS_EQUAL = 277,
    GREATER_EQUAL = 278,
    STRUCTURE = 279,
    ENGINE_ON = 280,
    RACE_LOOP = 281,
    ENGINE_OFF = 282,
    SET_UP = 283,
    RADIO_OFF = 284,
    RADIO_ON = 285,
    RADIO_CHECK = 286,
    REF_VAR_ATRIBUTE = 287,
    CALL = 288,
    THEN = 289,
    ELSE = 290,
    IN = 291,
    NEED = 292,
    COMMA = 293,
    OR = 294,
    AND = 295,
    NOT = 296,
    LOWER_THAN_ELSE = 297
  };
#endif

/* Value type.  */


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_F1_TAB_H_INCLUDED  */
