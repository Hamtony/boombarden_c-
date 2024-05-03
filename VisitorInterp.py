import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import math


class VisitorInterp(ExprVisitor):
    def visitValue(self, ctx:ExprParser.ValueContext):
        if ctx.getText().find(".")!=-1:
            return float(ctx.getText())
        else:
            return int(ctx.getText())
            

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
            return 0
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
            return 0
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return 0

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        for i in range(0, ctx.getChildCount(), 2):
            print(self.visit(ctx.getChild(i)))
        return 0