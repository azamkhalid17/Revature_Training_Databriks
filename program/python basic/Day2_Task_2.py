#Check whether a string is palindrome or not
"""
string1=input('Enter your first name: ')
string2=string1[::-1]
if string1==string2:
    print(f"{string1} is a palindrome")
else:
    print(f"{string1} is not a palindrome")

"""


#by while loop
"""
def palindrome(string):
    n = len(string)-1
    string2 = ""
    while n>=0:
        string2=string2+a[n]
        n=n-1
    return string2

a=input("Enter String: ")
x=palindrome(a)
if x==a:
    print(f"{a} is a palindrome")
else:
    print(f"{x} is not a palindrome")
"""
#by for And range
def palindrom1(string):
    n = len(string)
    string2 = ""
    for x in range(n-1,-1,-1):
        string2=string2+string[x]
    return string2
string=input("Enter String: ")
y=palindrom1(string)
if y==string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")