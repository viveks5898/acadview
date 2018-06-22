                               #TUPLES
#Q.1- Write a program to create a tuple with different data types and do the following operations.
#1. Find the length of tuples
a=(6,7,8,"sandeep")
len(a)
print(len(a))

#Q.2-Find largest and smallest elements of a tuples.
x=(3,7,3,4,6,0)
y=(2,4,1,7,5,9)
print("max value of x is",max(x))
print("max value of y is",max(y))
print("min value of x is",min(x))
print("min value of y is",min(y))

#Q.3- Write a program to find the product of all elements of a tuple.
p=(5*6*7,1*2*3,7*8*9)
print(p)
                                #SETS
#Q.1- Create two set using user defined values.
#1. Calculate difference between two sets.
s=set((1,2,3,4))
r=set((2,3,4))
q=s-r
print(q)

#2. Compare two sets.
s=set((6,7,8,9))
r=set((7,8,9))
q=s<=r
print(q)
p=s>=r
print(p)

#3. Print the result of intersection of two sets.
s=set((1,2,3,4,5,6,7,8,9))
r=set((2,4,5,6,7))
q=s&r
print(q)

                                #DICTIONARIES
#Q.1- Create a dictionary to store name and marks of 1 students by user input.
x=input("enter the name")
y=input("enter the age")
z={'name':x,'age':y}
print(z)

#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
s=("mississippi")
a=s.count("m")
b=s.count("i")
c=s.count("s")
d=s.count("p")
m={'no. of m':a,'no. of i':b,'no. of s':c,'no. of p':d}
print(m)