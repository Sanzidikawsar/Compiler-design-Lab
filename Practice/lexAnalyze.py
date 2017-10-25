import pandas as pd

df = pd.read_csv('symbol.csv')
df.head()

keyword = df['keyword'].dropna().values
math_oprator = df['Arithmetic Operators'].dropna().values
logical = df['Logical Operators'].dropna().values
bitwise = df['Bitwise Operators'].dropna().values
other = df['Other Operators'].dropna().values

f = open('in', 'r')
file = f.read()

def lexical_analyzer(file):
    return file.split()

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
        'Keywords': k,
        'Identifiers': i,
        'Math Operators': m,
        'Logical Operators': l + b,
        'Numerical Values': n + f,
        'Others': o
    }
    return outputs

lexic = lexical_analyzer(file)
table = symbol_table(inputs=lexic)
df1 = pd.DataFrame([table], columns=table.keys())
print(df1)
f = open('out', 'w')
for i in table:
    f.write(i)
    f.write(str(table[i]))
    f.write("\n")

