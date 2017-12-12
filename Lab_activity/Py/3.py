#Write a program to identify whether a given line is a comment or not.

inp = input("Enter your line: ")

if inp.startswith('//' or '/*'):
    print("This line is a comment!")
else:
    print("This lile is not a comment!")