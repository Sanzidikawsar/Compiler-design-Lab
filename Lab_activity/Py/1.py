#Task 1: Write a program to tokenize a sentences with raw codes.

inp = input("Enter your text to tokenize: ") #please have a space at last of the input text
tokens = list()
st = 0
en = 0

for ind, val in enumerate(inp):
    if val==' ':
        st = en
        en = ind
        if st==0:
            tokens.append(inp[st:en])
        else:
            tokens.append(inp[st+1:en])

for token in tokens:
    print(token)