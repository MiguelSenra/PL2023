import ply.lex as lex

tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "PAROPEN",
    "PARCLOSE"
)

t_PLUS = r'\+'
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_PAROPEN = r"\("
t_PARCLOSE = r"\)"


def t_MINUS(t):
    r"\-"
    return t


def t_NUMBER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t


#4 * (2+ 3)
t_ignore = ' \t\n'


def t_error(t):
    print(f"CARACTERE ilegal {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

data = """
    3 +4 * 10 +-20*2 
"""
lexer.input(data)

# while tok := lexer.token():
#   print(tok)

while data := input():
    lexer.input(data)
    while tok := lexer.token():
        print(tok)
