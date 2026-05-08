# Generated from gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,4,0,37,8,0,11,0,12,0,38,1,
        0,1,0,1,1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,2,1,
        2,1,2,1,2,3,2,58,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,79,8,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,96,8,7,10,7,12,7,99,
        9,7,1,7,1,7,1,7,1,7,5,7,105,8,7,10,7,12,7,108,9,7,1,7,3,7,111,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,119,8,8,10,8,12,8,122,9,8,1,8,1,8,
        1,9,1,9,1,10,1,10,1,10,5,10,131,8,10,10,10,12,10,134,9,10,1,11,1,
        11,1,11,5,11,139,8,11,10,11,12,11,142,9,11,1,12,1,12,1,12,5,12,147,
        8,12,10,12,12,12,150,9,12,1,13,1,13,1,13,3,13,155,8,13,1,14,1,14,
        1,14,5,14,160,8,14,10,14,12,14,163,9,14,1,15,1,15,1,15,5,15,168,
        8,15,10,15,12,15,171,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,182,8,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,0,4,1,0,19,20,1,0,21,24,1,0,15,16,1,0,17,18,190,0,36,
        1,0,0,0,2,42,1,0,0,0,4,53,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,10,74,
        1,0,0,0,12,83,1,0,0,0,14,89,1,0,0,0,16,112,1,0,0,0,18,125,1,0,0,
        0,20,127,1,0,0,0,22,135,1,0,0,0,24,143,1,0,0,0,26,151,1,0,0,0,28,
        156,1,0,0,0,30,164,1,0,0,0,32,181,1,0,0,0,34,37,3,2,1,0,35,37,3,
        4,2,0,36,34,1,0,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,
        39,1,0,0,0,39,40,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,5,1,0,
        0,43,44,5,28,0,0,44,48,5,9,0,0,45,47,3,6,3,0,46,45,1,0,0,0,47,50,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,
        51,52,5,10,0,0,52,3,1,0,0,0,53,54,5,2,0,0,54,57,5,28,0,0,55,56,5,
        3,0,0,56,58,3,18,9,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,
        60,5,13,0,0,60,5,1,0,0,0,61,68,3,8,4,0,62,68,3,10,5,0,63,68,3,12,
        6,0,64,68,3,14,7,0,65,68,3,16,8,0,66,68,3,4,2,0,67,61,1,0,0,0,67,
        62,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,
        0,68,7,1,0,0,0,69,70,5,28,0,0,70,71,5,14,0,0,71,72,3,18,9,0,72,73,
        5,13,0,0,73,9,1,0,0,0,74,75,5,4,0,0,75,78,5,11,0,0,76,79,5,30,0,
        0,77,79,3,18,9,0,78,76,1,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,81,
        5,12,0,0,81,82,5,13,0,0,82,11,1,0,0,0,83,84,5,5,0,0,84,85,5,11,0,
        0,85,86,5,28,0,0,86,87,5,12,0,0,87,88,5,13,0,0,88,13,1,0,0,0,89,
        90,5,6,0,0,90,91,5,11,0,0,91,92,3,18,9,0,92,93,5,12,0,0,93,97,5,
        9,0,0,94,96,3,6,3,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,
        98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,110,5,10,0,0,101,102,
        5,7,0,0,102,106,5,9,0,0,103,105,3,6,3,0,104,103,1,0,0,0,105,108,
        1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,
        1,0,0,0,109,111,5,10,0,0,110,101,1,0,0,0,110,111,1,0,0,0,111,15,
        1,0,0,0,112,113,5,8,0,0,113,114,5,11,0,0,114,115,3,18,9,0,115,116,
        5,12,0,0,116,120,5,9,0,0,117,119,3,6,3,0,118,117,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,
        1,0,0,0,123,124,5,10,0,0,124,17,1,0,0,0,125,126,3,20,10,0,126,19,
        1,0,0,0,127,132,3,22,11,0,128,129,5,26,0,0,129,131,3,22,11,0,130,
        128,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,
        21,1,0,0,0,134,132,1,0,0,0,135,140,3,24,12,0,136,137,5,25,0,0,137,
        139,3,24,12,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,23,1,0,0,0,142,140,1,0,0,0,143,148,3,26,13,0,144,
        145,7,0,0,0,145,147,3,26,13,0,146,144,1,0,0,0,147,150,1,0,0,0,148,
        146,1,0,0,0,148,149,1,0,0,0,149,25,1,0,0,0,150,148,1,0,0,0,151,154,
        3,28,14,0,152,153,7,1,0,0,153,155,3,28,14,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,27,1,0,0,0,156,161,3,30,15,0,157,158,7,2,0,0,158,
        160,3,30,15,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,
        162,1,0,0,0,162,29,1,0,0,0,163,161,1,0,0,0,164,169,3,32,16,0,165,
        166,7,3,0,0,166,168,3,32,16,0,167,165,1,0,0,0,168,171,1,0,0,0,169,
        167,1,0,0,0,169,170,1,0,0,0,170,31,1,0,0,0,171,169,1,0,0,0,172,173,
        5,11,0,0,173,174,3,18,9,0,174,175,5,12,0,0,175,182,1,0,0,0,176,177,
        5,27,0,0,177,182,3,32,16,0,178,182,5,28,0,0,179,182,5,29,0,0,180,
        182,5,30,0,0,181,172,1,0,0,0,181,176,1,0,0,0,181,178,1,0,0,0,181,
        179,1,0,0,0,181,180,1,0,0,0,182,33,1,0,0,0,17,36,38,48,57,67,78,
        97,106,110,120,132,140,148,154,161,169,181
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tarea'", "'ir_a'", "'si'", "'print'", 
                     "'input'", "'if'", "'else'", "'while'", "'{'", "'}'", 
                     "'('", "')'", "';'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "T_TAREA", "T_IR_A", "T_SI", "T_PRINT", 
                      "T_INPUT", "T_IF", "T_ELSE", "T_WHILE", "T_LBRACE", 
                      "T_RBRACE", "T_LPAREN", "T_RPAREN", "T_SEMICOLON", 
                      "T_ASSIGN", "T_PLUS", "T_MINUS", "T_MUL", "T_DIV", 
                      "T_EQ", "T_NEQ", "T_GT", "T_LT", "T_GEQ", "T_LEQ", 
                      "T_AND", "T_OR", "T_NOT", "ID", "NUMBER", "STRING", 
                      "WS", "COMMENT", "MULTILINE_COMMENT" ]

    RULE_program = 0
    RULE_task = 1
    RULE_transition = 2
    RULE_statement = 3
    RULE_assignment = 4
    RULE_printStmt = 5
    RULE_inputStmt = 6
    RULE_ifStmt = 7
    RULE_whileStmt = 8
    RULE_expression = 9
    RULE_logicalOrExpression = 10
    RULE_logicalAndExpression = 11
    RULE_equalityExpression = 12
    RULE_relationalExpression = 13
    RULE_additiveExpression = 14
    RULE_multiplicativeExpression = 15
    RULE_primary = 16

    ruleNames =  [ "program", "task", "transition", "statement", "assignment", 
                   "printStmt", "inputStmt", "ifStmt", "whileStmt", "expression", 
                   "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
                   "relationalExpression", "additiveExpression", "multiplicativeExpression", 
                   "primary" ]

    EOF = Token.EOF
    T_TAREA=1
    T_IR_A=2
    T_SI=3
    T_PRINT=4
    T_INPUT=5
    T_IF=6
    T_ELSE=7
    T_WHILE=8
    T_LBRACE=9
    T_RBRACE=10
    T_LPAREN=11
    T_RPAREN=12
    T_SEMICOLON=13
    T_ASSIGN=14
    T_PLUS=15
    T_MINUS=16
    T_MUL=17
    T_DIV=18
    T_EQ=19
    T_NEQ=20
    T_GT=21
    T_LT=22
    T_GEQ=23
    T_LEQ=24
    T_AND=25
    T_OR=26
    T_NOT=27
    ID=28
    NUMBER=29
    STRING=30
    WS=31
    COMMENT=32
    MULTILINE_COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def task(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.TaskContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.TaskContext,i)


        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.TransitionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.TransitionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 34
                    self.task()
                    pass
                elif token in [2]:
                    self.state = 35
                    self.transition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 40
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_TAREA(self):
            return self.getToken(gramaticaParser.T_TAREA, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def T_LBRACE(self):
            return self.getToken(gramaticaParser.T_LBRACE, 0)

        def T_RBRACE(self):
            return self.getToken(gramaticaParser.T_RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_task

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask" ):
                listener.enterTask(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask" ):
                listener.exitTask(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTask" ):
                return visitor.visitTask(self)
            else:
                return visitor.visitChildren(self)




    def task(self):

        localctx = gramaticaParser.TaskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_task)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(gramaticaParser.T_TAREA)
            self.state = 43
            self.match(gramaticaParser.ID)
            self.state = 44
            self.match(gramaticaParser.T_LBRACE)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435828) != 0):
                self.state = 45
                self.statement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(gramaticaParser.T_RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_IR_A(self):
            return self.getToken(gramaticaParser.T_IR_A, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def T_SEMICOLON(self):
            return self.getToken(gramaticaParser.T_SEMICOLON, 0)

        def T_SI(self):
            return self.getToken(gramaticaParser.T_SI, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_transition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransition" ):
                listener.enterTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransition" ):
                listener.exitTransition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransition" ):
                return visitor.visitTransition(self)
            else:
                return visitor.visitChildren(self)




    def transition(self):

        localctx = gramaticaParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(gramaticaParser.T_IR_A)
            self.state = 54
            self.match(gramaticaParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 55
                self.match(gramaticaParser.T_SI)
                self.state = 56
                self.expression()


            self.state = 59
            self.match(gramaticaParser.T_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(gramaticaParser.PrintStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(gramaticaParser.InputStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(gramaticaParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(gramaticaParser.WhileStmtContext,0)


        def transition(self):
            return self.getTypedRuleContext(gramaticaParser.TransitionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.assignment()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.printStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.inputStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.ifStmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.whileStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.transition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def T_ASSIGN(self):
            return self.getToken(gramaticaParser.T_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def T_SEMICOLON(self):
            return self.getToken(gramaticaParser.T_SEMICOLON, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramaticaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramaticaParser.ID)
            self.state = 70
            self.match(gramaticaParser.T_ASSIGN)
            self.state = 71
            self.expression()
            self.state = 72
            self.match(gramaticaParser.T_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_PRINT(self):
            return self.getToken(gramaticaParser.T_PRINT, 0)

        def T_LPAREN(self):
            return self.getToken(gramaticaParser.T_LPAREN, 0)

        def T_RPAREN(self):
            return self.getToken(gramaticaParser.T_RPAREN, 0)

        def T_SEMICOLON(self):
            return self.getToken(gramaticaParser.T_SEMICOLON, 0)

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramaticaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(gramaticaParser.T_PRINT)
            self.state = 75
            self.match(gramaticaParser.T_LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(gramaticaParser.STRING)
                pass

            elif la_ == 2:
                self.state = 77
                self.expression()
                pass


            self.state = 80
            self.match(gramaticaParser.T_RPAREN)
            self.state = 81
            self.match(gramaticaParser.T_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_INPUT(self):
            return self.getToken(gramaticaParser.T_INPUT, 0)

        def T_LPAREN(self):
            return self.getToken(gramaticaParser.T_LPAREN, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def T_RPAREN(self):
            return self.getToken(gramaticaParser.T_RPAREN, 0)

        def T_SEMICOLON(self):
            return self.getToken(gramaticaParser.T_SEMICOLON, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = gramaticaParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(gramaticaParser.T_INPUT)
            self.state = 84
            self.match(gramaticaParser.T_LPAREN)
            self.state = 85
            self.match(gramaticaParser.ID)
            self.state = 86
            self.match(gramaticaParser.T_RPAREN)
            self.state = 87
            self.match(gramaticaParser.T_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._statement = None # StatementContext
            self.if_block = list() # of StatementContexts
            self.else_block = list() # of StatementContexts

        def T_IF(self):
            return self.getToken(gramaticaParser.T_IF, 0)

        def T_LPAREN(self):
            return self.getToken(gramaticaParser.T_LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def T_RPAREN(self):
            return self.getToken(gramaticaParser.T_RPAREN, 0)

        def T_LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_LBRACE)
            else:
                return self.getToken(gramaticaParser.T_LBRACE, i)

        def T_RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_RBRACE)
            else:
                return self.getToken(gramaticaParser.T_RBRACE, i)

        def T_ELSE(self):
            return self.getToken(gramaticaParser.T_ELSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = gramaticaParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(gramaticaParser.T_IF)
            self.state = 90
            self.match(gramaticaParser.T_LPAREN)
            self.state = 91
            self.expression()
            self.state = 92
            self.match(gramaticaParser.T_RPAREN)
            self.state = 93
            self.match(gramaticaParser.T_LBRACE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435828) != 0):
                self.state = 94
                localctx._statement = self.statement()
                localctx.if_block.append(localctx._statement)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(gramaticaParser.T_RBRACE)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 101
                self.match(gramaticaParser.T_ELSE)
                self.state = 102
                self.match(gramaticaParser.T_LBRACE)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435828) != 0):
                    self.state = 103
                    localctx._statement = self.statement()
                    localctx.else_block.append(localctx._statement)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.match(gramaticaParser.T_RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._statement = None # StatementContext
            self.block = list() # of StatementContexts

        def T_WHILE(self):
            return self.getToken(gramaticaParser.T_WHILE, 0)

        def T_LPAREN(self):
            return self.getToken(gramaticaParser.T_LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def T_RPAREN(self):
            return self.getToken(gramaticaParser.T_RPAREN, 0)

        def T_LBRACE(self):
            return self.getToken(gramaticaParser.T_LBRACE, 0)

        def T_RBRACE(self):
            return self.getToken(gramaticaParser.T_RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = gramaticaParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(gramaticaParser.T_WHILE)
            self.state = 113
            self.match(gramaticaParser.T_LPAREN)
            self.state = 114
            self.expression()
            self.state = 115
            self.match(gramaticaParser.T_RPAREN)
            self.state = 116
            self.match(gramaticaParser.T_LBRACE)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435828) != 0):
                self.state = 117
                localctx._statement = self.statement()
                localctx.block.append(localctx._statement)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(gramaticaParser.T_RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(gramaticaParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = gramaticaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.LogicalAndExpressionContext,i)


        def T_OR(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_OR)
            else:
                return self.getToken(gramaticaParser.T_OR, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = gramaticaParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.logicalAndExpression()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 128
                self.match(gramaticaParser.T_OR)
                self.state = 129
                self.logicalAndExpression()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.EqualityExpressionContext,i)


        def T_AND(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_AND)
            else:
                return self.getToken(gramaticaParser.T_AND, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = gramaticaParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.equalityExpression()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 136
                self.match(gramaticaParser.T_AND)
                self.state = 137
                self.equalityExpression()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.RelationalExpressionContext,i)


        def T_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_EQ)
            else:
                return self.getToken(gramaticaParser.T_EQ, i)

        def T_NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_NEQ)
            else:
                return self.getToken(gramaticaParser.T_NEQ, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = gramaticaParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.relationalExpression()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.relationalExpression()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.AdditiveExpressionContext,i)


        def T_GT(self):
            return self.getToken(gramaticaParser.T_GT, 0)

        def T_LT(self):
            return self.getToken(gramaticaParser.T_LT, 0)

        def T_GEQ(self):
            return self.getToken(gramaticaParser.T_GEQ, 0)

        def T_LEQ(self):
            return self.getToken(gramaticaParser.T_LEQ, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = gramaticaParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.additiveExpression()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0):
                self.state = 152
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.MultiplicativeExpressionContext,i)


        def T_PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_PLUS)
            else:
                return self.getToken(gramaticaParser.T_PLUS, i)

        def T_MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_MINUS)
            else:
                return self.getToken(gramaticaParser.T_MINUS, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = gramaticaParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.multiplicativeExpression()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.multiplicativeExpression()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.PrimaryContext,i)


        def T_MUL(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_MUL)
            else:
                return self.getToken(gramaticaParser.T_MUL, i)

        def T_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.T_DIV)
            else:
                return self.getToken(gramaticaParser.T_DIV, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = gramaticaParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.primary()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.primary()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_LPAREN(self):
            return self.getToken(gramaticaParser.T_LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def T_RPAREN(self):
            return self.getToken(gramaticaParser.T_RPAREN, 0)

        def T_NOT(self):
            return self.getToken(gramaticaParser.T_NOT, 0)

        def primary(self):
            return self.getTypedRuleContext(gramaticaParser.PrimaryContext,0)


        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = gramaticaParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primary)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(gramaticaParser.T_LPAREN)
                self.state = 173
                self.expression()
                self.state = 174
                self.match(gramaticaParser.T_RPAREN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(gramaticaParser.T_NOT)
                self.state = 177
                self.primary()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(gramaticaParser.ID)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(gramaticaParser.NUMBER)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.match(gramaticaParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





