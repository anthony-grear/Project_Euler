#https://projecteuler.net/problem=18

#read in list of numbers
file = open('sum_path.txt', 'r')
digit_lines = file.readlines()

#strip the newlines from each line
strip_list=[]
for line in digit_lines:
  strip_list.append(line.strip())

#split into a list of lists
new_list=[]
for num_string in strip_list:
  new_list.append(num_string.split())

#change all strings to numbers
new_num_list=[list(map(int, x)) for x in new_list]
print(new_num_list)
print()


"""for each element in the second to last row, add to the element directly below, and then directly below and to the right. Compare the two sums. Whichever is larger, replace the element with the sum. Once this has been done for each element in the second to last row, then delete the last row and repeat the process. Stop when there is only one row left."""
while len(new_num_list)>1:
  for x in new_num_list[-2]:
    elem_index = new_num_list[-2].index(x)
    sum1= x + new_num_list[-1][elem_index]
    sum2= x + new_num_list[-1][elem_index + 1]
    if sum1>sum2:
      new_num_list[-2][elem_index] = sum1
    else:
      new_num_list[-2][elem_index] = sum2
  new_num_list.pop(-1)

print(new_num_list)
# arr = numpy.array(new_num_list, dtype=object)
# print(arr)
# for digits in digit_lines:
 
#   print(digits)

