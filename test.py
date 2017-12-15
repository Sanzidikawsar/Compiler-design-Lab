#Write a program to identify whether a given line is a comment or not.

from inspect import currentframe, getframeinfo

inp = input("Enter your line: ")

for line, val in enumerate(inp.split('\n')):
    if val.startswith('//' or '/*'):
        frameinfo = getframeinfo(currentframe())
        print("There is a comment in line: " + str(inp.frameinfo.lineno))
