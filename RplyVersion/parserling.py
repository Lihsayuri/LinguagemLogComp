from rply import ParserGenerator
# from lexer import lgfinal
from astling import Node, Structure, VarDec, StringVal, While


node_while = While("while", [])
onWhile = False

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NEWLINE', 'BEGIN_PROGRAM', 'END_PROGRAM', 'TYRE_TYPE', 'TYRE_STATUS', 'SECTOR', 'REF_VAR_ATRIBUTE', 'ATRIBUTE',
              'VAR_TYPE', 'LOOP_ON', 'LOOP_OFF', 'SETUP', 'RADIO_ON', 'RADIO_OFF', 'RADIO_CHECK', 'SILENCE', 'COPY', 'CALL',
              'IN', 'LOGICAL', 'THEN', 'NEED', 'OPERATOR', 'BOOLEAN', 'COMMA', 'OPEN_PARENTHESIS', 'CLOSE_PARENTHESIS',
              'OPEN_BRACES', 'CLOSE_BRACES', 'OPEN_BRACKETS', 'CLOSE_BRACKETS', 'IS', 'IDENTIFIER', 'STRING', 'FLOAT', 'INT']
        )

    def parse(self):
        @self.pg.production('beginning : BEGIN_PROGRAM NEWLINE structure')
        def beginning(p):
            print("Processei o beginning do programa")
            return p
        
        @self.pg.production('structure : END_PROGRAM')
        @self.pg.production('structure : program structure')
        def structure(p):
            print("Processei o program structure, vem coisa aí")
            if len(p) == 1:
                print("Entrei no else do structure")
                return Structure(p[0], [])  # Retorna um nó Structure com os filhos de p[1]
            else:
                print("Entrei no else do structure")
                structure_node = Node(p[1], [])  # Nó Structure atual
                program_node = p[0]  # Nó program
                structure_node.children.append(program_node)  # Adiciona o nó program como filho do nó Structure
                print("Aqui o structure_node.value: ", structure_node.value)
                print("Aqui o structure_node.children: ", structure_node.children)
                return structure_node

        @self.pg.production('program : var_declaration')
        @self.pg.production('program : loop')
        @self.pg.production('program : setup')
        @self.pg.production('program : radiocheck')
        @self.pg.production('program : call')
        @self.pg.production('program : LOOP_OFF NEWLINE')
        @self.pg.production('program : RADIO_OFF NEWLINE')
        def program(p):
            print("Entrei nas ramificações do program")
            if p[0] == "LOOP_OFF":
                onWhile = False
                return node_while
            return p # Retorna um nó Structure sem filhos

        @self.pg.production('var_declaration : VAR_TYPE IDENTIFIER IS value NEWLINE')
        def var_declaration(p):
            node_vardec = VarDec(p[0], [p[1],  p[3]])
            # p[3].evaluate()
            print("Aqui o node_vardec.value: ", node_vardec.value)
            print("Aqui o node_vardec.children: ", node_vardec.children)
            if onWhile:
                node_while.children.append(node_vardec)
            return node_vardec
            # return p
        
        @self.pg.production('loop : LOOP_ON race_loop')
        def loop(p):
            onWhile = True
            node_while = While("while", [])
            print("loop")
            return p
        
        @self.pg.production('race_loop : OPEN_BRACKETS INT CLOSE_BRACKETS NEWLINE')
        @self.pg.production('race_loop : OPEN_BRACKETS IDENTIFIER CLOSE_BRACKETS NEWLINE')
        def race_loop(p):
            print("Característica do race_loop: ", p)
            node_while.children.append(p[1])

        @self.pg.production('setup : SETUP setupfunction')
        def setup(p):
            print("Característica do setup: ", p )
            return p
        

        @self.pg.production('setupfunction : IDENTIFIER NEED VAR_TYPE IDENTIFIER NEWLINE RADIO_ON NEWLINE')
        @self.pg.production('setupfunction : IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers NEWLINE RADIO_ON NEWLINE')
        def setupfunction(p):
            print("Característica do setupfunction: ",p )
            return p
        
        
        @self.pg.production('ident_or_ref : IDENTIFIER')
        @self.pg.production('ident_or_ref : REF_VAR_ATRIBUTE')
        def ident_or_ref(p):
            print("Característica do ident_or_ref: ", p )
            return p
        

        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition var_declaration COPY NEWLINE else')
        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition call COPY NEWLINE else')
        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition radiocheckcondition COPY NEWLINE else')
        def radiocheck(p):
            print("Característica do radiocheck: ", p)
            return p
        
        @self.pg.production('else : SILENCE radiocheckcondition COPY NEWLINE')
        @self.pg.production('else : ')
        def else_(p):
            print("Característica do else: ", p)
            return p
        
        @self.pg.production('radiocheckcondition : ident_or_ref IN ident_or_ref manyconditions')
        @self.pg.production('radiocheckcondition : ident_or_ref IS value manyconditions')
        @self.pg.production('radiocheckcondition : ident_or_ref OPERATOR value manyconditions')
        def radiocheckcondition(p):
            print("Característica do radiocheckcondition: ", p)
            return p
        
        @self.pg.production('manyconditions : LOGICAL ident_or_ref IN ident_or_ref manyconditions')
        @self.pg.production('manyconditions : LOGICAL ident_or_ref IS value manyconditions')
        @self.pg.production('manyconditions : LOGICAL ident_or_ref OPERATOR value manyconditions')
        @self.pg.production('manyconditions : THEN')
        @self.pg.production('manyconditions : ')
        def manyconditions(p):
            print("Característica do manyconditions: ", p)
            return p
        
        @self.pg.production('call : CALL callsetup')
        def call(p):
            print("Característica do call: ",p )
            return p
        
        @self.pg.production('callsetup : IDENTIFIER NEED VAR_TYPE IDENTIFIER')
        @self.pg.production('callsetup : IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers')
        def callsetup(p):
            print("Característica do callsetup: ",p)
            return p


        @self.pg.production('tuple_int : OPEN_PARENTHESIS INT COMMA INT CLOSE_PARENTHESIS')
        def tuple_int(p):
            print("Característica da tupla: ", )
            return p
        
        @self.pg.production('many_sector : COMMA SECTOR')
        @self.pg.production('many_sector : many_sector COMMA SECTOR') 
        def many_sector(p):
            print("Característica do many_sector: ",p )
            return p


        @self.pg.production('tuple_drs : OPEN_PARENTHESIS SECTOR COMMA INT CLOSE_PARENTHESIS')
        @self.pg.production('tuple_drs : OPEN_PARENTHESIS SECTOR many_sector COMMA INT CLOSE_PARENTHESIS')
        def tuple_drs(p):
            print("Característica da tupla: ", p)
            return p


        @self.pg.production('tyre : OPEN_BRACES TYRE_TYPE COMMA TYRE_STATUS CLOSE_BRACES')
        def tyre(p):
            print("Característica do tyre: ", p)
            return p
        
        @self.pg.production('tyre_set : OPEN_BRACES tyre CLOSE_BRACES')
        @self.pg.production('tyre_set : OPEN_BRACES tyre manytires CLOSE_BRACES')
        def tyre_set(p):
            print("Característica do tyre_set: ", p)
            return p
        
        @self.pg.production('manytires : COMMA tyre')
        @self.pg.production('manytires : COMMA tyre manytires')
        def manytires(p):
            print("Característica do manytires: ", p)
            return p
        
        @self.pg.production('manyidentifiers : COMMA VAR_TYPE IDENTIFIER')
        @self.pg.production('manyidentifiers : COMMA VAR_TYPE IDENTIFIER manyidentifiers')
        def manyidentifiers(p):
            print("Característica do manyidentifiers: ", p)
            return p
        
        @self.pg.production('termo : IDENTIFIER')
        @self.pg.production('termo : REF_VAR_ATRIBUTE')
        @self.pg.production('termo : INT')
        def termo(p):
            print("Característica do termo: ", p)
            return p
        
        @self.pg.production('operacao : termo')
        @self.pg.production('operacao : operacao OPERATOR termo')
        def operacao(p):
            print("Característica da operação: ", p)
            return p



        @self.pg.production('value : STRING')
        @self.pg.production('value : FLOAT')
        @self.pg.production('value : BOOLEAN')
        @self.pg.production('value : tuple_int')
        @self.pg.production('value : tuple_drs')
        @self.pg.production('value : tyre')
        @self.pg.production('value : tyre_set')
        @self.pg.production('value : operacao')
        @self.pg.production('value : TYRE_STATUS')
        @self.pg.production('value : TYRE_TYPE')
        def value(p):
            print("Característica do value: ", p)
            if p[0].gettokentype() == 'STRING':
                print("Aquii o StringVal : ", p[0].value)
                return StringVal(p[0].value, [])
            # return StringVal()
            return p


    
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()