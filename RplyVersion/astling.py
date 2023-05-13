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
            print("Crieiii")
            SymbolTable.table[variable] = (type, value)
            print(f"Câmbio, {variable} sendo {value} setado com sucesso.")
            return SymbolTable.table[variable]
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
        print("Entrei no Structure")
        print("AST Aqui o valor do self.value: ", self.value)
        print("AST Aqui o valor do self.children: ", self.children)
        print(len(self.children))
        inverte = self.children[::-1]
        for child in inverte:
            print("AST Aqui o valor do child: ", child)
            filho = child[0].evaluate()
            print("AST Aqui o valor do child: ", filho)


class VarDec(Node):
    def evaluate(self):
        print("Entrei no VarDec")
        tipo_da_var = self.value.value
        identifier = self.children[0].value.value
        valor = self.children[1][0].evaluate()[1]

        print("AST Aqui o valor do self.value: ", tipo_da_var)
        print("AST Aqui o valor do self.children[0]: ", identifier)
        print("AST Aqui o valor do self.children[1]: ", valor)
        SymbolTable.create(tipo_da_var, identifier, valor)
        print(f"Variável {identifier} criada com sucesso.")
        return valor

class While(Node):
    def evaluate(self):
        for i in self.children[0].evaluate():
            self.children[1].evaluate()


class StringVal(Node):
    def evaluate(self):
        return ("string", str(self.value))
    
class IntVal(Node):
    def evaluate(self):
        return ("lap", int(self.value))

class TupleIntVal(Node):
    def evaluate(self):
        return ("tupleint", tuple(self.value))

class TupleDRSVal(Node):
    def evaluate(self):
        return ("tupledrs", tuple(self.value))
    
class TyreVal(Node):
    def evaluate(self):
        return ("tyre", {self.value[0], self.value[1]})
    
class BoolVal(Node):
    def evaluate(self):
        return ("bool", bool(self.value))
    
class FloatVal(Node):
    def evaluate(self):
        return ("float", float(self.value))
    
class Identifier(Node):
    def evaluate(self):
        return ("identifier", self.value)
    
class IdentifierGet(Node):
    def evaluate(self):
        return SymbolTable.getter(self.value)


class BinOp(Node):

    def evaluate(self):
        # print("Entrei no BinOp")
        # print("AST Aqui o valor do self.value: ", self.value)
        # print("AST Aqui o valor do self.children[0]: ", self.children[0].evaluate())
        # print("AST Aqui o valor do self.children[1]: ", self.children[1].evaluate())
        filho_esquerda = self.children[0].evaluate()
        filho_direita = self.children[1].evaluate()
        if self.value.value == "+":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                soma = filho_esquerda[1] + filho_direita[1]
                print("OLHA O EVALUATE DA SOMA AQUI: ", soma)
                return ("lap", soma)
            else:
                sys.stderr.write("Erro de tipos: operação de soma entre tipos incompatíveis")
        if self.value.value == "-":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                subtracao = filho_esquerda[1] - filho_direita[1]
                return ("lap", subtracao)
            else:
                sys.stderr.write("Erro de tipos: operação de subtração entre tipos incompatíveis")
        if self.value.value == "==":
            if filho_esquerda[1] == filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value.value == ">":
            if filho_esquerda[1] > filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value.value == "<":
            if filho_esquerda[1] < filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value.value == ">=":
            if filho_esquerda[1] >= filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value.value == "<=":
            if filho_esquerda[1] <= filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value.value == "or":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                valor1 = 0
                valor2 = 0
                if filho_esquerda[1] >= 1:
                    valor1 = 1
                if filho_direita[1] >= 1:
                    valor2 = 1
                return ("lap", valor1 or valor2)
            else:
                sys.stderr.write("Erro de tipos: operação de ou entre tipos incompatíveis")
        if self.value.value == "and":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                valor1 = 0
                valor2 = 0
                if filho_esquerda[1] >= 1:
                    valor1 = 1
                if filho_direita[1] >= 1:
                    valor2 = 1
                return ("lap", valor1 and valor2)
            else:
                sys.stderr.write("Erro de tipos: operação de e entre tipos incompatíveis")
    
# class RefVarAtribute(Node):
#     def evaluate(self): # vai receber uma tupla com o nome da variável e o atributo que quer acessar
#         if 
#         return SymbolTable.getter(self.value)