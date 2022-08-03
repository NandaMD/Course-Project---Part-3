import datetime

print("Payroll Processing\n")


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

def calc_tax_netpay(total_hours, hourly_rate, tax_rate):
    income_tax= float(total_hours) * float(hourly_rate) * float(tax_rate)
    netpay = float(total_hours) * float(hourly_rate) - income_tax
    return income_tax, netpay

def employee_info(from_date, to_date, employee_name, hours, hourly_rate, tax_rate, income_tax, gross_pay, netpay):
    print()
    print("From date:", from_date.strftime('%m/%d/%y'))
    print("To date:", to_date.strftime('%m/%d/%y'))
    print("Employee name: ", employee_name)
    print("Hours worked per pay period: ", hours)
    print("Hourly rate: $", hourly_rate)
    print("Gross pay: $", gross_pay)
    print("Effective tax rate: ", tax_rate)
    print("Income tax deducted: $", income_tax)
    print("Net pay for ", employee_name, "is: $", netpay)
    print("*******************************************************\n")

def cumulative_totals(total_dict):
    print("Total employees: ", total_dict['total_employees'])
    print("Cumulative hours all employees: ", total_dict['total_hours'])
    print("Total tax amount: $", total_dict['total_tax'])
    print("Total gross pay: $", total_dict['total_gross_pay'])
    print("Total net pay: $", total_dict['total_netpay'])
    print()
    print('*********************************************************\n')

def get_from_to_date():
    from_date = input("Enter from date in mm/dd/yyyy format: ")
    from_date = datetime.datetime.strptime(from_date, "%m/%d/%Y").date()
    to_date = input("Enter to date in mm/dd/yyyy format: ")
    to_date = datetime.datetime.strptime(to_date, "%m/%d/%Y").date()

    return from_date, to_date

def calc_employee_taxes(employee_list, total_dict):
    for employee in employee_listt:
        from_date, to_date, employee_name, hours, hourly_rate, tax_rate = employee
        gross_pay = calc_gross_pay(hours, hourly_rate)
        income_tax, netpay = calc_tax_netpay(total_hours, hourly_rate, tax_rate)


def main():
    employee_list = [ ]
    total_dict={"total_employees": 0,
    "total_hours":0,
    "total_gross_pay":0,
    "total_tax": 0,
    "total_netpay":0}

    while True:
        employee_name = insert_employee_name()
        if employee_name =="end":
            break
        from_date, to_date = get_from_to_date()
        hours_worked = insert_hours()
        hourly_rate = insert_hourly_rate()
        tax_rate = insert_tax_rate()
        gross_pay = calc_gross_pay(hours_worked, hourly_rate)
        income_tax, netpay= calc_tax_netpay(hours_worked, hourly_rate, tax_rate)
        employee_info(from_date, to_date, employee_name, hours_worked, hourly_rate, tax_rate, income_tax, gross_pay, netpay)

        total_dict['total_employees'] += 1
        total_dict['total_hours'] += hours_worked
        total_dict['total_tax'] += income_tax
        total_dict['total_gross_pay'] += gross_pay
        total_dict['total_netpay'] += netpay
    cumulative_totals(total_dict)

if __name__=="__main__":
    main()