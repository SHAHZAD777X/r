try:
    age=int(input("Enter your age:"))
    print("Age:",age)
except:
    print("Pls enter correct number or data")

if age%2==0:
    print("age number is even")
else:
    print("age number is odd")