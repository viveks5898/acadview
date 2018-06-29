
#Q.1- Write a Python program to read last n lines of a file

f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines"))
for i in range(0,n):
    print(a[i])
f.close()


#Q.2- Write a Python program to count the frequency of words in a file.


a="kill"
f=open("file.txt","r")
k=f.read()
m=k.split()
print(k.count(a))


#Q.3- Write a Python program to copy the contents of a file to another file


f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("file3.txt","w")
c.writelines(a)


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.


i=0
f=open("file1.txt","r")
a=(f.read())
b=open("file2.txt","r")
c=(b.read())
d= open("file4.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()



#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.


l=[]
global str
j=[]
import json
import random
for i in range(0,10):
    l.append(random.randint(1,10))
f=open("file2.txt","w")
for t in l:
    h="".join(str(t))
    f.write(h)
f.close()
d=open("file2.txt","r")
a=d.read()
for x in a:
    if(x.isdigit()):
        m="".join(x)
        j.append(m)
j.sort()
c=open("file5.txt","w")
c.write(str(j))

