import ply.lex as lex

states = (('place', 'inclusive'),
          ('openning', 'inclusive'),
          ('decoration', 'inclusive'))

tokens = ('PLACE_NAME',
          'OPEN',
          'CLOSED',
          'DECORATION_NAME',
          'QUOTES')


def t_next_place(t):
    r"\","
    t.lexer.last_place


def t_QUOTES(t):
    r"\""
    t.lexer.begin('place')


def place_PLACE_NAME(t):
    r"[^\(]"
    t.lexer.last_place = t.valaue.strip()


def t_place_end(t):
    r"\("
    t.lexer.begin('openning')


def t_openning_OPEN(t):
    r"open"
    t.lexer.openned_places[t.lexer.last_place] = []


def t_openning_end(t):
    r"\)"
    t.lexer.begin('INITIAL')


def t_begin_decoration(t):
    r"\("
    t.lexer.begin("decoration")


def t_decoration_DECORATION_NAME(t):
    r"[^\]]"
    l=t.lexer.openned_places.get(t.lexer.last_place)
    if l not None:
        l.append()
def t_ignore(t):
    r"\\n \t"


def t_LOCAL(t):


data = """
"Springfield (open) [bunny statue]",
"Happyville (closed)", 
"Chocolate Land (open) [Easter eggs]",
"Rabbit Hill
(closed) [chocolate bunnies]",
"Cadbury Castle (open)",
"Peeps Park (closed)",
"Lily Gardens
(open) [butterfly garden]",
"Cocoa Town (open) [chocolate river]",
"Carrot
Cove (closed)",
"Hoppington (open) [bunny hop]",
"Jellybean Junction (closed)",
"Bon Bon Bay (open) [marshmallow chickens]",
"Marshmallow 
Marsh (closed)",
"Candy Cane Canyon (open)",
"Cotton Candy Corner 
(closed)",
"Sugarplum Square (open) [sugarplum fairies]",
"Pudding Plains (closed)
[pudding cups]",
"Gingerbread Village (open)",
"Caramel Castle (closed)
[caramel apples]",
"Lollipop Lane (open)"
"Chirping Forest (open)",
"Carrot Farm (closed)",
"Jellybean Junction 
(open) [jellybean trail]",
"Springfield (closed)",
"Chocolate Land 
(closed)",
"Lily Gardens (closed)"
"""
lexer = lex.lex()
lexer.openned_places = dict()
lexer.last_place = 0
