# www.mydomain.com
# Meaning of (.) in regular expression - any character
# .*\.(.*)\..*

import re

# s1 = input("Enter a string\n")
# s1 = "this is my input which has $ some characters between dollar $ and need to be"
s1 = "in jinja template variables are given inside {{ myname }} like this"

# val = re.search(r'.*\.(.*)\..*', s1)
# val = re.search(r'.*\$(.*)\$(.*)', s1)
# val = re.search(r'.*\$(.*)\$(.*)', s1) # regex with 2 sets of parenthesis
val = re.search(r'.*\{(.*)\}\}.*', s1)

if val:
    print(val.group(1)) # display the characters between $
#   print(val.group(2)) # display the characters after the second $
else:
    print("not matched")