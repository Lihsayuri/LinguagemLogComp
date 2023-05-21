
from parserling import Parser
from lexerling import Lexer
from codegenling import CodeGen
from astling import *

# o uso_drs não vai ser mais uma tupla, vou ter o setor para usar o drs e a disponibilidade 

def evaluate_nodes(nodes):
    for node in nodes:
        if isinstance(node, Node):
            node.evaluate()
            evaluate_nodes(node.children)


text_input = """ ITS LIGHTS OUT AND AWAY WE GO 
lap volta is 1
rain_probability chance_of_rain is 0.2
overtaking conservador is (1,28)
driver piloto1 is 'Hamilton' 
radio_check chance_of_rain is 0.2 then >> conservador is (1,20) -Copy!
no_response >> piloto1 is 'Leclerc' -Copy!
CHECKRED FLAG"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
# parse_tree = parser.parse(tokens)
parse_tree = parser.parse(tokens).evaluate()
# print(parse_tree.evaluate())
# evaluate_nodes(parse_tree)


for token in tokens:
    print(token)