
from parserling import Parser
from lexerling import Lexer
from codegenling import CodeGen
from astling import *

def evaluate_nodes(nodes):
    for node in nodes:
        if isinstance(node, Node):
            node.evaluate()
            evaluate_nodes(node.children)


text_input = """ ITS LIGHTS OUT AND AWAY WE GO 
EngineOn[12]
driver piloto1 is 'Leclerc'
driver piloto2 is 'Vettel'
driver piloto3 is 'Hamilton'
EngineOff
CHECKRED FLAG"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
# parser.parse(tokens).eval()
parse_tree = parser.parse(tokens)
evaluate_nodes(parse_tree)
# for node in parse_tree:
#     if isinstance(node, Node):
#         print(node.value)
#         print(node.children)

for token in tokens:
    print(token)