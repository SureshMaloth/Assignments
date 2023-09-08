#1.Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
dict_a={"name":"suresh","age":21}
dict_a["study"]="BTech"
print(dict_a)


#2.Write a Python script to check whether a given key already exists in a dictionary.
dict_a={"a":1,"b":2,"c":3,"d":4}
giv_val="a"
res="Not In dict_a"
for i in dict_a:
    if i in giv_val:
        res=("Already Exists")
    
print(res)
#3.Write a Python program to iterate over dictionaries using for loops
Person_details=eval(input("Enter the dict:"))
for i in Person_details:
    print(i)
    
#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
number=int(input("enter the nbr:"))
dict_sqr={}
for i in range(1,number+1):
    dict_sqr[i]=i*i
print(dict_sqr)

#5.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
#Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
word_str=input("enter the str:")
word_str=word_str.replace(" ","")

nbr_ele={}
for i in word_str:
    nbr_ele[i]=word_str.count(i)
print(nbr_ele)


#6. Write a Python program to sum all the items in a dictionary.
dict_sum={1:"a",2:"b",3:"c",4:"d",5:"e"}
sum_dict=0
for i in dict_sum:
    sum_dict+=i
print(sum_dict)
#7.Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
dict1 = eval(input("enter the val1:"))
dict2 =eval(input("enter the val2:"))
dict3=dict2
for key,value in dict1.items():
    if key in dict2:
        dict3[key]=value+dict2[key]
    else:
        dict3[key]=value
print(dict3)
#8.Write a Python program to access dictionary key's element by index.
#Expected Output:
#physics
#math
#chemistry
dict_index=eval(input("enter the val:"))
list_ele=list(dict_index)
for i in range(len(list_ele)):
    index_keys=list_ele[i]
    print(index_keys)

#9.Write a Python program to remove a key from a dictionary.
dict_val=eval(input("enter the ele:"))
rem_key=input("enter the remove key:")
del dict_val[rem_key]
print(dict_val)
#10.Write a Python script to merge two Python dictionaries.d
dict_1=eval(input("enter the dict1:"))
dict_2=eval(input("enter the dict2:"))
dict_1.update(dict_2)
print(dict_1)