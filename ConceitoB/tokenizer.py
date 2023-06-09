import sys
lista_palavras_reservadas = ["START", "FINISH", "radio_check", "no_response",  "EngineOn", "EngineOff", "driver", "tyre", "lap", "and", "or", "is", "equals", "not", "SetUp", "need", "checked", "call", "then","Radio_on", "Radio_off", "Copy!", "soft", "medium", "hard", "fresh", "used" ]   # na PI vai pedir versão 2.1

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, source, position):
        self.source = source
        self.position = position
        self.next = Token(None, None)


    def selectNext(self):
        numero = ""
        while(len(self.source)!=self.position):
            if self.source[self.position].isnumeric():
                numero += self.source[self.position]
                self.position += 1
                while(len(self.source)!=self.position):
                    if self.source[self.position].isnumeric():
                        numero += self.source[self.position]
                        self.position += 1
                    else:
                        self.next = Token("INT", numero)
                        return
                self.next = Token("INT", numero)
                return
            elif self.source[self.position] == '+' :
                self.next = Token("PLUS", 0)
                self.position += 1
                return 
            elif self.source[self.position] == '-' :
                self.next = Token("MINUS", 0)
                self.position += 1
                return 
            elif self.source[self.position] == '.' :
                self.next = Token("DOT", 0)
                self.position += 1
                return
            elif self.source[self.position] == '(':
                self.next = Token("OPENPAR", 0)
                self.position += 1
                return
            elif self.source[self.position] == ')':
                self.next = Token("CLOSEPAR", 0)
                self.position += 1
                return
            elif self.source[self.position] == '[':
                self.next = Token("OPENBRA", 0)
                self.position += 1
                return
            elif self.source[self.position] == ']':
                self.next = Token("CLOSEBRA", 0)
                self.position += 1
                return
            elif self.source[self.position] == '{':
                self.next = Token("OPENCURLYBRA", 0)
                self.position += 1
                return
            elif self.source[self.position] == '}':
                self.next = Token("CLOSECURLYBRA", 0)
                self.position += 1
                return
            elif self.source[self.position] == '\n':
                self.position += 1
                self.next = Token("NEWLINE", 0)
                return
            elif self.source[self.position] == '=':
                if self.source[self.position+1] == ">":
                    self.next = Token("ARROW", 0)
                    self.position += 2
                    return
                else:
                    sys.stderr.write("Erro: caracter inválido")
            elif self.source[self.position] == ',':
                self.position += 1
                self.next = Token("COMMA", 0)
                return
            elif self.source[self.position] == '\'':
                if self.source[self.position+1] == '\'':
                    self.next = Token("STRING", '')
                    self.position += 2
                    return
                else:
                    self.position += 1
                    string = ''
                    while(self.source[self.position] != '\''):
                        string += self.source[self.position]
                        self.position += 1
                    self.next = Token("STRING", string)
                    self.position += 1
                    return

            elif self.source[self.position] == '>':
                if self.source[self.position+1] == '>':
                    self.next = Token("INDICA", 0)
                    self.position += 2
                    return
                self.next = Token("GREATER", 0)
                self.position += 1
                return
            elif self.source[self.position] == '<':
                self.next = Token("LESS", 0)
                self.position += 1
                return
            elif self.source[self.position].isalpha():
                palavra = ""
                palavra += self.source[self.position]
                self.position += 1
                while(len(self.source)!=self.position):
                    if self.source[self.position].isalpha() or self.source[self.position].isnumeric() or self.source[self.position] == "_" or self.source[self.position] == "!" :
                        palavra += self.source[self.position]
                        self.position += 1
                    else:
                        # print(palavra)
                        # print(palavra in lista_palavras_reservadas)
                        if palavra in lista_palavras_reservadas:
                            if palavra == "lap":
                                self.next = Token("TYPE", "lap")
                            elif palavra == "driver":
                                self.next = Token("TYPE", "driver")
                            elif palavra == "tyre":
                                self.next = Token("TYPE", "tyre")
                            elif palavra == "soft":
                                self.next = Token("TYRE_TYPE", "soft")
                            elif palavra == "medium":
                                self.next = Token("TYRE_TYPE", "medium")
                            elif palavra == "hard":
                                self.next = Token("TYRE_TYPE", "hard")
                            elif palavra == "fresh":
                                self.next = Token("TYRE_STATE", "fresh")
                            elif palavra == "used":
                                self.next = Token("TYRE_STATE", "used")
                            elif palavra == "or":
                                self.next = Token("OR", 0)
                            elif palavra == "and":
                                self.next = Token("AND", 0)
                            elif palavra == "is":
                                self.next = Token("EQUAL", 0)  
                            elif palavra == "equals":
                                self.next = Token("EQUAL_EQUAL", 0)                           
                            else:
                                self.next = Token(palavra.upper(), 0)
                            return
                        else:
                            self.next = Token("IDENTIFIER", palavra)
                            return
                if palavra in lista_palavras_reservadas:
                    self.next = Token(palavra.upper(), 0)
                    return
                else:
                    self.next = Token("IDENTIFIER", palavra)
                    return   
            elif self.source[self.position] == " " :
                self.position += 1
            else:
                sys.stderr.write("Você digitou um caracter inválido")
                sys.exit(1)
        
        # self.next = Token("EOF", 0)
        return
    
    def peek(self):
        saved_position = self.position
        saved_next = self.next
        
        # Obtenha o próximo token
        self.selectNext()
        next_token = self.next
        
        # Restaure a posição e o próximo token original
        self.position = saved_position
        self.next = saved_next
        
        return next_token


#teste a classe Tokenizer
# def run(file):
#     source = open(file, 'r')
#     source = source.read()
#     position = 0
#     tokenizer = Tokenizer(source, position)
#     while(tokenizer.next.type != "FINISH"):
#         tokenizer.selectNext()
#         print(tokenizer.next.type, tokenizer.next.value)


# if __name__ == "__main__":
#     run(sys.argv[1])