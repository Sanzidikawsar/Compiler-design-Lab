#Write a program to delete comments from codes saved in a text file.
#go here for more about RE https://python.maateen.me/regex.html

import re

text = open('in', 'r')
read = text.read()
text.close()

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    with open('out', 'w') as w:
        w.write(re.sub(pattern, replacer, text))

comment_remover(read)

