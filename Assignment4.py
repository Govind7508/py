try:
    file1 = open('sample.txt','r')
    readFile = file1.read()
    print(readFile)
    file1.close()
except FileNotFoundError : 
    print("File not Exsist in Directory")
    
sentence = input("Enter a word or sentence to save in file")    
file2 = open('output.txt','a')
file2.write(sentence)
file2.close()

with open('output.txt','r') as file2:
    readFile = file2.read()
    print(readFile)
    
      