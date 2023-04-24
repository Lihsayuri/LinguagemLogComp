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

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
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
    BEGIN_PROGRAM = 258,
    END_PROGRAM = 259,
    REF_VAR_ATRIBUTE = 260,
    VAR_TYPE = 261,
    LOOP_ON = 262,
    LOOP_OFF = 263,
    SETUP = 264,
    RADIO_ON = 265,
    RADIO_OFF = 266,
    RADIO_CHECK = 267,
    SILENCE = 268,
    COPY = 269,
    CALL = 270,
    IN = 271,
    LOGICAL = 272,
    THEN = 273,
    NEED = 274,
    BOOLEAN = 275,
    OPERATOR = 276,
    SECTOR = 277,
    TYRE_TYPE = 278,
    TYRE_STATUS = 279,
    COMMA = 280,
    OPEN_PARENTHESIS = 281,
    CLOSE_PARENTHESIS = 282,
    OPEN_BRACKETS = 283,
    CLOSE_BRACKETS = 284,
    OPEN_BRACES = 285,
    CLOSE_BRACES = 286,
    IS = 287,
    STRING = 288,
    IDENTIFIER = 289,
    INT = 290,
    FLOAT = 291,
    NEWLINE = 292
  };
#endif
/* Tokens.  */
#define BEGIN_PROGRAM 258
#define END_PROGRAM 259
#define REF_VAR_ATRIBUTE 260
#define VAR_TYPE 261
#define LOOP_ON 262
#define LOOP_OFF 263
#define SETUP 264
#define RADIO_ON 265
#define RADIO_OFF 266
#define RADIO_CHECK 267
#define SILENCE 268
#define COPY 269
#define CALL 270
#define IN 271
#define LOGICAL 272
#define THEN 273
#define NEED 274
#define BOOLEAN 275
#define OPERATOR 276
#define SECTOR 277
#define TYRE_TYPE 278
#define TYRE_STATUS 279
#define COMMA 280
#define OPEN_PARENTHESIS 281
#define CLOSE_PARENTHESIS 282
#define OPEN_BRACKETS 283
#define CLOSE_BRACKETS 284
#define OPEN_BRACES 285
#define CLOSE_BRACES 286
#define IS 287
#define STRING 288
#define IDENTIFIER 289
#define INT 290
#define FLOAT 291
#define NEWLINE 292

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
