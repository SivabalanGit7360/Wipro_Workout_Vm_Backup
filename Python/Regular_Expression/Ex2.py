# print('hello\nworld')
# print(r'hello\nworld')

# * - zero or more times
# + - one or more times
# ? - either present or absent
# {n} - 'n' number of occurances

# to*tal -- ttal total tootal toootal toooootal ex..
# to+tal -- total tootal toootal toooootal toooooootal
# https?://www.mydomain.com http://www.mydomain.com https://www/mydomain.com
# http://w{3}.mydomain http://www.mydomain.com

import re

s1 = input("Enter a string\n")
# val = re.search(r"to*tal",s1)
# val = re.search(r"to+tal",s1)
# val = re.search(r"https?://www.mydomain.com", s1)
val = re.search(r"https?://w{3}.mydomain.com", s1)

if val:
    print("matched")
else:
    print("not matched")

