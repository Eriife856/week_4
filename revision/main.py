#working with calculator
def add(a,b):
 return a + b

def sub(a,b):
 return a - b

def div(a,b):
 if b !=0:
    return a/b
 else:
   return "error:division by zero"

def mod(a,b):
 return a % b

def expo(a,b):
 return a **b

def mult(a,b):
  return a*b

#display operation option to the user

print("select operation")
print("1. Add")
print("2. subtract")
print("3. division")
print("4. modulus")
print("5. exponential")
print("6. multiplication")
print("0. plese click to exist")

#users input
choice= input("enter choice(1/2/3/4/5/6/0): ")
    
# get two numbers as input from user
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

#calculating using calculator to input user input


if choice  =="1":
  print("result:", add(num1,num2))

elif choice == "2":
  print("result:", sub(num1,num2))

elif choice == "3":
  print("result:", div(num1, num2))
  

elif choice == "4":
  print("result:", mod(num1,num2))

elif choice == "5":
  print("result:", expo(num1 ,num2))

elif choice == "6":
  print("result:", mult(num1 ,num2))

elif choice =="0":
  print("existing,bye!")

else:
  print("invalid input. try again")

