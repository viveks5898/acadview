#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(5)
        print("hi! this is Arijit Singh")
thread1=mythread(1)
thread1.start()


#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between

import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
         print(self.h)
for i in range(1,11):
    thread1=mythread(i)
    thread1.start()
    time.sleep(1)


#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec


import threading
import time
sec=[2,4,6,8,10]
class Dog(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run (self,counter):
        time.sleep(counter)
        print(self.h)

for i in sec:
    thread1=Dog(i)
    thread1.run(i)



#Q4. Call factorial function using thread.


import threading
import math
class fac(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        a=self.h
        b=math.factorial(a)
        print("factorial is =",b)
user=int(input("enter a no."))
thread=fac(user)
thread.start()
