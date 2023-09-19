#1.membership operator using in and not in

letter="this is membership check"
in_word="i" in letter
print(in_word)

letter_1="this is membership check"
not_in_word="n" in letter
print(not_in_word)

word=input("enter the word:")
ele=input("enter the ele:")
result=ele in word
print(result)

letter="this is membership check"
in_word="i" not in letter
print(in_word)

letter_1="this is membership check"
not_in_word="n" not in letter
print(not_in_word)

word=input("enter the word:")
ele=input("enter the ele:")
result=ele not in word
print(result)




#2.removing spaces from the string (strip)
word ="  thi is strip method "
value=word.strip()
print(value)

#particular  left side deletion
word ="  thi is strip method "
value=word.lstrip()
length=len(value)
print(value)
print(length)
print(len(word))

#particular  right side deletion
word ="   thi is strip method    "   
value=word.rstrip()
length=len(value)
print(value)
print(length)
print(len(word))
      


# particular char removes

word="@#! python is a programming language *^"
result=(word.strip("@#!*^ "))
print(result)
print(len(word))
print(len(result))

#3.comparing the two string

word_1=input("enter The word1:")
word_2=input("enter the word2:")
if word_1>word_2:
    print(word_1)
elif word_2>word_1:
    print(word_2)


#print the greater total value with ascii
name_1=input("enter the name1:")
name_2=input("enter the name2:")
split_name_1=list(name_1)
total_name_1=0
for i in split_name_1:
    num=ord(i)
    total_name_1+=num
split_name_2=list(name_2)
total_name_2=0
for i in split_name_2:
    num=ord(i)
    total_name_2+=num
if total_name_1>total_name_2:
    print(name_1)
else:
    print(name_2)


#comparing Numbers
num_1=int(input("enter the num1:"))
num_2=int(input("enter the num2:"))
if num_1==num_2:
    print("is Same")
elif num_1>num_2:
    print(num_1)
elif num_2>num_1:
    print(num)
#4.finding the substring by using index 
# to given the string first occurance of the substring value find() 
# if the value not availble returns value error
word="python is a high level programming launguage"
sub_string="h"
find_substring=word.index(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.index(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.index(subString,start,end)
print(result)
#5.finding the substring by using rindex
# to given the string last occurance of the substring value find() 
# if the value not availble returns value error
word="python is a high level programming launguage"
sub_string="g"
find_substring=word.rindex(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.rindex(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.rindex(subString,start,end)
print(result)
#6.finding the substring by using find
# to given the string first occurance of the substring value find() 
# if the value not availble returns -1
word="python is a high level programming launguage"
sub_string="h"
find_substring=word.find(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.find(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.find(subString,start,end)
print(result)
#7.finding the substring by using rfind
# to given the string last occurance of the substring value find() 
# if the value not availble returns   -1
word="python is a high level programming launguage"
sub_string="g"
find_substring=word.rfind(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.rfind(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.rfind(subString,start,end)
print(result)
#8.replacing the string(replace)
word="Iam Indian"
replace_word="Hindhu"
result=word.replace("Indian",replace_word)
print(result)


word_2="hii hii all of how are you hi what are"
replace_word_2="hello"
final_word=word_2.replace("hii",replace_word_2,2)
print(final_word)


word_3=input("enter the value:")
orginal_word=input("enter the changeWord:")
replace_word_3=input("enter the replaceword:")
occurance_value=int(input("enter the nbr"))
final_word=word_3.replace(orginal_word,replace_word,occurance_value)
print(final_word)

#9.splitting the string(split)

word="o cheliya naa priya sakiya"
result=word.split()
print(result)

second_result=word.split("a")
print(second_result)



word_2="ma@lo@th@Su@re@sh"
split_word=word_2.split("@")
print(split_word)

text="hello,i am suresh,25 years old,"
split_text=text.split(",")
print(split_text)

#max separation 
txt="sureshMalothHowareYou"
txt_sep=txt.split("o",2)
print(txt_sep)

#10.joining of string (join)
word="suresh"
char="-"
result=char.join(word)
print(result)


element=input("enter the element:")
value=input("enter the value:")
join_val=value.join(element)
print(join_val)

list_a=["ram","surya","abhi","chetan","srujan","venkat"]
join_word="ohm"
result=join_word.join(list_a)
print(result)