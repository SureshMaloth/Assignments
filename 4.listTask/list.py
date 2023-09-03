#1.write a python program to merge two lists
list_1=eval(input("enter the list1:"))
list_2=eval(input("enter the list2:"))
print(list_1+list_2)

#2.write a python program to find the sum of list elements.
list_1=eval(input("enter the list:"))

sum_list=0
for i in list_1:
    sum_list+=i
print(sum_list)
#3.write a python program to print even and odd numbers seperatly in list.
list_ele=eval(input("Enter The Nums:"))
even_num=[]
odd_nums=[]
for i in list_ele:
    if i%2==0:
        even_num.append(i)
    else:
        odd_nums.append(i)
print("Even_Nums:"+str(even_num))
print("Odd_Nums"+str(odd_nums))

#4.write a python program to delete element of given index in list.
list_ele=eval(input("Enter The ele:"))
index_char=int(input("enter the Index:"))
index_val=list_ele[index_char:index_char+1]
list_ele.remove(index_val[0])
print(list_ele)
#5.write a python program to delete given elemet from the list 
list_ele=eval(input("Enter The ele:"))
index_char=int(input("enter the Index:"))

list_ele.remove(index_char)
print(list_ele)
#6.write a python program to insert an elemet  at given index location.
list_ele=eval(input("enter the Ele:"))
insert_char=input("enter the Char:")
insert_index=int(input("enter the Index:"))
list_ele.insert(insert_index,insert_char)
print(list_ele)
#7.write a python program to check the sizes of given two lists are same.
list_1=eval(input("enter the list_1:"))
list_2=eval(input("enter the list_2:"))
len_1=len(list_1)
len_2=len(list_2)
print(len_1==len_2)
#8.Write a Python function that takes two lists and returns True if they have at least one common member.
list_1=eval(input("enter the list1:"))
list_2=eval(input("enter the lsit2:"))
result="False"
for i in list_1:
    for j in list_2:
        if i==j:
            result="True"
        
print(result)

#Write a Python program to remove a specified column from a given nested list.
#Original Nested list:
#[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#After removing 1st column:
#[[2, 3], [4, 5], [1, 1]] 

list_ele=eval(input("enter the nested list:"))
new_list=[]
spe_clmn=int(input("enter the clmn:"))
for i in list_ele:
    
    i.remove(i[spe_clmn])
    new_list.append(i)
print(new_list)
#9. Write a Python program to convert a list of multiple integers into a single integer.
#Sample list: [11, 33, 50]
#Expected Output: 113350

list_mul=eval(input("enter the mul int:"))
new_list=""
for i in list_mul:
    new_list+=str(i)
print(new_list)
#10.Write a Python program to remove duplicates from a list.
list_ele=eval(input("enter the ele:"))
new_list=[]
for i in list_ele:
    if i not in new_list:
        new_list.append(i)
print(new_list)