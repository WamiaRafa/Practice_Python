#approach 1
class Person:
    def __init__(self,fname, lname):
        self.fname=fname
        self.lname=lname
    def Print(self):
        return print(self.fname, self.lname)
class Student(Person):
   pass
s1=Student("Wamia" ,"Rafa")
s1.Print()

#approach 2
class animal:
    def __init__(self):
     pass
    def eat(self):
     return print("animal is eating")
class Dog(animal): 
    def __init__(self, birthdate):
       super().__init__()     
       #you can add more attribute
       self.birthdate=birthdate
    def bark (self) :     
     return print("barking", self.birthdate)
d1=Dog(1985)
d1.eat()
d1.bark()