grammar Expr;
INT : [0-9]+ ;
FLOAT : [0-9]+[.][0-9] ;
WS : [ \t\n\r]+ -> skip ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

program: ((expr | asing) ';')* EOF;
expr
    : value
    | ('+' | '-') expr
    | ('>') expr
    | '!' expr
    | ('*' | '/' | '%') expr expr
    | ('+' | '-') expr expr
    | '^' expr expr
    | '|' expr '|'
    | '(' expr ')'
    | value
    ;
asing: ID '=' expr;
value: INT | FLOAT | ID;
