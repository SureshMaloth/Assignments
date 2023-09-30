#1. write a program to create a calculator using functions (sum,sub,mul,div)
def sum_ele(values):
    total=0
    for i in values:
        total+=i
    return total
def sub_ele(values):
    total=0
    for i in values:
        total-=i
    return total
def mul_ele(values):
    total=1
    for i in values:
        total*=i
    return total
def div_ele(values):
    total=0
    for i in values:
        total//=i
    return total

values=list(map(int,(input("enter the num:").split())))
sum_values=sum_ele(values)
sub_values=sub_ele(values)
mul_values=mul_ele(values)
div_values=div_ele(values)
print(sum_values)
print(sub_values)
print(mul_values)
print(div_values)




#Variable length arguments. 
#2. Write a program to enter employee details and also filter  the stored employee  details  with name and empid and designation and email. 
def employee_details(*emp_details):
    employee_nbr=int(input("enter the empNbr:"))
    if employee_nbr in emp_details[0]:
        print(emp_details[0][employee_nbr])

emp_details={}
for i in range(int(input("enter the empNo:"))):
    name=input("enter the name:")
    emp_id=input("enter the empId:")
    designation=input("enter the des:")
    email=input("enter the mail:")
    emp_no=int(input("enter the nbr:"))
    employes={"Name":name,"EmpId":emp_id,"Designation":designation,"Mail":email}
    emp_details[emp_no]=employes
employee_details(emp_details)

                 


