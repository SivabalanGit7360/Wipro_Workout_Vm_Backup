# open [filepath, filemode, buffering]
# filepath = C:\Users\Administrator\Desktop\a.txt

# windows

# r'C:\Users\Administrator\Desktop\a.txt'
# 'C:\\Users\\Administrator\\Desktop\\a.txt'
# C:/Users/Administrator/Desktop/a.txt

fh = open('sample.txt','r')

print(fh.name) # return file along with path
print(fh.read())
print(fh.mode) # 
print(fh.closed) # return false if the file still open

print(fh.readline) # return one line at a time
print(fh.readlines) # return as list


fh = open('sample.txt','w')
fh.write("Programming in python is fun\n")

fh.writelines(['programming in python is a fun\n','python is easy to learn\n'])

fh.close()