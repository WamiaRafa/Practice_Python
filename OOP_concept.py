#Create a class
#class Myclass:
    #x=5
#Create an object named p1, and print the value of x:
#create a object:
#p1=Myclass()
#print(p1.x)    
 #delete object

#del p1

#multiple object
#p1=Myclass()
#p2=Myclass()
#p3=Myclass()

#print(p1. x)
#print(p2. x)
#print(p3. x)

#class  Student:
 #  def __init__(self, name , id):
  #     self.name=name
   #    self.id=id
   #def greet(self):
    #   print ("hello" ,self.name)    
   #def ID(self):
      # print("YOUR ID IS :" , self.id) 


#s1=Student("RAFA", "23-54301-3")
#s1.greet()
#s1.ID()


#class Dog :

 #def __init__(self, name , age):
  
  #self.name=name
  #self.age=age
 #def bark(self):
  #print(self.name , "says Woof")
# Create an object
#d1 = Dog("Buddy", "3")
# Call the bark method
#d1.bark()

class Rectangle :
  
  def __init__ (self, length, width) :
    self.length=length
    self.width=width
  def area(self) :
   return self.length * self.width
  def diameter(self): 
   total = 2*(self.length + self.width) 
   return total
r1=Rectangle(5,2)

print(r1.area())  
print("Diameter" , r1.diameter())


class Circle :
   def __init__(self, radius):
     self.radius=radius
   def calArea(self):
     return self.radius*self.radius

c1=Circle(4)
print("Circle Area: ",c1.calArea())     