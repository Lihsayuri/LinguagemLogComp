import sys

class FuncTable:
    def __init__(self):
        self.trocas_pneu = 0
        self.table = {}

    def prints_create(self, value, type):
        if hasattr(value, '__len__'):
            if type == "driver":
                print("Engenheiro : Radio check para o piloto ", value)
            if type == "lap":
                print("Engenheiro : Lap check para o piloto ", value)
            if type == "tyre":
                if len(value) == 2:
                    print("Engenheiro : Definindo pneu do tipo: " , value[0], "e no estado ", value[1], "para o piloto")
        elif type == "lap":
            print("Engenheiro : Lap check para o piloto ", value)

    def prints_setter(self, valor_antigo, variable, value):
        if hasattr(value, '__len__'):
            if value[0] == "driver":
                if valor_antigo == value[1]:
                    print("James : Opa ", value[1], " tudo certo por aqui! Segue o jogo!")
                else:
                    print("James : Câmbio, aqui é o James! Trocando ", variable, " para", value[1])
            if value[0] == "lap":
                if valor_antigo == value[1]:
                    print("James : Continuamos na volta ", value[1], " . Tenha paciência!")
                else: 
                    print("James : Alô! Estamos na volta ", value[1], " . Segura a posição!")
            if value[0] == "tyre":
                if valor_antigo == value[1]:
                    print("James : Pneu ", value[1][0], " no estado ", value[1][1], " continua na pista!")
                else:
                    self.trocas_pneu += 1
                    print("Binotto : Estratégia A é o foco! Trocando o pneu para o tipo", value[1][0], "e no estado", value[1][1], "na troca de número", self.trocas_pneu)

    def create(self, type, variable, value):
        if variable not in self.table:
            self.table[variable] = (type, value)
            self.prints_create(value, type)
        else:
            sys.stderr.write("Erro: variável já declarada")

    def getter(self,variable):
        return self.table[variable]
    
    def setter(self, variable, value):
        if self.table[variable][0] == value[0]:
            valor_antigo = self.table[variable][1]
            self.prints_setter(valor_antigo, variable, value)
            self.table[variable] =  value
        else:
            sys.stderr.write("Erro de tipos: atribuição de valor incompatível com o tipo da variável")

class SymbolTable:
    def __init__(self):
        self.trocas_pneu = 0
        self.table = {}


    def create(self,type, variable, value):
        if variable not in self.table:
            self.table[variable] = (type, value)
            # self.prints_create(value, type)
        else:
            sys.stderr.write("Erro: variável já declarada")

    def getter(self, variable):
        return self.table[variable]
    
    def setter(self, variable, value):
        if self.table[variable][0] == value[0]:
            self.table[variable] =  value
        else:
            sys.stderr.write("Erro de tipos: atribuição de valor incompatível com o tipo da variável")
