print("Simple Calculator")
print("For adding of two numbers type sum")
print("For subtraction of two numbers type subtract ")
print("For Multiplication of two numbers type multiply ")
print("For Division of two numbers type divide ")
operation=input("operation : ")
num1=float(input("number1 :"))
num2=float(input("number2 :"))
if(operation == "sum"):
     sum=num1+num2
     print(sum)                      #THIS IS SIMPLE CALCULATOR
elif(operation == "subtract"):
     subtract=num1-num2
     print(subtract)
elif(operation == "multiply"):
     multiply=num1*num2
     print(multiply)    
elif(operation == "divide"):
     divide=num1/num2
     print(divide)    
else:
     print("somthing is wrong")