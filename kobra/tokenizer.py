# Kobra tokenizer

reserved = {
    'if'        : 'IF',
    'then'      : 'THEN',
    'elif'      : 'ELIF',
    'else'      : 'ELSE',
    'end'       : 'END'
}

tokens = [
    "NUMBER",
    "LPAREN",
    "RPAREN",
    "COMPARE",
    "ID",
] + list(reserved.values())

t_ignore    = ' \t'

t_LPAREN    = r'\('
t_RPAREN    = r'\)'

literals = [ '+', '-', '*', '/', '=' ]

def t_EQUAL(t):
    r'=[ \t]*='
    t.type = 'COMPARE'
    t.value = '=='
    return t

def t_LGTHAN(t):
    r'[<>]'
    t.type = 'COMPARE'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Line {0.lineno}: Number {0.value} is too large!".format(t))
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

if __name__ == "__main__":
    from ply import lex
    lex.lex()
    lex.input("""
x = 6 + 1/(5*2 )
# comment goes here, lol
zeta = x + 1
if (zeta = = x) then
    zeta = -z
elif (zeta < x) then
elif (zeta > x) then
end
""")
    for tok in iter(lex.token, None):
        print ( repr(tok.type), repr(tok.value) )
