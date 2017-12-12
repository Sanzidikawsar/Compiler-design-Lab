#Write a program to remove the blank spaces (space, newline, tabs) from code.
#go here for more about RE https://python.maateen.me/regex.html

import re

inp = input("Enter your code:")

for line in inp.split('\n'):
    out = re.sub('\s+', ' ', line)

    print(out)