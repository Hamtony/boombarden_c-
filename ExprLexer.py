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
        4,0,17,88,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,13,4,13,63,8,13,11,13,12,13,64,1,14,4,14,68,8,14,
        11,14,12,14,69,1,14,1,14,1,14,1,15,4,15,76,8,15,11,15,12,15,77,1,
        15,1,15,1,16,1,16,5,16,84,8,16,10,16,12,16,87,9,16,0,0,17,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,1,0,5,1,0,48,57,1,0,46,46,3,0,9,10,13,13,32,32,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,91,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,1,35,1,0,0,0,3,37,1,0,0,0,5,39,1,0,0,0,7,41,1,0,0,0,9,
        43,1,0,0,0,11,45,1,0,0,0,13,47,1,0,0,0,15,49,1,0,0,0,17,51,1,0,0,
        0,19,53,1,0,0,0,21,55,1,0,0,0,23,57,1,0,0,0,25,59,1,0,0,0,27,62,
        1,0,0,0,29,67,1,0,0,0,31,75,1,0,0,0,33,81,1,0,0,0,35,36,5,59,0,0,
        36,2,1,0,0,0,37,38,5,43,0,0,38,4,1,0,0,0,39,40,5,45,0,0,40,6,1,0,
        0,0,41,42,5,62,0,0,42,8,1,0,0,0,43,44,5,33,0,0,44,10,1,0,0,0,45,
        46,5,42,0,0,46,12,1,0,0,0,47,48,5,47,0,0,48,14,1,0,0,0,49,50,5,37,
        0,0,50,16,1,0,0,0,51,52,5,94,0,0,52,18,1,0,0,0,53,54,5,124,0,0,54,
        20,1,0,0,0,55,56,5,40,0,0,56,22,1,0,0,0,57,58,5,41,0,0,58,24,1,0,
        0,0,59,60,5,61,0,0,60,26,1,0,0,0,61,63,7,0,0,0,62,61,1,0,0,0,63,
        64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,28,1,0,0,0,66,68,7,0,0,
        0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,
        1,0,0,0,71,72,7,1,0,0,72,73,7,0,0,0,73,30,1,0,0,0,74,76,7,2,0,0,
        75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,79,1,
        0,0,0,79,80,6,15,0,0,80,32,1,0,0,0,81,85,7,3,0,0,82,84,7,4,0,0,83,
        82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,34,1,0,0,
        0,87,85,1,0,0,0,5,0,64,69,77,85,1,6,0,0
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
    T__12 = 13
    INT = 14
    FLOAT = 15
    WS = 16
    ID = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'+'", "'-'", "'>'", "'!'", "'*'", "'/'", "'%'", "'^'", 
            "'|'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "WS", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "INT", 
                  "FLOAT", "WS", "ID" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


