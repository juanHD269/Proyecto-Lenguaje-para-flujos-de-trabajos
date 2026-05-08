grammar gramatica;

// Reglas de análisis sintáctico
program : (task | transition)+ EOF ;

task : T_TAREA ID T_LBRACE statement* T_RBRACE ;

transition : T_IR_A ID (T_SI expression)? T_SEMICOLON ;

statement : assignment | printStmt | inputStmt | ifStmt | whileStmt | transition ;

assignment : ID T_ASSIGN expression T_SEMICOLON ;

printStmt : T_PRINT T_LPAREN (STRING | expression) T_RPAREN T_SEMICOLON ;

inputStmt : T_INPUT T_LPAREN ID T_RPAREN T_SEMICOLON ;

ifStmt : T_IF T_LPAREN expression T_RPAREN T_LBRACE if_block+=statement* T_RBRACE (T_ELSE T_LBRACE else_block+=statement* T_RBRACE)? ;

whileStmt : T_WHILE T_LPAREN expression T_RPAREN T_LBRACE block+=statement* T_RBRACE ;

expression : logicalOrExpression ;

logicalOrExpression : logicalAndExpression (T_OR logicalAndExpression)* ;

logicalAndExpression : equalityExpression (T_AND equalityExpression)* ;

equalityExpression : relationalExpression ((T_EQ | T_NEQ) relationalExpression)* ;

relationalExpression : additiveExpression ((T_GT | T_LT | T_GEQ | T_LEQ) additiveExpression)? ;

additiveExpression : multiplicativeExpression ((T_PLUS | T_MINUS) multiplicativeExpression)* ;

multiplicativeExpression : primary ((T_MUL | T_DIV) primary)* ;

primary : T_LPAREN expression T_RPAREN | T_NOT primary | ID | NUMBER | STRING ;

// Reglas de análisis léxico (Tokens)
T_TAREA : 'tarea' ;
T_IR_A : 'ir_a' ;
T_SI : 'si' ;
T_PRINT : 'print' ;
T_INPUT : 'input' ;
T_IF : 'if' ;
T_ELSE : 'else' ;
T_WHILE : 'while' ;

T_LBRACE : '{' ;
T_RBRACE : '}' ;
T_LPAREN : '(' ;
T_RPAREN : ')' ;
T_SEMICOLON : ';' ;
T_ASSIGN : '=' ;

T_PLUS : '+' ;
T_MINUS : '-' ;
T_MUL : '*' ;
T_DIV : '/' ;

T_EQ : '==' ;
T_NEQ : '!=' ;
T_GT : '>' ;
T_LT : '<' ;
T_GEQ : '>=' ;
T_LEQ : '<=' ;

T_AND : '&&' ;
T_OR : '||' ;
T_NOT : '!' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip ;
