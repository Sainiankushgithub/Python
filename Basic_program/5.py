# LOOPS IN PYTHON 
# i=0
# while(i<10):
#     print(i)
#     i=i+1


# print("Printing the even and odd numbers form nth natural number")
# i=0
# num=int(input("Enter the nth natural number "))
# print("Displaying all the Even number form all natural number")
# while(i<num):
#     if(i%2==0):
#         print(i)
#     i=i+1

n=int(input("Enter the number to gets reverse "))
sum=0
while(n>0):
    r=n%10
    sum=sum*10+r;
    n=n//10;

print("Reverse of your number is ",sum);
