/*
 * Student's name: Trần Minh Hiếu
 * Student ID: 2113363
*/

grammar ZCode;
@lexer::header {
from lexererr import *
}
options {
	language=Python3;
}

// Declaredd
program: NEWLINE* listDeclared EOF;
listDeclared: declared listDeclared | declared;
declared: functionDeclared | variablesDeclared ignore;

// Variable Declared
variablesDeclared: explicitTypeDeclared | implicitVarDeclared  | implicitDynamicDeclared;
explicitTypeDeclared:  explicitType ID initVariableValueOrNull | explicitType ID LBRACK numbersList RBRACK initVariableValueOrNull;
explicitType: STRING | BOOL | NUMBER;
implicitVarDeclared: VAR ID initVariableValue;      
implicitDynamicDeclared: DYNAMIC ID initVariableValueOrNull;
initVariableValueOrNull: ASSIGN express | ;
initVariableValue: ASSIGN express;

numbersList: NUMBERLIT COMMA numbersList | NUMBERLIT;

functionDeclared: FUNC ID LPAREN prametersList RPAREN (ignore? blockStatement | ignore? returnStatement | ignore);  
prametersList: paramsPrime | ;
paramsPrime: param COMMA paramsPrime | param;
param: explicitType (ID | ID LBRACK numbersList RBRACK);

// Statement
statementList: statement statementList | ;

statement: declaredStatement | assignmentStatement | conditionStatement | forStatement 
            | breakStatement | continueStatement | returnStatement | callStatement | blockStatement;

declaredStatement: variablesDeclared ignore;   

assignmentStatement: (ID | ID indexOperatorNew) ASSIGN express ignore;
indexOperatorNew: (LBRACK expressList RBRACK);  

conditionStatement: IF conditionAndStatement (elseIfStatement | ) (elseStatement | );
elseIfStatement: ELIF conditionAndStatement elseIfStatement | ELIF conditionAndStatement;
elseStatement: ELSE ignore statement | ELSE statement;
conditionAndStatement: conditionExpress (ignore statement | statement);
conditionExpress: LPAREN express RPAREN;

forStatement: FOR ID UNTIL express BY express (statement | ignore statement);
continueStatement: CONTINUE ignore;
breakStatement: BREAK ignore;
returnStatement: RETURN (express | ) ignore; 
blockStatement:  BEGIN ignore (statementList | ) END ignore;

callFunction: ID LPAREN (expressList | ) RPAREN;
callStatement: ID LPAREN (expressList | ) RPAREN ignore;

// Expression
expressList: express COMMA expressList | express;
express:  express1 CONCAT express1 | express1;
express1: express2 (EQ | EQEQ | NEQ | LT | GT | LTE | GTE ) express2 | express2;
express2: express2 (AND | OR) express3 | express3;
express3: express3 (ADD | SUB) express4 | express4;
express4: express4 (MUL | DIV | MOD) express5 | express5;
express5: NOT express5 | express6;
express6: SUB express6 | express7 | express8;
express7: (ID | callFunction) (LBRACK expressList RBRACK);  
express8: NUMBERLIT | STRINGLIT | TRUE | FALSE | ID | arrayLiteral | (LPAREN express RPAREN) | callFunction;
arrayLiteral: LBRACK expressList RBRACK; 
 
ignore: NEWLINE+;

//KeyWord
TRUE : 'true'; FALSE : 'false'; NUMBER : 'number'; BOOL : 'bool';
STRING : 'string'; RETURN : 'return'; VAR : 'var'; DYNAMIC : 'dynamic';
FUNC : 'func'; FOR : 'for'; UNTIL : 'until'; BY : 'by'; BREAK : 'break';
CONTINUE : 'continue'; IF : 'if'; ELSE : 'else'; ELIF : 'elif'; BEGIN : 'begin';
END : 'end';

//Operator
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%'; EQ: '='; ASSIGN: '<-'; NEQ: '!=';
LT: '<'; LTE: '<='; GT: '>'; GTE: '>='; CONCAT: '...'; EQEQ: '=='; AND: 'and'; OR: 'or';
NOT: 'not';

//Separator
LPAREN : '('; RPAREN : ')'; LBRACK : '['; RBRACK : ']'; COMMA : ',';
 
//Identifier
ID : IDSTART IDCHAR*;
fragment IDSTART : [A-Za-z_];
fragment IDCHAR : [A-Za-z0-9_];

//Literal 
BOOLEAN: TRUE | FALSE;
STRINGLIT : '"' ( ~[\r\n\f\\"] | '\\' [btfrn'\\] | [']["] )* '"' {self.text = self.text[1:-1];};
NUMBERLIT: INT (DEC | DEC? EXP?);
fragment INT : [0-9]+;
fragment DEC : '.' [0-9]*;
fragment EXP : [eE] [-+]? [0-9]+;

// Comment
NEWLINE: [\n]; 
WS : [ \t\r\f\b]+ -> skip;  
COMMENTS: '##' ~[\n\r\f]* -> skip; 

// Error
UNCLOSE_STRING: '"' ( ~[\r\n\f\\"] | '\\' [btfrn'\\] | [']["] )* ( '\r\n' | '\n' | EOF )
{
   if (len(self.text) >= 2 and self.text[-2:] == '\r\n'):
      raise UncloseString(self.text[1:-2])
   elif self.text[-1] == '\n':
      raise UncloseString(self.text[1:-1])
   else:
      raise UncloseString(self.text[1:])
};
fragment ILLEGAL : ( [\r\f\b] | '\\' ~[btfrn'\\] ) ;
ILLEGAL_ESCAPE: '"' ( ~[\r\n\f\\"] | '\\' [btfrn'\\] | [']["] )* ILLEGAL
{
	raise IllegalEscape(self.text[1:]);
};
ERROR_CHAR: .{raise ErrorToken(self.text)};

// ----------- End Lexical  ----------- //

