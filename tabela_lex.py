import ply.lex as lex

tokens = ('BARRA',
        'TRACOS',
        'VALOR')

t_BARRA= r'\|'
def t_TRACOS(t):
    r"\-+"
    return t

def t_VALOR(t):
    r"[^\|\-\n]+"
    t.value=t.value.strip()
    return t

t_ignore=" \n\t"

def t_error(t):
    print(f"Carater ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer=lex.lex()
