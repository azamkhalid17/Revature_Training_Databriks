from ArithCalculation import ArithCalculation
from AgeNotEnoughError import AgeNotEnoughError
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
age=int(input("Enter age: "))
calc=ArithCalculation(n1,n2)
print(f'ADD two no.:{calc.add()}')
print(f'subtract two no.:{calc.sub()}')
print(f'Multiplication two no.:{calc.mul()}')
try:
    if n2==0:
        raise ZeroDivisionError ("num2 is 0")
    if age<18:
        raise AgeNotEnoughError("You are Minor")
except ZeroDivisionError as zde:
        print(f'{zde}')
except AgeNotEnoughError as anee:
    print(f'{anee}')
else:
    try:
       l1=[1,2,3]
       val=l1[10]
       res=calc.div()
    except ZeroDivisionError as zde:
        print(f"{zde} - 0 in denominator")
    except IndexError as ie:
        print(f"{ie} - Index not available")
    except:
        print("Oops !, something went wrong")
    else:
        print(val)
        print(res)
    finally:
        print("DONE !")



