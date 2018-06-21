#Q.1- Create a list with user defined inputs.
l=[]
a=input("enter value")
l.append(a)
print(a)

#output- enter values5
#5

#Q.2- Add the following list to above created list:
#l=['google','apple','facebook','microsoft','tesla']
l=[]
a=input("enter value")
l.append(a)
print(a)
x=input("enter the string")
l.append(x)
print(l)

#output- enter value4
#4
#enter the stringfacebook
#['4', 'facebook']


#Q.3- Count the number of time an object occurs in a list.
l=[1,2,2,2,2,4,5,3,5,9]
a=l.count(2)
print(a)

#output- 4

#Q.4- create a list with numbers and sort it in ascending order.
number=[3,5,1,9,4,3]
number.sort()
print(number)

#output- [1, 3, 3, 4, 5, 9]

#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
A=[2,8,6,4,3,1]
B=[9,1,5,3,7,4]
A.sort()
B.sort()
print(A)
print(B)
C=A+B
C.sort()
print(C)

#output- [1, 2, 3, 4, 6, 8]
      #   [1, 3, 4, 5, 7, 9]
     #    [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]

#Q.6-Implement a stack using lists.
l=[2,3,5,7,1]
(l.append(9))
print(l)
l.pop(3)
print(l)

#output-
#[2, 3, 5, 7, 1, 9]
#[2, 3, 5, 1, 9]


