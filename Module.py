
#Q.1- What is Time Tuple?

print("There is a popular time module available in python which provides function for working with time,and for converting"
      " between representations ,the function (time.time()) returns the current system time in ticks since 12 am,january 1,1970(epoch)"

      "Index   Attribute   values"
      "o       tm_year     2018"
      "1       tm_mon      1-12"
      "2       tm_mday     1-31"
      "3       tm_hour     0 to 23"
      "4       tm_min      0 to 59"
      "5       tm_sec      0 to 61(60 or 61 are leap-seconds"
      "6       tm_wday     0 to 6"
      "7       tm_yday     1 to 366"
      "8       tm_isdst    -1,0,1 where -1 means library determines DST")



#Q.2- Write a program to get formatted time.

import time
print(time.asctime())


#Q.3- Extract month from the time.

import datetime
a='2018-6-14'
d=(datetime.datetime.strptime(a,"%Y-%m-%d") )
print(d.month)


#Q.4- Extract date from the time.

import datetime
a='2018-6-19'
d=(datetime.datetime.strptime(a,"%Y-%m-%d") )
print(d.day)



#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.


import datetime
a='11/01/2021'
d=(datetime.datetime.strptime(a,"%d/%m/%Y"))
print(d.day)



#Q.6- Write a program to print time using localtime method.


import time
print(time.asctime(time.localtime()))



#Q.7- Find the factorial of a number input by user using math package functions.

import math
a=int(input("enter a number"))
print(math.factorial(a))



#Q.8- Find the GCD of a number input by user using math package functions.


import math
a=int(input("enter first number"))
b=int(input("enter second number"))
print(math.gcd(a,b))


#Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment. 

import os
print(os.getcwd())
print(os.environ)
