#print all rime Number in an interval
def primeno(n1, n2):
    primes = []
    for x in range(n1, n2 + 1):
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                primes.append(x)
    return primes


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = primeno(n1, n2)
print("Prime numbers between", n1, "and", n2, "are:", result)
