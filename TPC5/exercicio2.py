import ply.lex as lex

tokens = (
    "PAR_RETO_O",
    "PAR_RETO_C",
    "VIRGULA",
    "NUMERO",
    "BOOL",
    "STRING"
)

t_PAR_RETO_O = r"\["
t_PAR_RETO_C = r"\]"
t_VIRGULA = r","
t_BOOL = r"True|False"
t_STRING = r"[\w\-]+"
t_NUMERO = r"\d+(.\d+)?"


def t_error(t):
    print(f"CARACTERE ilegal {t.value[0]}")
    t.lexer.skip(1)


t_ignore = r" \n\t"

lexer = lex.lex()

data = "[ 1,5, palavra, False,3.14, 0, fim]"
lexer.input(data)

while token := lexer.token():
    print(token)
