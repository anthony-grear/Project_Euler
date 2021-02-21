import numpy as np

def compute_triangular_num(nth_index):
  """returns the nth triangular number"""
  return int((nth_index*(nth_index+1))/2)

def factors(n):
    return len(set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i))
    )


# arr = np.array([np.array(compute_triangular_num(x)) for x in range(10900,20001)])
# print(arr[1475])
# print()
# vfunc=np.vectorize(factors)
# fact_tri_nums = vfunc(arr)
# print(max(fact_tri_nums))
# print()
# result = np.where(fact_tri_nums > 500)
# print(result)

print(factors(76576500))






































# def get_factors(number):
#   """returns a list of factors"""
#   n=0
#   factor_list=[]
#   while n**2 <= number:
#     n+=1
#     if n**2 == number:
#       factor_list.append(number)
#     if number%n==0:
#       if n in factor_list:
#         continue
#       factor_list.append(n) 
#       factor_list.append(int(number/n)) 
#   factor_list = list(set(factor_list))
#   factor_list.sort()
#   return factor_list



# print(get_factors(166))
  


  