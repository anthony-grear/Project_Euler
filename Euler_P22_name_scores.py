import string

f = open("p022_names.txt", 'r')
name_list = f.readlines()

name_list = name_list[0].split(",")
name_list = [x.replace('"', '') for x in name_list]
name_list = sorted(name_list)

alpha_dict = dict(enumerate(string.ascii_uppercase, start=1))
alpha_dict = dict((y,x) for x,y in alpha_dict.items())

name_list = [list(x) for x in name_list]
#print(alpha_dict)
num_name_list = []
for name in name_list:
	temp_list = []
	for letter in name:
		temp_list.append(alpha_dict.get(letter))
	num_name_list.append(temp_list)

# for x in num_name_list:
# 	print(x)

sum_list = []
for x in num_name_list:
	sum_list.append(sum(x))

product_list = []
for x in range(1, (len(sum_list) + 1)):
	product_list.append(x * sum_list[x-1])

print(sum(product_list))