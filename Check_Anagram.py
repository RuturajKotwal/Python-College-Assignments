str1 = input("Enter 1st string : ")
list1 = list(str1)
str2 = input("Enter 2nd string : ")
list2 = list(str2)

if str1 == '' or str2 == '' :
	print("Error occured")
	exit()

if len(str1) != len(str2) :
	print("Not an anagram")
	exit()

flag = 1
for element in list1 :
	if element not in list2 :
		flag = 0
		break
	else :
		list2.remove(element)
		
if flag == 0 :
	print("Not an anagram")
else :
	print("It is an anagram")