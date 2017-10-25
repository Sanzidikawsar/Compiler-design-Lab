y = input('Enter the eqn: ')

operator = ['*', '/', '-', '+', '=']

output = []
stuck = []
for i in y:
    if i not in operator:
        output.append(i)
    else:
        if len(stuck) != 0:
            if operator.index(stuck[-1]) >= operator.index(i):
                stuck.append(i)
            else:
                output.append(stuck[-1])
                stuck.pop()
                stuck.append(i)
        else:
            stuck.append(i)

outputs = output + stuck[::-1]
for i in outputs:
    if i != " ":
        print(i, end='')