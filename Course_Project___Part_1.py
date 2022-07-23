print("Payroll Processing\n")

def calc_tax_netpay(total_hours, hourly_rate, tax_rate):
    income_tax= float(total_hours) * float(hourly_rate) * float(tax_rate)
    netpay = float(total_hours) * float(hourly_rate) - income_tax
    return income_tax, netpay

def insert_employee_name():
    employee_name = input("Enter employee name: ")
    return employee_name

def insert_hours():
    hours = float(input('Enter hours worked per pay period: '))
    return hours

def insert_hourly_rate():
    hourly_rate = float(input("Enter employee hourly rate: "))
    return hourly_rate

def insert_tax_rate():
    tax_rate = float(input("Enter effective tax rate (in decimal eg 0.30): "))
    return tax_rate

def calc_gross_pay(hours, hourly_rate):
    gross_pay = float(hours) * float(hourly_rate)
    return gross_pay

def employee_info(employee_name, hours, hourly_rate, tax_rate, income_tax, gross_pay, netpay):
    print()
    print("Employee name: ", employee_name)
    print("Hours worked per pay period: ", hours)
    print("Effective tax rate: ", tax_rate)
    print("Income tax deducted: $", income_tax)
    print("Gross pay: $", gross_pay)
    print("Net pay for ", employee_name, "is: $", netpay)
    print("*******************************************************\n")

def cumulative_totals(total_employees, total_hours, total_tax, total_gross_pay, total_netpay):
    print("Total employees: ", total_employees)
    print("Cumulative hours all employees: ", total_hours)
    print("Total tax amount: ", total_tax)
    print("Total gross pay: ", total_gross_pay)
    print("Total net pay: ", total_netpay)
    print()

def main():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_netpay = 0

    while True:
        employee_name = insert_employee_name()
        if employee_name =="end":
            break
        hours_worked = insert_hours()
        hourly_rate = insert_hourly_rate()
        tax_rate = insert_tax_rate()
        gross_pay = calc_gross_pay(hours_worked, hourly_rate)
        income_tax, netpay= calc_tax_netpay(hours_worked, hourly_rate, tax_rate)
        employee_info(employee_name, hours_worked, hourly_rate, tax_rate, income_tax, gross_pay, netpay)

        total_employees += 1
        total_hours += hours_worked
        total_tax += income_tax
        total_gross_pay += gross_pay
        total_netpay += netpay
    cumulative_totals(total_employees, total_hours, total_tax, total_gross_pay, total_netpay)

if __name__=="__main__":
    main()