"""
number=range(1,10)
print(list(number))
number1=range(10)
print(list(number1))
number2=range(1,10,2)
print(list(number2))
"""
"""
name="Mohd Azam"
for x in name:
    print(x)
"""
"""
for i in range(1,10,2):
    print(i)
"""
# while loop palindrome check
"""
num=int(input("Enter a number:"))
sum=0
temp=num
while temp!=0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if sum==num:
    print(num,"palindrome")
else:
    print(num,"not palindrome")
"""
#check num is armsrtong
"""
num1=int(input("Enter a number:"))
temp=num1
len=len(str(num1))
sum=0
while num1!=0:
    digit=num1%10
    sum=sum+(digit**len)
    num1=num1//10
if  sum==temp:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")
"""
#*****squre of the natural no*****
len=int(input("Enter a number:"))
sum=0
for x in range(1,len+1):
    sum=sum+(x*x)
print(sum)


