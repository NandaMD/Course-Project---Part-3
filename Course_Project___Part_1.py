from datetime import datetime

print("Payroll Processing\n")


def insert_employee_name():
    employee_name = input("Enter employee name: ")
    return employee_name

def get_from_to_date():
    from_date = input("Enter from date in %m/%d/%Y format: ")
    to_date = input("Enter to date in %m/%d/%Y format: ")
    
    return from_date, to_date

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

def print_info():
    total_employees = 0
    total_hours= 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_netpay = 0.00
    #################################################################
    Empfile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyy) or All for all data in file: ")
        if(rundate.upper()=="ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m,%d,%y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")
            print()
            continue
    while True:
        EmpDetail = Empfile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        from_date = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(from_date, "%m/%d/%y")
            if(checkdate < rundate):
                continue
#########################################################

        to_date = EmpList[1]
        employee_name = EmpList[2]
        hours = float(EmpList[3])
        hourly_rate = float(EmpList[4])
        tax_rate = float(EmpList[5])
        gross_pay, income_tax, netpay = calc_tax_netpay(total_hours, hourly_rate, tax_rate)
        print(from_date, to_date, employee_name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{netpay:,.2f}")
        total_employees + 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_tax = income_tax
        total_netpay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True




def PrintTotals(EmpTotals):
    print("Total employees: ", total_dict['total_employees'])
    print("Cumulative hours all employees: ", total_dict['total_hours'])
    print("Total tax amount: $", total_dict['total_tax'])
    print("Total gross pay: $", total_dict['total_gross_pay'])
    print("Total net pay: $", total_dict['total_netpay'])
    print()
    print('*********************************************************\n')





if __name__=="__main__":
    Empfile = open("Employees.txt", "a+")
    EmpTotals = {}
    while True:
        employee_name = insert_employee_name()
        if employee_name.upper() =="END":
            break
        from_date, to_date = get_from_to_date()
        hours_worked = insert_hours()
        hourly_rate = insert_hourly_rate()
        tax_rate = insert_tax_rate()
        ##############################################
        EmpDetail = from_date + "|" + to_date + "|" + employee_name + "|" + str(hours_worked) + "|" + "|" + str(hourly_rate) + "|" + str(tax_rate) + "\n"
        Empfile.write(EmpDetail)

        Empfile.close()
        DetailsPrinted = False
        print_info()

        if (DetailsPrinted):
            PrintTotals(EmpTotals)
        else:
            print ("No detail information to print")
        

