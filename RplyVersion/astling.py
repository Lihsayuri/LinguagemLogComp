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
            print(f"Câmbio, {variable} sendo {value} setado com sucesso.")
        else:
            sys.stderr.write("Erro: variável já declarada")
        # print("Aquiii a symbol table: ", SymbolTable.table)

    def getter(variable):
        print("Aquiii a symbol table: ", SymbolTable.table)
        return SymbolTable.table[variable]
    
    def setter(variable, value):
        if SymbolTable.table[variable][0] == value[0]:
            SymbolTable.table[variable] =  value
        else:
            sys.stderr.write("Erro de tipos: atribuição de valor incompatível com o tipo da variável")
        print("Aquiii a symbol table: ", SymbolTable.table)
            

class Structure(Node):
    def evaluate(self):
        for child in self.children:
            child.evaluate()

class VarDec(Node):
    def evaluate(self):
        SymbolTable.create(self.value, self.children[0].value, self.children[1].evaluate()[1])
        print(f"Variável '{self.children[0].value}' criada com sucesso.")
        return self.children[1].evaluate()

class While(Node):
    def evaluate(self):
        for i in self.children[0].evaluate():
            self.children[1].evaluate()


class StringVal(Node):
    def evaluate(self):
        return ("string", str(self.value))