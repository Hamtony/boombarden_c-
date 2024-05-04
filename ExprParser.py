# Generated from Expr.g4 by ANTLR 4.13.1
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
        4,1,17,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,3,0,11,8,0,1,0,
        1,0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,0,
        0,4,0,2,4,6,0,3,1,0,2,3,1,0,6,8,2,0,14,15,17,17,64,0,16,1,0,0,0,
        2,49,1,0,0,0,4,51,1,0,0,0,6,55,1,0,0,0,8,11,3,2,1,0,9,11,3,4,2,0,
        10,8,1,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,13,5,1,0,0,13,15,1,0,
        0,0,14,10,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,19,
        1,0,0,0,18,16,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,50,3,6,3,0,22,
        23,7,0,0,0,23,50,3,2,1,0,24,25,5,4,0,0,25,50,3,2,1,0,26,27,5,5,0,
        0,27,50,3,2,1,0,28,29,7,1,0,0,29,30,3,2,1,0,30,31,3,2,1,0,31,50,
        1,0,0,0,32,33,7,0,0,0,33,34,3,2,1,0,34,35,3,2,1,0,35,50,1,0,0,0,
        36,37,5,9,0,0,37,38,3,2,1,0,38,39,3,2,1,0,39,50,1,0,0,0,40,41,5,
        10,0,0,41,42,3,2,1,0,42,43,5,10,0,0,43,50,1,0,0,0,44,45,5,11,0,0,
        45,46,3,2,1,0,46,47,5,12,0,0,47,50,1,0,0,0,48,50,3,6,3,0,49,21,1,
        0,0,0,49,22,1,0,0,0,49,24,1,0,0,0,49,26,1,0,0,0,49,28,1,0,0,0,49,
        32,1,0,0,0,49,36,1,0,0,0,49,40,1,0,0,0,49,44,1,0,0,0,49,48,1,0,0,
        0,50,3,1,0,0,0,51,52,5,17,0,0,52,53,5,13,0,0,53,54,3,2,1,0,54,5,
        1,0,0,0,55,56,7,2,0,0,56,7,1,0,0,0,3,10,16,49
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'>'", "'!'", "'*'", 
                     "'/'", "'%'", "'^'", "'|'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "WS", "ID" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_asing = 2
    RULE_value = 3

    ruleNames =  [ "program", "expr", "asing", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    FLOAT=15
    WS=16
    ID=17

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
            return self.getToken(ExprParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def asing(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AsingContext)
            else:
                return self.getTypedRuleContext(ExprParser.AsingContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 184316) != 0):
                self.state = 10
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.asing()
                    pass


                self.state = 12
                self.match(ExprParser.T__0)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 23
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(ExprParser.T__3)
                self.state = 25
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(ExprParser.T__4)
                self.state = 27
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.expr()
                self.state = 30
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.expr()
                self.state = 34
                self.expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.match(ExprParser.T__8)
                self.state = 37
                self.expr()
                self.state = 38
                self.expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.match(ExprParser.T__9)
                self.state = 41
                self.expr()
                self.state = 42
                self.match(ExprParser.T__9)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 44
                self.match(ExprParser.T__10)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(ExprParser.T__11)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 48
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_asing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsing" ):
                listener.enterAsing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsing" ):
                listener.exitAsing(self)




    def asing(self):

        localctx = ExprParser.AsingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ExprParser.ID)
            self.state = 52
            self.match(ExprParser.T__12)
            self.state = 53
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 180224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





