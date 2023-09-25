from compras_lex import tokens
import ply.yacc as yacc


def p_listacompras(p):
    'listacompras : categorias'
    p[0] = p[1]


def p_categorias(p):
    """categorias : categorias categoria
                  | categoria """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]+[p[2]]


def p_categoria(p):
    'categoria : CATEGORIA PONTOS2 produtos'
    p[0] = {p[1]: p[3]}


def p_produtos(p):
    """produtos : produtos produto
                | produto
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]+[p[2]]


def p_produto(p):
    'produto : HIFEN INDICE PONTOS2 PONTOS2 PRODUTO  PONTOS2 PONTOS2 PRECO  PONTOS2 PONTOS2 NUMERO PONTOVIRGULA  '
    p[0] = (p[5], float(p[8])*float(p[11]))


def p_error(p):
    print('ERRO SINTATICO')


parser = yacc.yacc(debug=True)

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

print(parser.parse(data))
