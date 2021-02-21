#Find the largest palindrome made from the product of two 3-digit numbers.
palindrome_list=[]
for x in range(100,1000):
	for y in range(100,1000):
		product = x*y
		product = str(product)
		if len(product)==5:
			if product[0]==product[4] and product[1]==product[3]:
				palindrome_list.append(product)
		if len(product)==6:
			if product[0]==product[5] and product[1]==product[4] and product[2]==product[3]:
				palindrome_list.append(product)

palindrome_number_list=[]
for number in palindrome_list:
	number= int(number)
	palindrome_number_list.append(number)


palindrome_number_list= list(dict.fromkeys(palindrome_number_list))
palindrome_number_list.sort()
print(palindrome_number_list)
print(max(palindrome_number_list))