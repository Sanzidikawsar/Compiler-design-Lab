#Write a program to tokenize a sentence using strtok() function.

inp = input("Enter your text to tokenize: ")
tokens = inp.split(' ') #split() is alternative of strtok() of C

for token in tokens:
    print(token)