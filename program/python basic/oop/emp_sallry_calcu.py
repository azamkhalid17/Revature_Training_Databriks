from Employee import Employee

def main():
    employee = Employee()
    try:
        empid = int(input('Enter employee ID: '))
    except ValueError:
        print("Invalid employee ID. It must be an integer.")
        return

    ename = input('Enter employee name: ')
    try:
        bp = float(input('Enter basic pay of employee: '))
    except ValueError:
        print("Invalid basic pay. Provide a number.")
        return

    gross = employee.calc_grosspay(bp)
    net = employee.calc_netpay(bp)

    print(f'Emp id: {empid}\nName: {ename}\n'
          f'Gross Pay: {gross:.2f}\n'
          f'Net Pay: {net:.2f}')

if __name__ == "__main__":
    main()