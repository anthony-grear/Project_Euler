import copy
import time

def proper_divisors_list(number): 
    """Returns a list of proper divisors for a given number.""" 

    sqrt_number = number**(0.5) + 1 # square root + 1 
    factor_list = []
    for x in range(1, int(sqrt_number)): 
        if number % x == 0: 
            factor_list.append(x)
            factor_list.append(int(number/x)) 
    factor_list = list(set(factor_list)) 
    factor_list.sort()
    factor_list.pop()
    return factor_list 

def abundant_number_test(number, proper_divisors_list): 
    """Given a number and proper_divisors_list,
    return True if sum of proper_divisors_list is greater than number""" 
    
    if sum(proper_divisors_list) > number :
        return True 
    else: 
        return False 

def abundant_number_list(start, stop):
    """Creates a list of sorted abundant_numbers- *two instances of each number."""
    
    abundant_number_list = []
    for number in range(start,stop+1):
        proper_divisors = proper_divisors_list(number)
        abundant_number_test_result = abundant_number_test(number, proper_divisors)
        if abundant_number_test_result == True:
            abundant_number_list.append(number)
    abundant_number_list_copy = copy.deepcopy(abundant_number_list)
    abundant_number_list += abundant_number_list_copy 
    abundant_number_list.sort()
    return abundant_number_list 



def abundant_sum_test(number, abundant_number_list, start=0, end=-1):
    """Returns True if a number is the sum of two abundant numbers."""

    a_n_list = abundant_number_list
    while True:
        if start > (len(a_n_list) -1):  #no abundant sum found          
            if start > (len(a_n_list)-1):
                start -= 1
            if end < ((-1)*(len(a_n_list)) ):
                end += 1
            print(f"<condition1>Non-abundant Sum: {number} != {a_n_list[start]} + {a_n_list[end]}")
            return False 
        
        if end < ((-1)*(len(a_n_list)) ): #no abundant sum found           
            if start > (len(a_n_list)-1):
                start -= 1
            if end < ((-1)*(len(a_n_list)) ):
                end += 1
            print(f"<condition2>Non-abundant Sum: {number} != {a_n_list[start]} + {a_n_list[end]}")
            return False
        
        if a_n_list[start] + a_n_list[end] > number:  #if higher than number start working backwards from the end of list
            print(f"{a_n_list[start]} + {a_n_list[end]} > {number}")
            end -= 1
            continue
        if a_n_list[start] + a_n_list[end] < number: #if lower than number start working forwards from the beginning of the list 
            print(f"{a_n_list[start]} + {a_n_list[end]} < {number}")
            start += 1
            continue 
        
        if a_n_list[start] + a_n_list[end] == number:  #an abundant sum has been found 
            print(f"Abundant Sum: {number} = {a_n_list[start]} + {a_n_list[end]}")
            return True 
        else: #no abundant sum found
            
            if start > (len(a_n_list)-1):
                start -= 1
            if end < ((-1)*(len(a_n_list)) ):
                end += 1
            print(f"<condition3> Non-abundant Sum: {number} != {a_n_list[start]} + {a_n_list[end]}")
            return False

    
         


if __name__ == '__main__':
    
    abundant_numbers = abundant_number_list(1,28124)
    for number in reversed(range(1,28124)):
        abundant_sum_test_result = abundant_sum_test(number, abundant_numbers)      
        if abundant_sum_test_result == False: 
            print(f"The max non_abundant sum: {number}")
            break
    
    non_abundant_sums = []
    abundant_numbers = abundant_number_list(1,20162)
    for number in (range(1,20162)):  
        abundant_sum_test_result = abundant_sum_test(number, abundant_numbers)      
        if abundant_sum_test_result == False:
            non_abundant_sums.append(number)
            print(non_abundant_sums)
            time.sleep(0.3)
            
    print(non_abundant_sums)
    print(len(non_abundant_sums))
    print(sum(non_abundant_sums))
    
            
        
        
            
    
