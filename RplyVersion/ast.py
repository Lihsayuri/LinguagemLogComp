import sys
import re

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def evaluate(self):
        pass


class SymbolTable:
    table = {}

    def create(type, variable, value):
        if variable not in SymbolTable.table:
            SymbolTable.table[variable] = (type, value)
        else:
            sys.stderr.write("Erro: variável já declarada")

    def getter(variable):
        return SymbolTable.table[variable]
    
    def setter( variable, value):
        if SymbolTable.table[variable][0] == value[0]:
            SymbolTable.table[variable] =  value
        else:
            sys.stderr.write("Erro de tipos: atribuição de valor incompatível com o tipo da variável")
            

class Structure(Node):
    def evaluate(self):
        for child in self.children:
            child.evaluate()


class VarDec(Node):
    def evaluate(self):
        SymbolTable.create(self.value, self.children[0].value, self.children[1].evaluate()[1])


class StringVal(Node):
    def evaluate(self):
        return ("string", str(self.value))