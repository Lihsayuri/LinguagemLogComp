from rply import LexerGenerator

lg = LexerGenerator()


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # NewLine
        self.lexer.add('NEWLINE', r'\n' )
        # Begin Program
        self.lexer.add('BEGIN_PROGRAM', r'ITS LIGHTS OUT AND AWAY WE GO')
        # End Program
        self.lexer.add('END_PROGRAM', r'CHECKRED FLAG')

        # TYRE_TYPE soft|hard|medium
        self.lexer.add('TYRE_TYPE', r'soft|hard|medium')

        # TYRE_STATUS fresh|lil_used|too_used
        self.lexer.add('TYRE_STATUS', r'fresh|lil_used|too_used')

        # SECTOR sector1|sector2|sector3
        self.lexer.add('SECTOR', r'sector1|sector2|sector3')

        # self.lexer.add('REF_VAR_ATRIBUTE', r'(type|status|availability|sector|start_lap|end_lap)(of\.[a-zA-Z_][a-zA-Z0-9_]*)+')

        # Atribute - pode ser qualquer um desses : type|status|availability|sector|start_lap|end_lap
        # self.lexer.add('ATRIBUTE', r'type|status|availability|sector|start_lap|end_lap')

         # Var Type: driver|driver_engineer|team|grand_prix|expected_sc|rain_probability|drs_usage|aggressive_overtaking|conservative_overtaking|sets_of_tyres|lap|tyre
        self.lexer.add('VAR_TYPE', r'driver_engineer|driver|team|grand_prix|expected_sc|rain_probability|drs_usage|overtaking|sets_of_tyres|lap|tyre')

        # Loop On: EngineOn
        self.lexer.add('LOOP_ON', r'EngineOn')

        # Loop Off: EngineOff
        self.lexer.add('LOOP_OFF', r'EngineOff')

        # Setup: SetUp
        self.lexer.add('SETUP', r'SetUp')

        # RADIO_ON: Radio_on
        self.lexer.add('RADIO_ON', r'Radio_on')

        # RADIO_OFF: Radio_off
        self.lexer.add('RADIO_OFF', r'Radio_off')

        # RADIO_CHECK : radio_check
        self.lexer.add('RADIO_CHECK', r'radio_check')

        # SILENCE: no_response >>
        self.lexer.add('SILENCE', r'no_response >>')

        # COPY: -Copy!
        self.lexer.add('COPY', r'-Copy!')

        # CALL: call
        self.lexer.add('CALL', r'call')

        # IN: in
        self.lexer.add('IN', r'in')

        # LOGICAL:and|or
        self.lexer.add('LOGICAL', r'and|or')

        # THEN: then >>
        self.lexer.add('THEN', r'then >>')

        # NEED: need
        self.lexer.add('NEED', r'need')

        # OPERATOR "+"|"-"|">="|"<="|">"|"<"
        self.lexer.add('OPERATOR', r'\+|\-|\>=|\<=|\>|\<|\==')


        # BOOLEAN True|False 
        self.lexer.add('BOOLEAN', r'True|False')

        # COMMA ","
        self.lexer.add('COMMA', r'\,')

        # OPEN_PARENTHESIS "("
        self.lexer.add('OPEN_PARENTHESIS', r'\(')

        # CLOSE_PARENTHESIS ")"
        self.lexer.add('CLOSE_PARENTHESIS', r'\)')

        # { OPEN_BRACES
        self.lexer.add('OPEN_BRACES', r'\{')

        # } CLOSE_BRACES
        self.lexer.add('CLOSE_BRACES', r'\}')

        # [ OPEN_BRACKETS
        self.lexer.add('OPEN_BRACKETS', r'\[')

        # ] CLOSE_BRACKETS
        self.lexer.add('CLOSE_BRACKETS', r'\]')

        # is IS
        self.lexer.add('IS', r'is')

        # # Identifier : [a-zA-Z_][a-zA-Z0-9_]*
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # \'([^\\\n]|(\\.))*\'    { printf("STRING: %s\n", yytext); return STRING; }
        self.lexer.add('STRING', r'\'([^\\\n]|(\\.))*\'')

        # {NUMBER}+[.]{NUMBER}+   { printf("FLOAT: %s \n", yytext); return FLOAT; }
        self.lexer.add('FLOAT', r'\d+[.]\d+')
        #{NUMBER}+               { printf("INT: %s \n", yytext); return INT; }
        self.lexer.add('INT', r'\d+')

        # Ignore spaces
        self.lexer.ignore(r'[ \t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()