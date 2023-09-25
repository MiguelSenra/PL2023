import ply.lex as lex

states = (
    ("taga", "exclusive"),
    ("tagf", "exclusive")
)

tokens = (
    "ATAG",
    "FTAG",
    "ATAGF",
    "NOME_TAG",
    "VALOR"
)


def t_ATAGF(t):
    r"</"
    t.lexer.begin("tagf")
    return t


def t_ATAG(t):
    r"<"
    t.lexer.begin("taga")
    return t


def t_taga_FTAG(t):
    r">"
    t.lexer.begin("INITIAL")
    return t


def t_taga_tagf_NOME_TAG(t):
    r"\w+"
    return t


def t_VALOR(t):
    r"[^<]+"
    return t


t_ignore = " \n\t"


def t_ANY_error(t):
    print(f"CARATERE ilegal {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

data = """
<pessoa>
    <nome>Maria</nome>
    <idade>12</idade>
</pessoa>
"""
lexer.input(data)


while token := lexer.token():
    print(token)
