try:
    file1 = open('sample.txt','r')
    readFile = file1.read()
    print(readFile)
    file1.close()
except FileNotFoundError : 
    print("File not Exsist in Directory")
    
    
file2 = open('output.txt','a')
file2.write(" Hey I complete my task It's work")
file2.close()

with open('output.txt','r') as file2:
    readFile = file2.read()
    print(readFile)
    
      