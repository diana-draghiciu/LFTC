%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token MAIN
%token READ
%token WRITE
%token IF
%token ELSE
%token FOR
%token IN
%token WHILE
%token INT
%token STRING
%token INTARR
%token STRINGARR
%token ISLT
%token ISLTE
%token IS
%token ISNOT
%token ISGT
%token ISGTE
%token ODD
%token EVEN
%token AND
%token OR

%token IDENTIFIER
%token CONSTANT

%token ASSIGN

%left '+' '-' '*' '/'

%token ADD 
%token SUB
%token DIV 
%token MUL 

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 

%token COLON
%token COMMA 
%token SEMI_COLON

%start program
%error-verbose

%%
program : MAIN OPEN_ROUND_BRACKET CLOSED_ROUND_BRACKET COLON stmtList;
declaration: type IDENTIFIER
type1 :  INT | STRING;
arraydecl : INTARR | STRINGARR
type :  type1 | arraydecl;
stmtList: statement |  statement stmtList;
statement : assignStatement | ioStatement | declaration | ifStatement | forStatement | foreachStatement | whileStatement;
assignStatement : IDENTIFIER ASSIGN expression;
expression: expression ADD term | expression SUB term | term | EVEN | ODD
term: term MUL factor | term DIV factor |  factor
factor: OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | IDENTIFIER | CONSTANT
ioStatement : READ IDENTIFIER | WRITE IDENTIFIER | WRITE CONSTANT;     
ifStatement : IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET ELSE OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET | IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET;
forStatement :  FOR OPEN_ROUND_BRACKET assignStatement SEMI_COLON condition SEMI_COLON assignStatement CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET;	
foreachStatement: FOR OPEN_ROUND_BRACKET IDENTIFIER IN IDENTIFIER CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET;	
whileStatement :  WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement CLOSED_CURLY_BRACKET;   
condition : expression relation expression | condition logicalop condition;
relation : ISLT | ISLTE | IS | ISNOT | ISGTE | ISGT;
logicalop: OR | AND

%%
yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}