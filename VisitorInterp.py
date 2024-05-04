import sys
from tkinter import NO
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import math
import re

class VisitorInterp(ExprVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.memory = dict()
    
    def visitValue(self, ctx:ExprParser.ValueContext):
        if re.search("[a-zA-Z_][a-zA-Z_0-9]*", ctx.getText()):
            return self.memory[ctx.getText()]
        if ctx.getText().find(".")!=-1:
            return float(ctx.getText())
        else:
            return int(ctx.getText())
        return None

    def visitExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.getChild(1))
            if ctx.getChild(0).getText() == "|":
                return abs(self.visit(ctx.getChild(1)))
            op = ctx.getChild(0).getText()
            v1 = self.visit(ctx.getChild(1))
            v2 = self.visit(ctx.getChild(2))
            if op == "+":
                return v1 + v2
            if op == "-":
                return v1 - v2
            if op == "*":
                return v1 * v2
            if op == "/":
                return v1 / v2
            if op == "%":
                return v1 % v2
            if op == "^":
                math.pow(v1,v2)
                return None
            return None
        if ctx.getChildCount() == 2:
            opc = ctx.getChild(0).getText()
            if opc == "+":
                return self.visit(ctx.getChild(1))
            if opc == "-":
                return - self.visit(ctx.getChild(1))
            if opc == "!":
                return math.factorial(self.visit(ctx.getChild(1)))
            if opc == ">":
                return math.sqrt(self.visit(ctx.getChild(1)))
            return None
        if ctx.getChildCount() == 1:                
            return self.visit(ctx.getChild(0))
        return None
    
    def visitAsing(self, ctx:ExprParser.AsingContext):
        v1 = ctx.getChild(0).getText()
        v2 = self.visit(ctx.getChild(2))
        self.memory[v1] = v2
        return None
    
    def visit(self, tree):
        if type(tree) == ExprParser.AsingContext:
            return self.visitAsing(tree)
        elif type(tree) == ExprParser.ValueContext:
            return self.visitValue(tree)
        elif type(tree) == ExprParser.ExprContext:
            return self.visitExpr(tree)
            
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        outputs = []
        for i in range(0, ctx.getChildCount(),2):
            outputs.append(self.visit(ctx.getChild(i)))
        for output in outputs:
            if output != None:
                print(output)
        print(self.memory)
        return None