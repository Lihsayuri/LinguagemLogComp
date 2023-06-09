
import sys
from main import PrePro, Node, UnOp, BinOp, LapVal, StringVal, TyreVal, Identifier, FuncCall, VarDec, Block, Assign,  Return, While, If, FuncDec, NoOp
from tokenizer import *
from tables import *


## vê onde tu parou, mas basicamente: o funcCall acho que tá ok no identifier. O problema tá sendo definir a variável a = x+ y. Algum select next
# Alguma logica mal feita

class Parser:
    tokenizer = None

    def parseRelExp(tokenizer):
        node = Parser.parseExpression(tokenizer)
        while tokenizer.next.type == "GREATER" or tokenizer.next.type == "LESS" or tokenizer.next.type == "EQUAL_EQUAL" :
            if tokenizer.next.type == "EQUAL_EQUAL":
                node = BinOp(tokenizer.next.type, [node, Parser.parseExpression(tokenizer)])
            if tokenizer.next.type == "GREATER":
                node = BinOp(tokenizer.next.type, [node, Parser.parseExpression(tokenizer)])
            if tokenizer.next.type == "LESS":    
                node = BinOp(tokenizer.next.type, [node, Parser.parseExpression(tokenizer)])
 
        if tokenizer.next.type == "INT":
            sys.stderr.write(f"Erro de sintaxe: INT não esperado.Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
            sys.exit(1)
        else:
            return node


    def parseExpression(tokenizer):
        node = Parser.parseTerm(tokenizer)
        while tokenizer.next.type == "PLUS" or tokenizer.next.type == "MINUS" or tokenizer.next.type == "OR":
            if tokenizer.next.type == "PLUS":
                node = BinOp(tokenizer.next.type, [node, Parser.parseTerm(tokenizer)])
            if tokenizer.next.type == "MINUS":    
                node = BinOp(tokenizer.next.type, [node, Parser.parseTerm(tokenizer)])
            if tokenizer.next.type == "OR":
                node = BinOp(tokenizer.next.type, [node, Parser.parseTerm(tokenizer)])
 
        if tokenizer.next.type == "INT":
            sys.stderr.write(f"Erro de sintaxe: INT não esperado.Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
            sys.exit(1)
        else:
            return node

    def parseTerm(tokenizer):
        node = Parser.parseFactor(tokenizer)
        tokenizer.selectNext()
        while tokenizer.next.type == "AND":
            if tokenizer.next.type == "AND":
                node = BinOp(tokenizer.next.type, [node, Parser.parseFactor(tokenizer)])
            tokenizer.selectNext()
        if tokenizer.next.type == "INT":
            sys.stderr.write(f"Erro de sintaxe: INT não esperado.Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
            sys.exit(1)
        else:
            return node

 
    def parseFactor(tokenizer):
        tokenizer.selectNext()
        if tokenizer.next.type == "INT":
            node = LapVal(tokenizer.next.value, [])
            return node
        elif tokenizer.next.type == "STRING":
            node = StringVal(tokenizer.next.value, [])
            return node
        elif tokenizer.next.type == "OPENCURLYBRA":
            Parser.tokenizer.selectNext()
            if tokenizer.next.type != "TYRE_TYPE":
                sys.stderr.write(f"Erro de sintaxe: falta o tipo do pneu. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            tipo_pneu = tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type != "COMMA":
                sys.stderr.write(f"Erro de sintaxe: falta vírgula. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.type != "TYRE_STATE":
                sys.stderr.write(f"Erro de sintaxe: falta o estado do pneu. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            estado_pneu = tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type != "CLOSECURLYBRA":
                sys.stderr.write(f"Erro de sintaxe: falta fechar chaves. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node = TyreVal("tyre", [tipo_pneu, estado_pneu])
            return node
        elif tokenizer.next.type == "IDENTIFIER":  ## CORRIGIR ESSA PARTEEEEE
            node = Identifier(tokenizer.next.value, [])   ## ele faz o gette
            return node
        elif tokenizer.next.type == "CALL":  ## CORRIGIR ESSA PARTEEEEE
            tokenizer.selectNext()
            if tokenizer.next.type == "IDENTIFIER":
                node = Identifier(tokenizer.next.value, [])   ## ele faz o getter
                tokenizer.selectNext()
                if tokenizer.next.type == "NEED":
                    if tokenizer.peek().type == "OPENPAR":
                        tokenizer.selectNext()
                        node_call = FuncCall(node.value, [])
                        if tokenizer.peek().type != "CLOSEPAR":
                            while tokenizer.next.type != "CLOSEPAR":
                                node_rel_exp = Parser.parseRelExp(tokenizer)
                                node_call.children.append(node_rel_exp)
                                if tokenizer.next.type != "COMMA" and tokenizer.next.type != "CLOSEPAR":
                                    sys.stderr.write("Erro de sintaxe: falta vírgula no funcCall. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                            return node_call
                        else:
                            tokenizer.selectNext()
                            return node_call
        elif tokenizer.next.type == "MINUS":
            node = UnOp(tokenizer.next.type, [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == "PLUS":
            node = UnOp(tokenizer.next.type, [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == "NOT":
            node = UnOp(tokenizer.next.type, [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == "OPENPAR":
            node = Parser.parseRelExp(tokenizer)
            if tokenizer.next.type == "CLOSEPAR":
                return node
            else:
                sys.stderr.write(f"Erro de sintaxe: falta fechar parênteses no Factor. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
        else:
            sys.stderr.write(f"Erro de sintaxe: aqui só entra número, - ou +. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
            sys.exit(1)

    def parseBlock(tokenizer):
        node_Block = Block("", [])
        tokenizer.selectNext()
        while tokenizer.next.type != "FINISH":
            if tokenizer.next.type == "START":
                tokenizer.selectNext()
            node_Block.children.append(Parser.parseStatement(tokenizer))
            tokenizer.selectNext()
        return node_Block
    

    def parseStatement(tokenizer):
        if Parser.tokenizer.next.type == "TYPE":
            tipo_da_var = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                node_identifier = Identifier(Parser.tokenizer.next.value, [])
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "EQUAL":
                    node_expression = Parser.parseRelExp(Parser.tokenizer)
                    if Parser.tokenizer.next.type != "NEWLINE":
                        sys.stderr.write("Erro de sintaxe: não terminou a linha no identifier.  Caracter atual: {tokenizer.next.value}")
                    return VarDec(tipo_da_var, [node_identifier, node_expression])
            else:
                sys.stderr.write("Erro de sintaxe: falta o identifier. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
        elif Parser.tokenizer.next.type == "CHECKED":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "ARROW":
                sys.stderr.write("Erro de sintaxe: falta a seta no return.  Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node_rel_expl = Parser.parseRelExp(Parser.tokenizer)
            if Parser.tokenizer.next.type != "NEWLINE":
                sys.stderr.write("Erro de sintaxe: não terminou a linha no return.  Caracter atual: {tokenizer.next.value}")
            return Return("return", [node_rel_expl])
        elif Parser.tokenizer.next.type == "IDENTIFIER":
            node_identifier = Identifier(Parser.tokenizer.next.value, [])  # vai criar um nó com o valor sendo a variável. Ex: x1 e não tem nenhum filho
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                # tokenizer.selectNext()
                node_expression = Parser.parseRelExp(Parser.tokenizer)   ### PAREIIII AQUI
                if Parser.tokenizer.next.type != "NEWLINE" and Parser.tokenizer.next.type != "COPY!":
                    sys.stderr.write("Erro de sintaxe: não terminou a linha no identifier.  Caracter atual: {tokenizer.next.value}")
                print("Entrei no ASSIGN")
                return Assign(None, [node_identifier, node_expression])
            else:
                sys.stderr.write("Erro de sintaxe: falta o equal. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
        elif Parser.tokenizer.next.type == "CALL":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                node_identifier = Identifier(Parser.tokenizer.next.value, [])   ## ele faz o getter
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "NEED":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "OPENPAR":   ## CONFERIR ISSO AQUI
                        node_call = FuncCall(node_identifier.value, [])
                        if Parser.tokenizer.next.type != "CLOSEPAR":
                            while Parser.tokenizer.next.type != "CLOSEPAR":
                                node_rel_exp = Parser.parseRelExp(Parser.tokenizer)
                                node_call.children.append(node_rel_exp)
                                if Parser.tokenizer.next.type != "COMMA" and Parser.tokenizer.next.type != "CLOSEPAR":
                                    sys.stderr.write("Erro de sintaxe: falta vírgula no funcCall. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                            if Parser.tokenizer.peek().type != "NEWLINE" and Parser.tokenizer.peek().type != "COPY!":
                                sys.stderr.write("Erro de sintaxe: não terminou a linha no identifier.  Caracter atual: {tokenizer.next.value}")
                            return node_call
        elif Parser.tokenizer.next.type == "ENGINEON":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "OPENBRA":
                sys.stderr.write("Erro de sintaxe: falta abrir chaves no loop. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node_rel_exp = Parser.parseRelExp(Parser.tokenizer)
            if Parser.tokenizer.next.type != "COMMA":
                sys.stderr.write("Erro de sintaxe: falta vírgula no loop. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node_rel_exp_2 = Parser.parseRelExp(Parser.tokenizer)
            if Parser.tokenizer.next.type != "CLOSEBRA":
                sys.stderr.write("Erro de sintaxe: falta fechar chaves no loop. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "NEWLINE":
                sys.stderr.write("Erro de sintaxe: não terminou a linha no while. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node_block = Block("", [])
            tokenizer.selectNext()
            while tokenizer.next.type != "ENGINEOFF" : # and tokenizer.next.type != "FINISH"
                node_block.children.append(Parser.parseStatement(tokenizer))
                tokenizer.selectNext()
            if Parser.tokenizer.next.type != "ENGINEOFF":
                sys.stderr.write("Erro de sintaxe: falta end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "NEWLINE":
                sys.stderr.write("Erro de sintaxe: não terminou a linha no end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            return While("", [node_rel_exp, node_rel_exp_2, node_block])
        
        elif Parser.tokenizer.next.type == "RADIO_CHECK": #famigerado if
            node_rel_exp = Parser.parseRelExp(Parser.tokenizer)
            if Parser.tokenizer.next.type != "THEN":
                sys.stderr.write("Erro de sintaxe: não terminou a linha no if. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "INDICA":
                sys.stderr.write("Erro de sintaxe: não terminou a linha no if. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            node_block = Block("", [])
            tokenizer.selectNext()
            while tokenizer.next.type != "COPY!":
                node_block.children.append(Parser.parseStatement(tokenizer))
                if tokenizer.next.type == "COPY!":
                    break
                tokenizer.selectNext()
            if Parser.tokenizer.next.type == "COPY!": #por enquanto deixa o finish:
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type != "NEWLINE":
                    sys.stderr.write("Erro de sintaxe: não terminou a linha no end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                    sys.exit(1)
                # return If("", [node_rel_exp, node_block])
            print("OLHA O TOKEN AQUI: ", Parser.tokenizer.peek().type)
            if Parser.tokenizer.peek().type == "NO_RESPONSE":
                Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                print (Parser.tokenizer.next.type)
                if Parser.tokenizer.next.type != "INDICA":
                    sys.stderr.write("Erro de sintaxe: não terminou o else. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                    sys.exit(1)
                node_block_else= Block("", [])
                tokenizer.selectNext()
                while tokenizer.next.type != "COPY!": # and tokenizer.next.type != "ENGINEOFF" and tokenizer.next.type != "FINISH"
                    node_block_else.children.append(Parser.parseStatement(tokenizer))
                    if tokenizer.next.type == "COPY!":
                        break
                    tokenizer.selectNext()
                if Parser.tokenizer.next.type != "COPY!" :
                    sys.stderr.write("Erro de sintaxe: falta end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                    sys.exit(1)
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type != "NEWLINE":
                    sys.stderr.write("Erro de sintaxe: não terminou a linha no end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                    sys.exit(1)
                print("Uai. olha aquiii o node_block_else: ", node_block_else)
                print("Uai. olha aquiii o node_block: ", node_block)
                return If("", [node_rel_exp, node_block, node_block_else])
            return If("", [node_rel_exp, node_block])
            # else:
            #     sys.stderr.write("Erro de sintaxe: falta end ou else. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
            #     sys.exit(1)
        elif Parser.tokenizer.next.type == "SETUP":
            Tokenizer.selectNext(Parser.tokenizer)
            if Parser.tokenizer.next.type != "TYPE":
                sys.stderr.write("Erro de sintaxe: falta type no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                sys.exit(1)
            tipo_da_var_func = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                node_identifier_func = Identifier(Parser.tokenizer.next.value, [])
                Tokenizer.selectNext(Parser.tokenizer)
                if Parser.tokenizer.next.type != "NEED":
                    sys.stderr.write("Erro de sintaxe: falta o need no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                    sys.exit(1)
                Tokenizer.selectNext(Parser.tokenizer)
                if Parser.tokenizer.next.type == "OPENPAR":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "TYPE":
                        tipo_da_var = Parser.tokenizer.next.value
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type != "IDENTIFIER":
                            sys.stderr.write("Erro de sintaxe: falta o identificador no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                            sys.exit(1)
                        node_identifier_var = Identifier(Parser.tokenizer.next.value, [])
                        node_var_dec = VarDec(tipo_da_var, [node_identifier_var])
                        lista_var_decs = [node_var_dec]
                        Parser.tokenizer.selectNext()
                        while Parser.tokenizer.next.type == "COMMA":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type != "TYPE":
                                sys.stderr.write("Erro de sintaxe: falta o tipo no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                sys.exit(1)
                            tipo_da_var = Parser.tokenizer.next.value
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type != "IDENTIFIER":
                                sys.stderr.write("Erro de sintaxe: falta o identificador no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                            node_identifier_var = Identifier(Parser.tokenizer.next.value, [])
                            node_var_dec = VarDec(tipo_da_var, [node_identifier_var])
                            print("node_var_dec: ", node_var_dec)

                            lista_var_decs.append(node_var_dec)
                            Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "CLOSEPAR":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "NEWLINE":
                                node_Block = Block("", [])
                                tokenizer.selectNext()
                                if Parser.tokenizer.next.type != "RADIO_ON":
                                    sys.stderr.write("Erro de sintaxe: falta o radioon no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                    sys.exit(1)
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type != "NEWLINE":
                                    sys.stderr.write("Erro de sintaxe: não terminou a linha no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                    sys.exit(1)
                                tokenizer.selectNext()
                                while tokenizer.next.type != "RADIO_OFF":
                                    statement = Parser.parseStatement(tokenizer)
                                    if statement != None:
                                        node_Block.children.append(statement)
                                    tokenizer.selectNext()
                                if Parser.tokenizer.next.type != "RADIO_OFF":
                                    sys.stderr.write("Erro de sintaxe: falta end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                    sys.exit(1)
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type != "NEWLINE":
                                    sys.stderr.write("Erro de sintaxe: não terminou a linha no end. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                    sys.exit(1)
                                return FuncDec(tipo_da_var_func, [node_identifier_func, lista_var_decs, node_Block])
                            else:
                                sys.stderr.write("Erro de sintaxe: não terminou a linha no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                                sys.exit(1)
                        else:
                            sys.stderr.write("Erro de sintaxe: falta o CLOSEPAR no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                            sys.exit(1)
                    else:
                        sys.stderr.write(" Erro de sintaxe: falta type no function. Tipo atual: {tokenizer.next.type}. Caracter atual: {tokenizer.next.value}")
                        sys.exit(1)

        elif Parser.tokenizer.next.type == "NEWLINE":
            return NoOp("", [])
        

    def run(code):
        code = PrePro.filter(code)
        Parser.tokenizer = Tokenizer(code, 0)
        root = Parser.parseBlock(Parser.tokenizer)

        if Parser.tokenizer.position == len(Parser.tokenizer.source) and Parser.tokenizer.next.type == "FINISH":
            resultado =  root.evaluate(symbolTable=SymbolTable())
            return resultado
        else:
            sys.stderr.write("Erro de sintaxe: não consumiu tudo no diagrama sintático")
            sys.exit(1)
