print("Enter your Number to Know your number is ODD or Even")

a = int(input("Enter your number : "))


if(a==0):
    print("Your number is not Either Odd Numbe or Even Number")
else:   
    if(a%2 ==0):
          print("Your number is Even")
    else:
          print("Your number is Odd")    
          
total = 0          
for i in range(1, 51):
    total += i
    
print(total)
              