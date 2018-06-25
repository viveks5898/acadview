#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        print("ek tha tiger")

class Tiger(Animal):
    def lion(self):
        print("tiger zinda hai")
k=Tiger()
k.animal_attribute()
k.lion()


#Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

output= A B
        A B


#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.


class Cop:
    def __init__(self,name,age,work__experience,designation):
        self.name=name
        self.age=age
        self.work__experience=work__experience
        self.designation=designation
    def display(self):
        print("before update")
        print("name=", self.name)
        print("age=", self.age)
        print("work experience=", self.work__experience)
        print("designation=", self.designation)
    def __update__(self,name,age,work__experience,designation):
        self.name = name
        self.age = age
        self.work__experience = work__experience
        self.designation = designation
class Mission(Cop):
    def add_mission_detail(self,name,age,work__experience,designation):
        print("updated cop details are")
        print("name=", end="")
        self.name = name
        print(name)
        print("age=", end="")
        self.age = age
        print(age)
        print("work__experience=", end="")
        self.work__experience = work__experience
        print(work__experience)
        print("designation=", end="")
        self.designation = designation
        print(designation)
x=Mission("Vivek",20,5,"Singer")
name=input("enter name")
age=int(input("enter age"))
work__experience=(input("enter work experience"))
designation=input("designation")
x.display()
y=Mission(name,age,work__experience,designation)
y.add_mission_detail(name,age,work__experience,designation)



#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        def area(self):
            s= self.length*self.breadth
            print(area)
class rectangle(shape):
    def area(self):
        area = self.length*self.breadth
        print("area of rectangle =", end="")
        print(area)
class square(shape):
    def area(self):
        area = self.length*self.breadth
        print("area of square =",end="")
        print(area)
m=rectangle(2,20)
n=square(34,34)
m.area()
n.area()

s