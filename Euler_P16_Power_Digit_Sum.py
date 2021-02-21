import numpy as np 
arr = np.full((100), (2**10), dtype=object)
print(arr)
print(type(arr))
product = (np.prod(arr, dtype=object))

print(type(product))
num_list = (list(str(product)))
num_list = list(map(int, (num_list)))
print(num_list)
print(sum(num_list))
