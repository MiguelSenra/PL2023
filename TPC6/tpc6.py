import ply.lex as lex

states = (
    ("ocomment", "exclusive"),
    ("linecomment", "exclusive")
)

tokens = (
    "A_COMMENT",
    "F_COMMENT",
    "AL_COMMENT",
    # Para fechar o comentário de linha que é dado quando aparece o caracter \n.
    "FL_COMMENT",
    "TIPO",
    "VARIAVEL",
    "OPERADOR",
    "NUMERO",
    "FUNCTION",
    "FUNCTION_TIPO",
    "A_PAREN",
    "F_PAREN",
    "A_CHAV",
    "F_CHAV",
    "A_PARENR",
    "F_PARENR",
    "PONTO_VIRGULA",
    "PONTO",
    "VIRGULA",
    "IGUAL",
    "CONDITION_OPERATOR",
    "FOR_LOOP",
    "WHILE_LOOP",
    "IF",
    "IN"


)


def t_TIPO(t):
    r"int"
    return t


def t_FOR_LOOP(t):
    r"for"
    return t


def t_WHILE_LOOP(t):
    r"while"
    return t


def t_IF(t):
    r"if"
    return t


def t_IN(t):
    r"in"
    return t


def t_CONDITION_OPERATOR(t):
    r"==|<|>|!=|<=|>="
    return t


def t_IGUAL(t):
    r"="
    return t


def t_VIRGULA(t):
    r","
    return t


def t_PONTO_VIRGULA(t):
    r";"
    return t


def t_PONTO(t):
    r"\."
    return t


def t_A_PAREN(t):
    r"\("
    return t


def t_F_PAREN(t):
    r"\)"
    return t


def t_A_PARENR(t):
    r"\["
    return t


def t_F_PARENR(t):
    r"\]"
    return t


def t_A_CHAV(t):
    r"{"
    return t


def t_F_CHAV(t):
    r"}"
    return t


def t_A_COMMENT(t):
    r"\/\*"
    t.lexer.begin("ocomment")
    return t


def t_ocomment_F_COMMENT(t):
    r"\*\/"
    t.lexer.begin("INITIAL")
    return t


def t_AL_COMMENT(t):
    r"\/\/"
    t.lexer.begin("linecomment")
    return t


def t_linecomment_FL_COMMENT(t):
    r"\n"
    t.lexer.begin("INITIAL")
    return t


def t_NUMERO(t):
    r"-?\d+"
    return t


def t_OPERADOR(t):
    r"[\+\-/\*]"
    return t


def t_FUNCTION_TIPO(t):
    r"(function|myprogram)\s+(?=\w+\s*(?=\())"
    return t


def t_FUNCTION(t):
    r"\w+\s*(?=\()"
    return t


def t_VARIAVEL(t):
    r"\w+"
    return t


t_ANY_ignore = " \n\t"

t_linecomment_ignore = " \t"


def t_ocomment_linecomment_error(t):
    t.lexer.skip(1)


def t_error(t):
    print(f"CARATERE ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

data = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

data2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""
lexer.input(data2)
lexer.variables = list()


while token := lexer.token():
    print(token)
