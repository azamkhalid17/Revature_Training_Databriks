
a=7
b=5
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


#ter
price= 50
print("price is less than 100") if price<100 else print("price is greater than 100")

#conditional satement
day=int(input("enter the day: "))
if day==1:
    print("day is Monday")
elif day==2:
    print("day is Tuesday")
elif day==3:
    print("day is Wednesday")
elif day==4:
    print("day is Thursday")
elif day==5:
    print("day is Friday")
elif day==6:
    print("day is Saturday")
elif day==7:
    print("day is Sunday")
else:
    print("Enter day b/w 1 to 7")
"""
"""
day=int(input("enter the day: "))
match day:
    case 1:
        print("day is Monday")
    case 2:
        print("day is Tuesday")
    case 3:
        print("day is Wednesday")
    case 4:
        print("day is Thursday")
    case 5:
        print("day is Friday")
    case 6:
        print("day is Saturday")
    case 7:
        print("day is Sunday")
    case _:
        print("Enter day b/w 1 to 7")

#check leap year
year=int(input("enter the year: "))
if year%400==0:
    print(f"{year} is a leap year")
elif year%100==0:
    print(f"{year} is not a leap year")
elif year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")





