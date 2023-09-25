import ply.lex as lex

tokens = (
    "PALAVRA",
    "VIRGULA",
    "PONTO_E",
    "PONTOI",
    "PONTOF",
    "RETS"
)

t_PALAVRA = r"(\w|\-)+"
t_VIRGULA = r"\,"
t_PONTO_E = r"\!"
t_PONTOI = r"\?"
t_PONTOF = r"\."
t_RETS = r"\.{3,}"

t_ignore = " \t\n"


def t_error(t):
    print(f"CARATERE ilegal {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

data = "OLa,eu chamo-me miguel!"

lexer.input(data)

while token := lexer.token():
    print(token)
