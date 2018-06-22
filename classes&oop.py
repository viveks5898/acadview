#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def circum(self):
        return 2*self.radius*3.14
x=Circle(5)
print("Area of Circle is:",x.area())
print("Circumference of circle is:",x.circum())


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.


class Student():
    def __init__(self,name,roll_no):
        self.x=name
        self.y=roll_no
p=Student('Sandeep Kumar',11602148)
print("Name of student is:",p.x)
print("roll_no of student is:",p.y)


#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature():
    def __init__(self,celsius_temperature):
        self.temp=celsius_temperature
    def fahrenheit(self):
        return 9/5*self.temp+32
    def celsius(self):
        return self.temp
m=Temperature(100)
print("the fahrenheit temperature of celcius is:",m.fahrenheit())
print("the celsius temperature of farenheat is:",m.celsius())


#Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.


class Movie_Details():
    def __init__(self,movie_name,artist_name,year_of_relase,rating):
        self.w=movie_name
        self.x=artist_name
        self.y=year_of_relase
        self.z=rating

c=Movie_Details('Race-3','Salmaan Khan',2018,4)
print("Name of the movie is:",c.w)
print("Actor name is:",c.x)
print("Year of relase:",c.y)
print("rating:",c.z)

def __update__(self, movie_name, artist_name, year_of_relase, rating):
    self.w = movie_name
    self.x = artist_name
    self.y = year_of_relase
    self.z = rating

n=input("enter the movie name")
an=input("entre the artist name")
y=input("enter the year")
r=input("enter the rating")





#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary


class Expenditure():
    def __init__(self,expenditure,saving,total_salary=0):
        self.ex=expenditure
        self.s=saving
        self.t=0

    def display(self):
        print("total expenditure:",self.ex)
        print("total saving:",self.s)

    def total_salary(self):
        self.t=self.ex+self.s
    def display__salary(self):
        return self.t
p=int(input("enter the expenditure"))
r=int(input("enter the saving"))
i=Expenditure(p,r)
i.display()
i.total_salary()
print("total salary:",i.display__salary())