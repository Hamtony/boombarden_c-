# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,15,75,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,4,12,57,8,
        12,11,12,12,12,58,1,13,4,13,62,8,13,11,13,12,13,63,1,13,1,13,1,13,
        1,14,4,14,70,8,14,11,14,12,14,71,1,14,1,14,0,0,15,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,1,
        0,3,1,0,48,57,1,0,46,46,3,0,9,10,13,13,32,32,77,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,1,31,1,0,0,0,3,33,1,
        0,0,0,5,35,1,0,0,0,7,37,1,0,0,0,9,39,1,0,0,0,11,41,1,0,0,0,13,43,
        1,0,0,0,15,45,1,0,0,0,17,47,1,0,0,0,19,49,1,0,0,0,21,51,1,0,0,0,
        23,53,1,0,0,0,25,56,1,0,0,0,27,61,1,0,0,0,29,69,1,0,0,0,31,32,5,
        59,0,0,32,2,1,0,0,0,33,34,5,43,0,0,34,4,1,0,0,0,35,36,5,45,0,0,36,
        6,1,0,0,0,37,38,5,62,0,0,38,8,1,0,0,0,39,40,5,33,0,0,40,10,1,0,0,
        0,41,42,5,42,0,0,42,12,1,0,0,0,43,44,5,47,0,0,44,14,1,0,0,0,45,46,
        5,37,0,0,46,16,1,0,0,0,47,48,5,94,0,0,48,18,1,0,0,0,49,50,5,124,
        0,0,50,20,1,0,0,0,51,52,5,40,0,0,52,22,1,0,0,0,53,54,5,41,0,0,54,
        24,1,0,0,0,55,57,7,0,0,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,
        0,58,59,1,0,0,0,59,26,1,0,0,0,60,62,7,0,0,0,61,60,1,0,0,0,62,63,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,7,1,0,0,
        66,67,7,0,0,0,67,28,1,0,0,0,68,70,7,2,0,0,69,68,1,0,0,0,70,71,1,
        0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,6,14,0,0,74,
        30,1,0,0,0,4,0,58,63,71,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    INT = 13
    FLOAT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'+'", "'-'", "'>'", "'!'", "'*'", "'/'", "'%'", "'^'", 
            "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "INT", "FLOAT", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

