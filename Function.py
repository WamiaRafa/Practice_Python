def is_even(number):
    if number % 2 == 0:
        return True
    else :    
        return False
print (is_even(70))

def greetings(name, greet="Welcome"):
    print(name ,greet )  
    return 1

greetings("RAFA")


balance=10000

def deposit(amount):
   global balance
   balance= amount+balance
   print( balance)
   return  balance

deposit(50000) 

