#Q.1-Take an input year from user and decide wheather it is leap year or not.

a=int(input("Enter a year= "))
if(a%4==0):
    print("leap yaer")
else:
    print("not leap year")



#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

a=int(input("Enter a length"))
b=int(input("Enetr a breadth"))
if(a==b):
    print("It is square")
else:
    print("it is Rectanglee")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

x=int(input("Enter a age of x"))
y=int(input("Enter a age of y"))
z=int(input("Enetr a age of z"))
if(x<y and x<z):
    print("x is youngest")
if(y<x and y<z):
    print("y is youngest")
if(z<x and z<y):
    print("z is youngest")
if(x>y and x>z):
    print("x is oldest")
if(y>x and y>z):
    print("y is oldest")
if(z>x and z>y):
    print("z is oldest")
else:
    print("ages are same")



#Q.4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input). points can only take on positive integer values up to 200.
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."
#Points	Prize
#1-50	No Prize
#51-150	Wooden Dog
#151-180	Book
#181-200	Chocolates

x=int(input("Enter a point"))
if(x>=1 and x<=50):
    print("Sorry no prize this time")
elif(x>=51 and x<=150):
    print("Congratulations You Won a Wooden Dog")
elif(x>=151 and x<=180):
    print("Congratulation You Won a Book")
elif(x>=181 and x<=200):
    print("Congratulations You Won a chocolates")


#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

x=int(input("Enter the quantity"))
p=100*x
if(p>1000):
    p=p-.1*p
print(p)