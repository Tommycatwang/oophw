from tkinter import N
import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():
    name=ec.employeeclass('Jimmy Smith',58475 , 'Information System', 'Developer', 6800)

    desc1=pdc.payrolldeduction('Food Court', '8/14/2022', 22.50,39119)
    desc2=pdc.payrolldeduction('Gift contribution','8/12/2022',25.00,58475)
    desc3=pdc.payrolldeduction('food court','8/17/2022',15.25,21547)
    desc4=pdc.payrolldeduction('Vending Machine','8/22/2022',3.00,58475)
    desc5=pdc.payrolldeduction('Vending Machine','8/5/2022',2.75,58475)
    
    final=int(desc2.get_chargeamount()) + int(desc4.get_chargeamount()) + int(desc5.get_chargeamount())

    print("*** Employee Pay ***")
    print("Name:", name.get_name())
    print("ID Number:", name.get_idnumber())
    print("Department:", name.get_department())
    print("Gross Pay: $", f'{name.get_monthlysalary():,.2f}')
    print("Net Pay: $", f'{name.get_monthlysalary()-final:,.2f}')

main()
