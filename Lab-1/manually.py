text = str(input("Enter your text here: "))

temp = ''

for i in text:
    if i == ' ':
        temp = temp + "\n"

print(temp)