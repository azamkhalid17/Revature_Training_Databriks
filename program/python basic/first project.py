#rint("hello word")
#print without new line
"""
print("Hello word",end=" ")
print(" I want to print in ssme line")
"""
#print output number
"""
print(3)
print(358)
print(50000)
print("I am", 35, "years old.")
"""
#variable Name
"""
1.Camle case variable-myFullName
2.pascal case-MyFLullName
3.Snake Case-my_full_namne
"""
x,y,z=1,2,3
print(x,y,z)
x=y=z=3
print(x,y,z)
#unpack=extracting value in variable from list and tuple is called unpacking
marks=[20,30,40]
x, y, z = marks
print(x)
print(y)
print(z)
#*****global variable and global keyword****
#Create a variable outside of a function, and use it inside the function
x = "Mohd Azam"
def myfunc():
  print("My name is " + x)
myfunc()
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
#Create a variable inside a function, with the same name as the global variable
x = " Mohd Mzam"
def myname():
  x = "Azam"
  print("My name is " + x)
myname()
print("My namme is " + x)
#global kewword
#If you use the global keyword, the variable belongs to the global scope:
def myname():
  global x
  x = "Mohd Azam"
myname()
print("My name is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "Mohd Azam"
def myname():
  global x
  x = "Azam"
myname()
print("My name is " + x)

