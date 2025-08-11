studentList ={"A":100,"B":82,"C":78,"D":50}

print(studentList)

name = input("Enter Student Name and Get Their number : ").capitalize()
if name in studentList:
    print(f"{name}'s number is {studentList[name]}")
else:
    print("Student  Not Found")
    
    
    
list =[1,2,3,4,5,6,7,8,9,10]
listNew =[]
for i in list:
        listNew.append(i)
        if i == 5:
         break   
print(f"Original List {list}") 
print(f"Extracted First Five Element {listNew}")     
listNew.reverse()
print(f"Reversed Extracted Element {listNew}")    
    
