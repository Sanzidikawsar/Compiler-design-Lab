keyword = ['keyword', 'auto', 'break', 'case', 'char', 'const', 'continue' 'default', 'do', 'double', 'else', 'enum', 'extern', 'float',
 'for', 'goto', 'if', 'int', 'long', 'register', 'return',' short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
 'union', 'unsigned', 'void', 'volatile', 'while']
math_oprator = ['+', '-', '*', '/', '=', '+=', '-=', '*=', '/=', '%=']
logical = ['Err:520', '>', '<', '!=', '>=', '<=', '&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
other = [',', '{', '}', '(', ')', '[', ']']

text = open('in', 'r')
file = text.read()
text.close()

lexic = file.split()

def symbol_table(inputs):
    k = []
    m = []
    l = []
    b = []
    o = []
    n = []
    i = []
    f = []

    for data in inputs:
        if data in keyword:
            if data not in k:
                k.append(data)
        elif data in math_oprator:
            if data not in m:
                m.append(data)
        elif data in logical:
            if data not in l:
                l.append(data)
        elif data in bitwise:
            if data not in b:
                b.append(data)
        elif data in other:
            if data not in o:
                o.append(data)
        else:
            try:
                num = int(data)
                if num not in n:
                    n.append(num)
            except:
                try:
                    num = float(data)
                    if num not in f:
                        f.append(num)
                except:
                    if data not in i:
                        i.append(data)

    outputs = {
        'Keywords: ': k,
        'Variables:': i,
        'Operators': m + l + b,
        'Constants: ': n + f,  # adding both flot and int value
        'Special Symbols: ': o,
    }

    return outputs

table = symbol_table(lexic)
for i in table:
    print(i, table[i])

print()
