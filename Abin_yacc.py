from Abin_lex import tokens
import ply.yacc as yacc


class Abin:
    def __init__(self, num, esq, dir):
        self.numero = num
        self.esq = esq
        self.dir = dir

    def pp(self):
        return f"|num:({self.numero}) esq:({self.esq.pp()}) dir:({self.dir.pp()}|"


class Vazia:
    def __init__(self):
        self.num = 0

    def pp(self):
        return "|Empty|"


def p_Abin(p):
    """Abin : PA PF
            | PA NUM Abin Abin PF"""
    if len(p) == 3:
        p[0] = Vazia()
    else:
        p[0] = Abin(p[2], p[3], p[4])


def p_error(p):
    print("Erro Sintatico.")


parser = yacc.yacc()

Abin_in = """
( 5 (3 (1 () ()) ()) (8 () (10 () ())))
"""
print(parser.parse(Abin_in).pp())
