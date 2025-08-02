n = 4
a = 1


def fact(a , b):
    for i in range(1,a+1):
        b *= i

    print(b)        
    
    
fact(n,a)    




def facRec(a):
    if(a<2):
        return 1
    else:
        return a * facRec(a - 1)
    
getFact = facRec(n)    
print(getFact)
    
    # Task 2: Using the Math Module for Calculations
    
    
import math    

a = int(input("Enter your Number :"))


print()


def squareRoot():
   global a
   b = math.sqrt(a) 
   print(f"Square Root of your number {a} is  {b}")

squareRoot()



def naturalLogarithm():
    global a
    b = math.log(a)
    print(f"Natural Logarithm of your number {a} is  {b}")



naturalLogarithm()



def sine():
    global a
    b = math.sin(a)
    print(f"Sine of your number {a} is  {b}")



sine()