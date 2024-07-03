# [] - character class
# 'hello\s[abcdefghijklmn]'
# 'hello\s[a-n]'
# 'hello\s[A-Za-zo-9_]'
# 'hello\s[\w]'

import re

s1 = input("Enter a string\n")

val = re.search(r'hello\s[\w]', s1)

if val:
    print("matched")
else:
    print("not matched")