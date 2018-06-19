#Q.1- Take 10 integers from user and print it on screen.
i=0
l=[]
while(i<10):
  y=int(input("enter the no."))
  l.append(y)
  i=i+1
for i in l:
    print(i)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while(True):
    print("infinite")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
a=[]
sq=[]
for i in range(0,5):
    p=int(input("enter a no."))
    a.append(p)
print(a)
for p in a:
    k=p*p
    sq.append(k)
print(sq)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately.
i=0
l=[61,22,"abc",2.0]
x=[]
y=[]
z=[]
for i in l:

    if (type(i)==int):
        x.append(i)
    elif (type(i)==str):
        y.append(i)
    else:
        z.append(i)
print(x)
print(y)
print(z)

#Q.5- Using range(1,101), make a list containing even and odd numbers.
even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#Q.6-Print the following patterns:
#*
#**
#***
#****
p=4
for i in range(0,p):
    for a in range(0,i+1):
        print("*",end="")
    print("\r")

#Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.
m={'style': 'Arijitians','age':20}
for i in m:
    print(i,m[i])

#Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

i=0
x=[]
while(i<5):
    a=int(input("enter number"))
    x.append(a)
    i=i+1
a=int(input("enter number to be searched"))
for i in x:
         if(a==i):
             x.remove(i)
print(x)

