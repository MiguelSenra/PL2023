import ply.lex as lex

states = (
    ('multiline', 'exclusive'),
)

tokens = ('TEXTO',
          'INLINE_COMMENT')


def t_ANY_enter_multiline(t):
    r"\/\*"
    t.lexer.comment_level += 1
    T.begin('multiline')


def multiline_leave(t):
    r"\`\/"
    t.lexer.comment_level -= 1
    if (t.lexer.comment_level == 0):
        t.begin('INITIAL')


def t_multine_TEXTO(t):
    r"(.|\n)+?"


def t_INLINE_COMMENT(t):
    r'\/\/.*'
    pass


def t_TEXTO(t):
    r"(.|\n)+?"
    return t


dados = """
/* comment */ ola1

/* comment****comment */ ola2 /*
comment
/* comentário dentro de comentário */
****/ ola3

/*********/

ola4
 mais um pouco // remover comentário inline
FIM"""
lexer = lex.lex()
lexer.input(dados)
lexer.comment_level = 0

while tok := lexer.token():
    print(tok)
