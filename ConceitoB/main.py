import sys
import re
from tokenizer import *
from tables import *
from parser_ import *

class PrePro:
    def filter(source):
        source = re.sub(r"#.*\n", "\n", source)  # remove comentários
        source = re.sub(r"#.*", "", source)  # remove linhas em branco
        return source
    
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def evaluate(self, funcTable, symbolTable):
        pass

class UnOp(Node):
    def evaluate(self, symbolTable):
        if self.children[0].evaluate(symbolTable)[0] == "lap":
            if self.value == "MINUS":
                return ("lap", -self.children[0].evaluate(symbolTable)[1])
            elif self.value == "NOT":
                return ("lap", not self.children[0].evaluate(symbolTable)[1]) #pega o filho da esquerda, faz o evaluate e pega o valor
            elif self.value == "PLUS":
                return ("lap", self.children[0].evaluate(symbolTable)[1])
        else:
            sys.stderr.write("Erro de tipos: operação unária entre tipos incompatíveis")
            sys.exit(1)

class BinOp(Node):

    def evaluate(self, symbolTable):
        filho_esquerda = self.children[0].evaluate(symbolTable)
        filho_direita = self.children[1].evaluate(symbolTable)
        if self.value == "PLUS":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                return ("lap", (filho_esquerda[1] + filho_direita[1]))
            else:
                sys.stderr.write("Erro de tipos: operação de soma entre tipos incompatíveis")
        if self.value == "MINUS":
            if filho_esquerda[0] == "lap" and filho_direita[0] == "lap":
                return ("lap", filho_esquerda[1] - filho_direita[1])
            else:
                sys.stderr.write("Erro de tipos: operação de subtração entre tipos incompatíveis")
        if self.value == "EQUAL_EQUAL":
            if filho_esquerda[1] == filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value == "GREATER":
            if filho_esquerda[1] > filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value == "LESS":
            if filho_esquerda[1] < filho_direita[1]:
                return ("lap", 1)
            else:
                return ("lap", 0)
        if self.value == "OR":
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
        if self.value == "AND":
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
        
class LapVal(Node):
    def evaluate(self, symbolTable):
        return ("lap", int(self.value))
    
class StringVal(Node):
    def evaluate(self, symbolTable):
        return ("String", self.value)
    
class TyreVal(Node):
    def evaluate(self, symbolTable):
        return ("tyre", [self.children[0], self.children[1]])
    
class NoOp(Node):
    def evaluate(self, symbolTable):
        pass 

class Assign(Node):
    def evaluate(self, symbolTable):
        symbolTable.setter(self.children[0].value, self.children[1].evaluate(symbolTable))

class VarDec(Node):
    def evaluate(self, symbolTable):
        if len(self.children) == 1:
            if self.value == "lap":
                symbolTable.create(self.value, self.children[0].value, 0)
            elif self.value == "tyre" or self.value == "driver":
                symbolTable.create(self.value, self.children[0].value, "")
        else:
            if self.value == "lap":
                symbolTable.create(self.value, self.children[0].value, self.children[1].evaluate(symbolTable)[1])
            elif self.value == "driver":
                symbolTable.create(self.value, self.children[0].value, self.children[1].evaluate(symbolTable)[1])
            elif self.value == "tyre":
                symbolTable.create(self.value, self.children[0].value, self.children[1].evaluate(symbolTable)[1])


class FuncDec(Node):
    def evaluate(self, funcTable):
        funcTable.create(self.value, self.children[0].value, self)

class FuncCall(Node):

    def evaluate(self, funcTable):
        node_funcao = funcTable.getter(self.value) #retorna a tupla com o nome e o children
        new_symbol_table = SymbolTable()
        iden, *args, block = node_funcao[1].children

        filhos_call = self.children #filhos do funcCall
        if len(*args) != len(filhos_call):
            sys.stderr.write(f"Erro de sintaxe: número de argumentos não corresponde ao número de parâmetros da função '{self.value}'")

        for var_dec, filho_call in zip(*args, filhos_call):
            var_dec.evaluate(new_symbol_table)   # a gente da evaluate no vardec que são as variaveis da funcaopara saber o tipo e o nome e o filho_call é o que passei na chamada da função
            new_symbol_table.setter(var_dec.children[0].value, filho_call.evaluate(funcTable))


        (type, value) = block.evaluate(new_symbol_table)

        if type != iden.evaluate(funcTable)[0]:
            sys.stderr.write(f"Erro de tipos: tipo de retorno da função '{self.value}' não corresponde ao tipo declarado")

        # print("value: ", value)
        # print("type: ", type)
        
        return (type, value)

class Return(Node):
    def evaluate(self, symbolTable):
        return self.children[0].evaluate(symbolTable)


class Identifier(Node):
    def evaluate(self, symbolTable):
        return symbolTable.getter(self.value)
    
    
class Block(Node):
    def evaluate(self, symbolTable):
        for child in self.children:
            valor = child.evaluate(symbolTable)
            # print("valor: ", valor)
            if valor is not None:
                return valor

class While(Node):
    def evaluate(self, symbolTable):
        for i in range(self.children[0].evaluate(symbolTable)[1], self.children[1].evaluate(symbolTable)[1]):
            symbolTable.setter(self.children[0].value, ("lap", i))
            self.children[2].evaluate(symbolTable)
            

class If(Node):
    def evaluate(self, symbolTable):
        if self.children[0].evaluate(symbolTable)[1]:
            self.children[1].evaluate(symbolTable)
        else:
            if len(self.children) == 3:
                self.children[2].evaluate(symbolTable)

if __name__ == "__main__":
    # argv1 vai ser nome do arquivo e nao travar a extensão .
    with open(sys.argv[1], "r") as file:
        code = file.read()
    
    Parser.run(code)


