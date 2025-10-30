#Count Of the number of vowels count in a string
string=input("Enter a string")
count=0
for x in string:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        count+=1
print("*****Number of vowels*****")
print(count)