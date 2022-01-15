def add(A,B):
    return A + B
def subtract(A,B):
    return A - B
def multiply(A,B):
    return A * B
def divide(A,B):
    return A / B

print ("Select the operation : ")
print ("A-> Add")
print ("B -> Subtract")
print ("C -> Multiply")
print ("D -> Divide")

choice = input("Enter the choice (A / B / C /D) : ")
num1 = int(input("Please enter your first number : "))
num2 = int(input("Please enter your second number : "))

if choice == 'A':
    print (num1,"+",num2,"=", add(num1,num2))
elif choice == 'B':
    print (num1,"-",num2,"=", subtract(num1,num2))
elif choice == 'C':
    print (num1,"-",num2,"=", multiply(num1,num2))
elif choice == 'D':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")