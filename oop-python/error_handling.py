
result =None
x=int(input("Enter The first Number:"))
y = int(input("Enter The Second Number"))
try:
    result=x/y
except Exception as e:
    print("The error in my code is:",e)
print("------------New Line------------")
print("Result:",result)
