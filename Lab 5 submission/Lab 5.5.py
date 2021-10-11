def get_bonus(sold, salary):
    if(sold> 1000):
        bonus = 20/100*salary
    elif(sold > 500 and sold <= 1000):
        bonus= 10/100*salary
    return bonus

def get_nett_salary(salary, bonus):
    netsalary = bonus + salary
    return netsalary

def main(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 DATA ENTRY                 ")               
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    staff = int(input("Enter staff id          : "))
    salary = float(input("Enter staff salary      : RM "))
    units_sold = int(input("Enter total units sold  : "))
    bonus = get_bonus(units_sold, salary)
    netsalary= get_nett_salary(salary, bonus)
    display(staff, salary, units_sold, bonus, netsalary)

def display(staff, salary, units_sold, bonus, netsalary):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 SALARY SLIP                ")   
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                : ", staff)
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              : ", units_sold)
    print("Bonus                   :  RM {:.2f}".format(bonus))
    print("Nett Salary             :  RM {:.2f}".format(netsalary))

main()