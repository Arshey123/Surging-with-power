# Activity 1
# n= int(input("Enter a number:"))
# def power2(n):
#     if n<=0:
#         return False
#     return (n&(n-1))==0
# if power2(n):
#     print(n,"is power of 2")
# else:
#     print(n,"is not power of 2")
# ACtivity 2
# def power (x,y):
#     result= 1
#     while y>0:
#         if (y%2==0):
#             x=x*x
#             y>>=1
#         else:
#             result= result*x
#             y= y-1
#     return result
# x= int(input("Enter a number:"))
# y= int(input("Enter power:"))
# print(power(x,y))
# Activity 3
def power(number):
    count=0
    if (number & (~(number & (number-1)) )):
        while(number>1):
            number>>=1
            count+=1
        if (count %2 ==0):
            return True
        else:
            return False
        

number=int(input("enter no"))
if (power(number)):
    print("number is power of 4")
else:
    print("number is not power of 4")