
#1.Write a python program to remove a given  character from string.
string=input("enter the string:")
char=input("enter the char:")
remove_char=string.replace(char,"")
print(remove_char)

#2.Write a program to check String is Palindrome or not.
string_poly=input("enter the str:")
check_poly=string_poly[::-1]
if string_poly==check_poly:
    print("Given String is a Polindrom")
else:
    print("Given String is Not a Polindrom")
#3.Write a python program to check given character is vowel or consonant.
char=input("enter the char:")
vowel="a,e,i,o,u,A,E,I,O,U"
if char in vowel:
    print("The Character is Vowel")
else:
    print("The Character is Not a Vowel")

#4.Write a python program to replace string space with given character in Python.
re_string=input("enter the str:")
char=input("enter the char:")
replace_string=re_string.replace(" ",char)
print(replace_string)

#5.Write a python program to count alphabets, digits, and special characters in the string.
string=input("enter the string:")
alphabets=0
digits=0
special_char=0
for i in string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        alphabets+=1
    else:
        special_char+=1
print(alphabets)
print(digits)
print(special_char)
#6.Write a python program to remove all the blank spaces in a given string.
space_word=input("enter the word:")
all_space=space_word.replace(" ","")
print(all_space)
#7.Write a python program to find sum of integers in the string.
string=input("enter the str:")
num=0
for i in string:
    if i.isdigit():
        num+=int(i)
print(num)

#8.Write a python program to Remove Repeated Character from String.
string=input("enter the str:")
pattern=""
count=0
for i in string:
    if i not in pattern:
        pattern+=i
print(pattern)
    
#9.Write a python program to count occurrence of given character in string. 
string=input("enter the str:")
char=input("enter the char:")
char_count=string.count(char)
print(char_count)

#10.Write a python program to check string is anagrams or not in Python.
str_1=input("enter the str_1:")
str_2=input("enter the str_2:")
len_1=len(str_1)
len_2=len(str_2)
result_1=0
for i in str_1:
    num=int(ord(i))
    result_1+=num
result_2=0
for j in str_2:
    nbr=int(ord(j))
    result_2+=nbr

if result_1==result_2:
    print("This Is Anagrams")
else:
    print("This is Not Anagrams")



