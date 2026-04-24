grammar WhileLang;

program : statement* EOF ;

statement : assignment | whileStmt | ifStmt ;

assignment : ID '=' expression ';' ;

whileStmt : 'while' '(' expression ')' '{' statement* '}' ;

ifStmt : 'if' '(' expression ')' '{' statement* '}' ('else' '{' statement* '}')? ;

expression : additiveExpression (('>' | '<' | '==') additiveExpression)* ;

additiveExpression : multiplicativeExpression (('+' | '-') multiplicativeExpression)* ;

multiplicativeExpression : primary (('*' | '/') primary)* ;

primary : '(' expression ')' | ID | NUMBER ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

NUMBER : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;