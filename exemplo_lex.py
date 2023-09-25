import ply.lex as lex

tokens = ['STRING']


def t_STRING(t):
    r'".*"'
    var = t.value[1:-1]
    t.value = []
    t.value.append(var)
    t.value.append("INDENT")
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex(debug=1)

text = '"Hello, World!"'
lexer.input(text)
for token in lexer:
    print(token)
