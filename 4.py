# INPUT AND OUTPUT STATEMENTS


# print("Enter your name : ")
# name=input()
# age=int(input("Enter your age : "))
# roll_no=int(input("Enter your roll_no "))
# print(name,age,roll_no)

# print("Checking your eligibility in PUB ")
# if(age>=18):
#     year=int(input("Enter your year "))
#     if(year>1):
#         print("Your are allowed !!!!")
#     else:
#         print("You are not allowed")
# else:
#     print("Sorry !!! You are not Eligible because your age below 18")


# SUM OF THREE NUMBERS USING NESTED ELSE IF 

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if(a>b):
    if(a>c):
        print("A is greator")
    else:
        print(" C is greator")
elif(b>c):
    print("b is greator")
else:
    print("C is greator")
    
