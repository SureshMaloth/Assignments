"""
#

employ_details={
    101:{"Name":"Suresh","Domain":"Python","Emp_id":"MT-01931","Mail":"suresh.marolix@gmail.com"},
    102:{"Name":"Abhi","Domain":"Devops","Emp_id":"MT-01932","Mail":"abhi.marolix@gmail.com"},
    103:{"Name":"Ram","Domain":".Net","Emp_id":"MT-01933","Mail":"ram.marolix@gmail.com"},
    104:{"Name":"Surya","Domain":"Testing","Emp_id":"MT-01934","Mail":"Surya.marolix@gmail.com"}
}

check_the_input=input("the vale is remove or update r add r check:")

if check_the_input=="check":
    given_empId=int(input("enter empId:"))
    if given_empId in employ_details:
        print(employ_details[given_empId])
    else:
        print("Employee Id Is Not Found")
elif check_the_input=="add":
    add_key=int(input("enter empId:"))
    employee=eval(input("enter emp Dtails:"))
    employ_details[add_key]=employee
    print(employ_details)
    print(employ_details[add_key])
    print(len(employ_details))
elif check_the_input=="update":
    given_empId=int(input("enter empId:"))
    given_key=input("enter the key:")
    update_value=input("enter the val:")
    if given_empId in employ_details:
        employ_details[given_empId][given_key]=update_value
        print(employ_details[given_empId])
    else:
        print("Not Found the Employee Id")
elif check_the_input=="remove":
    given_empId=int(input("enter the empId:"))
    if given_empId in employ_details:
        employ_details.pop(given_empId)
        print(employ_details)
    else:
        print("Not Found The Employee Id")
else:
    print("Enter The Correct Employee Id")
"""
                   
#
employee_details={}

def add_employee_details():
    Name=(input("enter the name:"))
    Domain=(input("enter the Domain:"))
    Mail=(input("enter the Mail:"))
    Empid=(input("enter the empId:"))
    EmpNo=int(input("enter No:"))

    employees={
        "Name":Name,
        "Domain":Domain,
        "Mail":Mail,
        "EmpId":Empid
    }
    employee_details[EmpNo]=employees
for i in range(int(input("Nbr of emp:"))):
    add_employee_details()

#print(employee_details)
check_the_input=input("the vale is remove or update r add r check:")


if check_the_input=="add":
    
    print(employee_details)
    
    print(len(employee_details))
elif check_the_input=="check":
    given_empId=int(input("enter empId:"))
    if given_empId in employee_details:
        print(employee_details[given_empId])
    else:
        print("Employee Id Is Not Found")
elif check_the_input=="update":
    given_empId=int(input("enter empId:"))
    given_key=input("enter the key:")
    update_value=input("enter the val:")
    if given_empId in employee_details:
        employee_details[given_empId][given_key]=update_value
        print(employee_details[given_empId])
    else:
        print("Not Found the Employee Id")
elif check_the_input=="remove":
    given_empId=int(input("enter the empId:"))
    if given_empId in employee_details:
        employee_details.pop(given_empId)
        print(employee_details)
    else:
        print("Not Found The Employee Id")
else:
    print("Enter The Correct Employee Id")

                    
