import ply.yacc as yacc

from tabela_lex import tokens


def p_tabela(p):
    "tabela : linha linha_lixo conteudo"
    p[0] = p[1]+'\n' + p[3]


def p_linha(p):
    "linha: BARRA valores BARRA"
    p[0] = ','.join(p[2])


def p_valores(p):
    """valores: valores BARRA VALOR
              | VALOR """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+[p[3]]


def p_linha_lixo(p):
    "linha_lixo : BARRA lixo BARRA"
    p[0] = p[2]


def p_lixo(p):
    """ lixo: lixo BARRA tracos~
            |tracos
    """
    p[0] = ""


def p_conteudo(p):
    """conteudo : conteudo linha
                | linha"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+[p[3]]


def p_error(p):
    print("Erro Sintatico.")


parser = yacc.yacc()

tab_in = """
"""
print(parser.parse(tab_in))
