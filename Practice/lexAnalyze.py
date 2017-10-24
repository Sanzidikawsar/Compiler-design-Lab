import pandas as pd  # import dependencies

df = pd.read_csv('symbol.csv')  # I collect all C language Keyword , operator data and store them in a csv file
df.head()  # Showing top 5 data

keyword = df['keyword'].dropna().values  # addaing keyword from csv file and remove any NaN or empty row
math_oprator = df['Arithmetic Operators'].dropna().values
logical = df['Logical Operators'].dropna().values
bitwise = df['Bitwise Operators'].dropna().values
other = df['Other Operators'].dropna().values

file = """
int a , b , c ;
float d , e ;
a = b = 5 ;
c = 6 ;
if ( a > b )
{
    c = a - b ;
    e = d - 2.0 ;
}
else
{
    d = e + 6.0 ;
    b = a + c ;
}
"""


# ***lexical analyzer function will split the code in to 


def lexical_analyzer(file):
    """file:  will take any text file
        return: lexical analyze of that file."""
    return file.split()


# ***symbol table function will create a symbol table from the l

def symbol_table(inputs):
    """inputs: Will take a lexical analyzed array,
        return: return a dictonary with Keywords, Identifiers, Operators and values"""
    k = []
    m = []
    l = []
    b = []
    o = []
    n = []
    i = []
    f = []

    for data in inputs:
        if data in keyword:  # checking the lexic is in the keyword list
            if data not in k:  # if the lexic is not in symbol table will add in the table else will drop
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
        #         'Bitwise Operators' : b,
        'Numerical Values': n + f,  # adding both flot and int value
        'Others': o
    }

    return outputs


# ***lexical analyze the input file***
lexic = lexical_analyzer(file)
# ***Creating Symbol table***
table = symbol_table(inputs=lexic)
# ***Showing table as a table format using pandas***
df1 = pd.DataFrame([table], columns=table.keys())
print(df1)
# ***Printing the table***
for i in table:
    print(i, table[i])
