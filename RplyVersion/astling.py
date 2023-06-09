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
        print("Aquiii a symbol table: ", SymbolTable.table)
        print("Aquiii a symbol table: ", variable, value)

        if value[0] == 'string':
            tipo = SymbolTable.table[variable][0]
            SymbolTable.table[variable] =  (tipo, value[1])
        elif SymbolTable.table[variable][0] == value[0]:
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
            if child != None:
                filho = child.evaluate()
                print("AST Aqui o valor do child: ", filho)


class VarDec(Node):
    def evaluate(self):
        print("Entrei no VarDec")
        print("AST Aqui o valor do self.value: ", self.value.value, self.children[0].value.value)
        print("AST Aqui o valor do self.children: ", self.children[1].evaluate()[1])
        tipo_da_var = self.value.value
        identifier = self.children[0].value.value
        valor = self.children[1].evaluate()[1]

        print("AST Aqui o valor do self.value: ", tipo_da_var)
        print("AST Aqui o valor do self.children[0]: ", identifier)
        print("AST Aqui o valor do self.children[1]: ", valor)
        SymbolTable.create(tipo_da_var, identifier, valor)
        print(f"Variável {identifier} criada com sucesso.")
        return valor

class While(Node):
    def evaluate(self):
        print("Entrei no While")
        print("AST Aqui o valor do self.value: ", self.value)
        print("AST Aqui o valor do self.children[0]: ", self.children[0])
        len_children = len(self.children)
        print("AST Aqui o valor do len_children: ", len_children)
        if len_children == 1:
            print(self.children[0].evaluate()[1])
            for i in range(self.children[0].evaluate()[1]):
                print("AST Aqui o valor do i: ", i)
        else:
            for i in range(self.children[0].evaluate()[1]):
                print("AST Aqui o valor do i ", i)
                self.children[1].evaluate()

class If(Node):
    def evaluate(self):
        print("Entrei no If")
        print("AST Aqui o valor do self.value: ", self.value)
        print("AST Aqui o valor do self.children[0]: ", self.children[0].value , self.children[0].children)
        print("AST Aqui o valor do self.children[1]: ", self.children[1])
        print(self.children)
        if self.children[0].evaluate()[1]:
            self.children[1].evaluate()
        else:
            if len(self.children) == 3:
                print("AST Aqui o valor do self.children[2]: ", self.children[2])
                print("AST Aqui o valor do self.children[2]: ", self.children[2].value)
                print("AST Aqui o valor do self.children[2]: ", self.children[2].children)
                self.children[2].evaluate()
    
class DriverVal(Node):
    def evaluate(self):
        return ("driver", str(self.value))

class DriverEngineerVal(Node):
    def evaluate(self):
        return ("driver_engineer", str(self.value))
    
class TeamVal(Node):
    def evaluate(self):
        return ("team", str(self.value))
    
class GrandPrixVal(Node):
    def evaluate(self):
        return ("grand_prix", str(self.value))
    
class IntVal(Node):
    def evaluate(self):
        print("Entrei no IntVal")
        print("AST Aqui o valor do self.value: ", self.value)
        return ("lap", int(self.value))

class TupleIntVal(Node):
    def evaluate(self):
        print("Entrei no TupleIntVal")
        print("AST Aqui o valor do self.value: ", self.value)
        print("AST Aqui o valor do self.children[0]: ", self.children[0].evaluate()[1])
        print("AST Aqui o valor do self.children[1]: ", self.children[1].evaluate()[1])
        return ("overtaking", (self.children[0].evaluate()[1], self.children[1].evaluate()[1]))

class TupleDRSVal(Node):
    def evaluate(self):
        return ("tupledrs", tuple(self.value))
    
class TyreVal(Node):
    def evaluate(self):
        return ("tyre", {self.value[0], self.value[1]})
    
class BoolVal(Node):
    def evaluate(self):
        return ("expected_sc", bool(self.value))
    
class FloatVal(Node):
    def evaluate(self):
        print("Entrei no FloatVal")
        print("AST Aqui o valor do self.value: ", self.value)
        return ("rain_probability", float(self.value))
    
class Identifier(Node):
    def evaluate(self):
        print("IDENTIFIER: ", self.value)
        print("IDENTIFIER: ", self.children[0])
        print("IDENTIFIER: ", type(self.children[0]))

        if isinstance(self.children[0], str): 
            SymbolTable.setter(self.value, ('string', self.children[0]))
        else:
            SymbolTable.setter(self.value, self.children[0].evaluate())
            
    
class IdentifierGet(Node):
    def evaluate(self):
        return SymbolTable.getter(self.value)


class BinOp(Node):

    def evaluate(self):
        filho_esquerda = self.children[0].evaluate()
        filho_direita = self.children[1].evaluate()
        print("Olha o evaluate do filho 0 no binop: ", filho_esquerda)
        print("Olha o evaluate do filho 1 no binop: ", filho_direita)
        if self.value.value == "+":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                soma = filho_esquerda[1] + filho_direita[1]
                print("OLHA O EVALUATE DA SOMA AQUI: ", soma)
                return (filho_esquerda[0], soma)
            else:
                sys.stderr.write("Erro de tipos: operação de soma entre tipos incompatíveis ou que não podem ser somados")
        if self.value.value == "-":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                subtracao = filho_esquerda[1] - filho_direita[1]
                return (filho_esquerda[0], subtracao)
            else:
                sys.stderr.write("Erro de tipos: operação de subtração entre tipos incompatíveis ou que não podem ser subtraidos")
        if self.value.value == "is":
            print("OLHA O EVALUATE DA COMPARAÇÃO AQUI: ", filho_esquerda[1] == filho_direita[1])
            if (filho_esquerda[0] == filho_direita[0]) and (filho_esquerda[1] == filho_direita[1]):
                return (filho_esquerda[0], 1)
            else:
                return (filho_esquerda[0], 0)
        if self.value.value == "in":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "overtaking"):
                if min(filho_direita[1]) <= filho_esquerda[1] <= max(filho_direita[1]):
                    return ("lap", 1)
                else:
                    return ("lap", 0)
        if self.value.value == ">":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                if filho_esquerda[1] > filho_direita[1]:
                    return ("lap", 1)
                else:
                    return ("lap", 0)
        if self.value.value == "<":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                if filho_esquerda[1] < filho_direita[1]:
                    return ("lap", 1)
                else:
                    return ("lap", 0)
        if self.value.value == ">=":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                if filho_esquerda[1] >= filho_direita[1]:
                    return ("lap", 1)
                else:
                    return ("lap", 0)
        if self.value.value == "<=":
            if (filho_esquerda[0] == "lap" and filho_direita[0] == "lap") or (filho_esquerda[0] == "rain_probability" and filho_direita[0] == "rain_probability"):
                if filho_esquerda[1] <= filho_direita[1]:
                    return ("lap", 1)
                else:
                    return ("lap", 0)
        if self.value.value == "or":
            if filho_esquerda[0] == "lap" or filho_direita[0] == "lap":
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