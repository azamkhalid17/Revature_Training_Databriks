#print pascal triangle
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    num = 1
    print(" " * (rows - i), end=" ")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
