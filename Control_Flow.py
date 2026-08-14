number=int(input('Enter a number:'))
if number % 2 == 0:
   print('Even number')
else :
   print('Odd number')

#IF-ELSE
marks=78
if marks >= 90 :
   grade="A+"
elif marks >=80 :
   grade ="A"      
elif marks >=70 :
   grade ="B"   
elif marks >=60 :
   grade ="C"   
elif marks >=50 :
   grade ="D"   
else :
   grade='F'
print(marks, {grade})     

#for loop 
for i in range(5):
   print(i)      
fruits=[ "mango", "papaya", "banana"] 
print(fruits) 

#while loop
count =1 

while count<=5 :
   print(count)
   count+=1
print("count>5")
for i in range(1,11):
   if i==6:
    break 
   print(i)
for i in range(1,11):
   if i==6:
    continue 
   print(i)   

for i in range(1,51 ) :
  if i % 3 == 0 and i % 5 == 0:
     print("Fizz Buzz")

  elif i % 3 == 0:
     print("Fizz")
  elif i % 5 == 0:
     print("Buzz")  
  else :
     print(i)   