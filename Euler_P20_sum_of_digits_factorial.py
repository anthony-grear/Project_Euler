import numpy as np 
import math

arr = np.array(math.factorial(100), dtype='O')
str_arr = np.array_str(arr)
str_arr = list(str_arr)
str_arr = list(map(int, str_arr))
print(sum(str_arr))