f = open('MyData.txt','r')
#print(f.read())
#print(f.readline())

f1 = open('NewData.txt','w')
#f1.write('hello welcome to my world')

for data in f:
    f1.write(data)