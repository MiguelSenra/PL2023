import ply.lex as lex

states = (('index', 'exclusive'),
          ('valor', 'exclusive'))

tokens = ('CATEGORIA',
          'PONTOS2',
          'INDICE',
          'HIFEN',
          'PRODUTO',
          'PRECO',
          'NUMERO',
          'PONTOVIRGULA'
          )


def t_CATEGORIA(t):
    r"\w+"
    return t


def t_PONTOS2(t):
    r":"
    t.lexer.begin('index')
    return t


def t_index_valor_PONTOS2(t):
    r":"
    return t


def t_index_apanhaenter(t):
    r"\n(?=\w)"
    t.lexer.begin('INITIAL')
    pass


def t_index_HIFEN(t):
    r"-"
    return t


def t_index_INDICE(t):
    r"\d+"
    return t


def t_index_PRODUTO(t):
    r"[\w ]+\w+"
    t.lexer.begin('valor')
    return t


def t_valor_PRECO(t):
    r"\d+\.\d{2}"
    return t


def t_valor_NUMERO(t):
    r"\d+"
    return t


def t_valor_PONTOVIRGULA(t):
    r";\n"
    t.lexer.begin('index')
    return t


t_ANY_ignore = r"[ \t\n]"


def t_ANY_error(t):
    print(f"Caracter ilegal : '{t.value[0]}'")
    t.lexer.skip(1)


data = """CARNE :
  - 1 :: Bife :: 10.00 :: 1;
  - 2 :: Panado :: 5.00 :: 4;
  - 3 :: Hambúrguer :: 8.00 :: 3;
  - 4 :: Almôndegas :: 7.00 :: 5;

BEBIDA :
  - 5 :: Água :: 0.40 :: 16;
  - 6 :: Sumo :: 1.50 :: 9;
  - 7 :: Refrigerante :: 1.80 :: 10;

FRUTA :
  - 8 :: Maçã :: 0.60 :: 20;
  - 9 :: Banana :: 0.50 :: 15;
  - 10 :: Laranja :: 0.80 :: 18;
  - 11 :: Pêssego :: 0.70 :: 22;
  - 12 :: Uva :: 0.90 :: 17;

LEGUMES :
  - 13 :: Alface :: 1.00 :: 25;
  - 14 :: Tomate :: 0.75 :: 23;
  - 15 :: Cebola :: 0.50 :: 28;
  - 16 :: Batata :: 0.30 :: 30;
  - 17 :: Cenoura :: 0.40 :: 26;

PASTELARIA :
  - 18 :: Bolo de Chocolate :: 3.50 :: 1;
  - 19 :: Croissant :: 1.20 :: 14;
  - 20 :: Pastel de Nata :: 1.00 :: 5;
  - 21 :: Donut :: 0.80 :: 13;
"""

lexer = lex.lex()
lexer.input(data)

while tok := lexer.token():
    print(tok)
