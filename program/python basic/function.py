#Method pass parameters in function
"""
def diff(n1,n2):
    result=n1-n2
    return result
def add(n1,n2):
    result=n1+n2
    return result
def addition(*nums):#arbitary Variable Length Argument
    for num in nums:
        res=res+num
    return res

n1=int(input("enter first number"))
n2=int(input("enter second number"))
sum=add(n1,n2)#positional parameter
print(sum)
difference=diff(n1=5,n2=6)#kerword argument
print(difference)
"""
"""
def total(*numbeers):
    result=sum(numbeers)
    return result
print(total(1,2,3))

def addition(**nums):
    result=nums["f"]+nums["s"]+nums["t"]
    return result
n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
print(addition(f=n1,s=n2,t=n3))
"""
"""
def details(**info):
    for key,value in info.items():
        print(f"{key}: {value}")
details(name="Azam",age=23,city="Noida")
"""
"""
def add(n1,n2,n3=0,n4=0):
    result=n1+n2+n3+n4
    return result
n1=int(input("enter first number"))
n2=int(input("enter second number"))
#n3=int(input("enter third number"))
#n4=int(input("enter fourth number"))
print(add(n1,n2,n3,n4))
print(add(n1,n2,n3))
print(add(n1,n2))
"""
"""
def calculate(num1,num2,num3):
    total=num1+num2+num3
    avg=total/3
    return avg
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
totalavg=calculate(num1,num2,num3)
print(f'Totalavg:{totalavg}')
"""
#****lambda function******
add=lambda n1,n2:n1+n2
print(add(1,2))
squre=lambda n1:n1*n1
print(f'squre of 5 if {squre(5)}')
res=lambda x,y:2*x+3*y+7
print(res(2,3))



