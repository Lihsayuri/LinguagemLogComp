from rply import ParserGenerator
# from lexer import lgfinal
from astling import *
from rply.token import Token

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NEWLINE', 'BEGIN_PROGRAM', 'END_PROGRAM', 'TYRE_TYPE', 'TYRE_STATUS', 'SECTOR',
              'VAR_TYPE', 'LOOP_ON', 'LOOP_OFF', 'SETUP', 'RADIO_ON', 'RADIO_OFF', 'RADIO_CHECK', 'SILENCE', 'COPY', 'CALL',
              'IN', 'LOGICAL', 'THEN', 'NEED', 'OPERATOR', 'BOOLEAN', 'COMMA', 'OPEN_PARENTHESIS', 'CLOSE_PARENTHESIS',
              'OPEN_BRACES', 'CLOSE_BRACES', 'OPEN_BRACKETS', 'CLOSE_BRACKETS', 'IS', 'IDENTIFIER', 'STRING', 'FLOAT', 'INT']
        )
        self.node_while = None
        self.onWhile = False  # Inicializa onWhile como False
        self.structure_node = Structure("structure", [])  # Nó Structure inicial

    def parse(self):
        @self.pg.production('beginning : BEGIN_PROGRAM NEWLINE structure')
        def beginning(p):
            print("Processei o beginning do programa")
            print(self.structure_node.value)
            print(self.structure_node.children)
            return self.structure_node
            # return p
        
        @self.pg.production('structure : END_PROGRAM')
        @self.pg.production('structure : program structure')
        def structure(p):
            print("Processei o program structure, vem coisa aí")
            print("Aqui o p: ", p)
            if len(p) == 2:
                program_node = p[0]  # Nó program

                if isinstance(program_node, Structure):
                    return program_node
                self.structure_node.children.append(program_node)
                return self.structure_node


        @self.pg.production('program : var_declaration')
        @self.pg.production('program : loop')
        @self.pg.production('program : setup')
        @self.pg.production('program : radiocheck')
        @self.pg.production('program : call')
        @self.pg.production('program : LOOP_OFF NEWLINE')
        @self.pg.production('program : RADIO_OFF NEWLINE')
        def program(p):
            print("Processei o program")
            print("Aqui o p: ", p)
            if len(p) == 2 and p[0].gettokentype() == 'LOOP_OFF':
                onWhile = False
                print("Entrei no loop off")
                print("Aqui o node_while: ", self.node_while)
                return self.node_while
            print("Aqui o p[0]: ", p[0])
            return p[0]
        

        @self.pg.production('var_declaration : VAR_TYPE IDENTIFIER IS value NEWLINE')
        def var_declaration(p):
            node_identifier = Identifier(p[1], [])
            # print("VARTYPE AQUIII: ", p[0].value)
            if (p[0].value == 'driver'):
                node_driver = DriverVal(p[3], [])
                node_vardec = VarDec(p[0], [node_identifier, node_driver])
            elif (p[0].value == 'driver_engineer'):
                node_driver_engineer = DriverEngineerVal(p[3], [])
                node_vardec = VarDec(p[0], [node_identifier, node_driver_engineer])
            elif (p[0].value == 'team'):
                node_team = TeamVal(p[3], [])
                node_vardec = VarDec(p[0], [node_identifier, node_team])
            elif (p[0].value == 'grand_prix'):
                node_grand_prix = GrandPrixVal(p[3], [])
                node_vardec = VarDec(p[0], [node_identifier, node_grand_prix])
            else:
                node_vardec = VarDec(p[0], [node_identifier,  p[3]])
                print("Aqui o node_vardec: ", node_vardec)
                print("Aqui o node_vardec.children: ", node_vardec.children)

            if self.onWhile:
                print("Entrei no while no vardec")
                self.node_while.children.append(node_vardec)
                print("Aqui o node_while.children: ", self.node_while.children)
            else:
                print("Entrei no else no vardec")
                return node_vardec
            # return p
        
        @self.pg.production('loop : LOOP_ON race_loop')
        def loop(p):
            self.onWhile = True
            print("loop")
            return self.structure_node  # antes tava sem, agora funcionou
            # return self.structure_node.children.append(self.node_while)
        

        @self.pg.production('race_loop : OPEN_BRACKETS termo CLOSE_BRACKETS NEWLINE')
        def race_loop(p):
            self.node_while = While("while", [])
            self.node_while.children.append(p[1])


        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition var_declaration COPY NEWLINE else') #por enquanto tirei o else do final
        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition call COPY NEWLINE else')
        @self.pg.production('radiocheck : RADIO_CHECK radiocheckcondition IDENTIFIER IS value COPY NEWLINE else')
        def radiocheck(p):
            print("Característica do radiocheck: ", p)
            node_if = If("if", [])
            node_if.children.append(p[1])
            if len(p) == 8:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                node_identifier = Identifier(p[2].value, [p[4]]) 
                node_if.children.append(node_identifier)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                print("Aqui o p[7]: ", p[7])
                if p[7] != None:
                    print("Aqui o p[7] ENTREI AQUIIII: ", p[7])
                    node_if.children.append(p[7])
            else:
                node_if.children.append(p[2])
                if p[5] != None:
                    node_if.children.append(p[5])

            print("Filhos do radiocheck: ", node_if.children)

            
            print("Característica do radiocheck: ", node_if.children)
            return node_if
            # print("Característica do radiocheck: ", p)
        
        @self.pg.production('else : SILENCE var_declaration COPY NEWLINE')
        @self.pg.production('else : SILENCE call COPY NEWLINE')
        @self.pg.production('else : SILENCE IDENTIFIER IS value COPY NEWLINE')
        @self.pg.production('else : ')
        def else_(p):
            # print("Característica do else: ", p)
            if len(p) == 0:
                return None
            else:
                if len(p) == 6:
                    print("Característica do else: ", p)
                    print("Aqui o p[3]: ", p[3])
                    print("Aqui o p[1].value: ", p[1].value)
                    node_identifier = Identifier(p[1].value, [p[3]])
                    return node_identifier
                else:
                    return p[1]
    
        @self.pg.production('radiocheckcondition : IDENTIFIER IN IDENTIFIER THEN')
        @self.pg.production('radiocheckcondition : IDENTIFIER IS value THEN')
        @self.pg.production('radiocheckcondition : IDENTIFIER OPERATOR value THEN')
        def radiocheckcondition(p):
            print("Característica do radiocheckcondition: ", p)
            if isinstance(p[0], Token):
                if p[0].gettokentype() == 'IDENTIFIER':
                    identifier_node = IdentifierGet(p[0].value, [])
                    node_comparison = BinOp(p[1], [identifier_node, p[2]])
   


            print("Aqui o node_comparison.value: ", node_comparison.value)
            print("Aqui o node_comparison.children: ", node_comparison.children)
            return node_comparison
            
                

        ## --------------------------------------------------------------------------------------------------------------------------------
        ## DEFINIÇÕES DE FUNÇÃO
        
        @self.pg.production('setup : SETUP setupfunction')
        def setup(p):
            print("Característica do setup: ", p )
            return p
        

        @self.pg.production('setupfunction : IDENTIFIER NEED VAR_TYPE IDENTIFIER NEWLINE RADIO_ON NEWLINE')
        @self.pg.production('setupfunction : IDENTIFIER NEED VAR_TYPE IDENTIFIER manyidentifiers NEWLINE RADIO_ON NEWLINE')
        def setupfunction(p):
            print("Característica do setupfunction: ",p )
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
        
        ## --------------------------------------------------------------------------------------------------------------------------------
        ## DEFINIÇÃO DE TIPOS DE VARIÁVEIS


        @self.pg.production('tuple_int : OPEN_PARENTHESIS INT COMMA INT CLOSE_PARENTHESIS')
        def tuple_int(p):
            print("Característica da tupla: ", )
            int_node1 = IntVal(p[1].value, [])
            int_node2 = IntVal(p[3].value, [])
            tuple_int_node = TupleIntVal("overtaking", [int_node1, int_node2])
            print("Aqui o tuple_int_node.value: ", tuple_int_node.value)
            print("Aqui o tuple_int_node.children: ", tuple_int_node.children)
            return tuple_int_node

        @self.pg.production('tuple_drs : OPEN_PARENTHESIS SECTOR COMMA INT CLOSE_PARENTHESIS')
        @self.pg.production('tuple_drs : OPEN_PARENTHESIS SECTOR COMMA SECTOR COMMA INT CLOSE_PARENTHESIS')
        @self.pg.production('tuple_drs : OPEN_PARENTHESIS SECTOR COMMA SECTOR COMMA SECTOR COMMA INT CLOSE_PARENTHESIS')
        def tuple_drs(p):
            print("Característica da tupla: ", p)
            if len(p) == 5:
                tuple_drs_node = TupleDRSVal((p[1], IntVal(p[3], [])), [])
            elif len(p) == 7:
                tuple_drs_node = TupleDRSVal((p[1], p[3], IntVal(p[5], [])), [])
            elif len(p) == 9:
                tuple_drs_node = TupleDRSVal((p[1], p[3], p[5], IntVal(p[7], [])), [])

            print("Aqui o tuple_drs_node.value: ", tuple_drs_node.value)
            print("Aqui o tuple_drs_node.children: ", tuple_drs_node.children)
            return tuple_drs_node


        @self.pg.production('tyre : OPEN_BRACES TYRE_TYPE COMMA TYRE_STATUS CLOSE_BRACES')
        def tyre(p):
            print("Característica do tyre: ", p)
            TyreVal_node = TyreVal((p[1], p[3]), [])
            print("Aqui o TyreVal_node.value: ", TyreVal_node.value)
            print("Aqui o TyreVal_node.children: ", TyreVal_node.children)
            return TyreVal_node
        
        @self.pg.production('manyidentifiers : COMMA VAR_TYPE IDENTIFIER')
        @self.pg.production('manyidentifiers : COMMA VAR_TYPE IDENTIFIER manyidentifiers')
        def manyidentifiers(p):
            print("Característica do manyidentifiers: ", p)
            return p
        
        @self.pg.production('termo : IDENTIFIER')
        # @self.pg.production('termo : REF_VAR_ATRIBUTE')
        @self.pg.production('termo : INT')
        def termo(p):
            print("Característica do termo: ", p)
            if p[0].gettokentype() == 'INT':
                return IntVal(p[0].value, [])
            if p[0].gettokentype() == 'IDENTIFIER':
                return IdentifierGet(p[0].value, [])
        
        @self.pg.production('operacao : termo')
        @self.pg.production('operacao : operacao OPERATOR termo')
        @self.pg.production('operacao : operacao LOGICAL termo')
        def operacao(p):
            if len(p) == 1:
                return p[0]
            else:
                node_binop = BinOp(p[1], [p[0], p[2]])
                print("Característica da operação: ", p)
                print("Aqui o node_binop.value: ", node_binop.value)
                print("Aqui o node_binop.children: ", node_binop.children)

                return node_binop


        @self.pg.production('value : STRING')
        @self.pg.production('value : FLOAT')
        @self.pg.production('value : BOOLEAN')
        @self.pg.production('value : tuple_int')
        @self.pg.production('value : tuple_drs')
        @self.pg.production('value : tyre')
        # @self.pg.production('value : tyre_set')
        @self.pg.production('value : operacao')
        @self.pg.production('value : TYRE_STATUS')
        @self.pg.production('value : TYRE_TYPE')
        def value(p):
            print("Característica do value: ", p[0])
            if isinstance(p[0], Token) :
                print("Aqui o p[0].gettokentype(): ", p[0].gettokentype())
                if p[0].gettokentype() == 'STRING':
                    # print("Aquii o StringVal : ", p[0].value)
                    # return StringVal(p[0].value, [])
                    return p[0].value
                if p[0].gettokentype() == 'FLOAT':
                    print("Aquii o FloatVal : ", p[0].value)
                    return FloatVal(p[0].value, [])
                if p[0].gettokentype() == 'BOOLEAN':
                    print("Aquii o BooleanVal : ", p[0].value)
                    return BoolVal(p[0].value, [])
                return p[0]
            
            print("Aqui o node.value: ", p)
            return p[0]


    
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()