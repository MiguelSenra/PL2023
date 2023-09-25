import ply.lex as lex

tokens = ('PA',
          'PF',
          'NUM')

t_PA = r"\("
t_PF = r"\)"
t_NUM = r"\d+"
t_ignore = " \n\t"


def t_error(t):
    print(f"Carater ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()
