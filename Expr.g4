grammar Expr;
INT : [0-9]+ ;
FLOAT : [0-9]+[.][0-9] ;
WS : [ \t\n\r]+ -> skip ;

program: expr(';' expr)* EOF;
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
value: INT | FLOAT;
