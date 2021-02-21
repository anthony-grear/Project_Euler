import numpy as np

#read the large number from a text file
f = open('large_sum.txt','r' )
list_of_lines = f.readlines()

#strip the newlines from each line (except the last line)
converted_list= [] 
for line in list_of_lines:
  converted_list.append(line.strip())

#split each string into individual characters
split_list = []
for long_string in converted_list:
  split_list.append(list(long_string))

#convert each string to an integer
integer_list = []
for line in split_list:
 integer_list.append(list(map(int, line)))

#convert to 2d array
arr = np.array(integer_list)

#find the sum of each column
column_sums = arr.sum(axis=0)
column_sums = column_sums.tolist()
column_sums.reverse()


place_value_list = []
counter=0
#execute carrying over place values until the 2nd to last number
for total in column_sums:
  counter+=1
  if counter == 50:
    break
  place_value_list.append(total % 10)
  column_sums[counter]+= (total // 10)

#finish carrying over manually for the last place values
#print(divmod(column_sums[49],10))
#print(divmod(55, 10))
#print(divmod(5, 10))
place_value_list.append(3)
place_value_list.append(5)
place_value_list.append(5)

place_value_list.reverse()
print(place_value_list[0:10])
print(len(place_value_list))





