

#Q.1- Create a function to calculate the area of a circle by taking radius from user.


x=int(input("enter a no."))
def area(x):
    area=3.14*x*x
    return area
print(area(x))




#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.



def perfect(n):
   sum=0
   for i in range(1,n):
        if(n%i==0):
            sum=sum+i
   if(sum==n):
         return True
   else:
         return False
for i in range(1,1001):
    if(perfect(i)):
        print(i)



#Q.3- Print multiplication table of 12 using recursion.



def table(x,t=1):
    if (t==11):
        return
    (print(str(x) + "x" + str(t) +"=" + str(x*t)))
    table(x,t+1)
table(x=12)



#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.



def power(m,p):
    if(p==1):
        return m
    else:
        return(m*power(m,p-1))
print(power(9,9))



#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.



n=int(input("enter a number"))
def fact(n):
    if n == 0:
        return 1
    s=n*fact(n-1)
    return s
b=fact(n)
print(b)
