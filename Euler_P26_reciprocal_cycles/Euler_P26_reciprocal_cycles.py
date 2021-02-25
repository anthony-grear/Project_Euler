import math
import copy

def create_factor_list(number):
    """Returns a list of factors when given a positive integer."""

    factor_list = []    
    if number < 1:
            raise ValueError("Please enter a positive integer.")
    if isinstance(number, float):
            raise ValueError("Please enter a positive integer.")
    sqrt_number = int(number**(0.5))
    for x in range(1,sqrt_number + 1):
        if number % x == 0:
            factor_list.append(x)
            factor_list.append(number//x)
    factor_list = list(set(factor_list))        
    return factor_list

def gcd(value_1, value_2):
    """Returns the greatest common divisor of two numbers."""

    if value_1 < 1 or value_2 < 1:
            raise ValueError("Please enter a positive integer.")
    if isinstance(value_1, float):
            raise ValueError("Please enter a positive integer.")
    if isinstance(value_2, float):
            raise ValueError("Please enter a positive integer.")
    while True:
        
        result = divmod(value_1, value_2)        
        if result[1]==0:
            return value_2
        value_1 = value_2
        value_2 = result[1]

def coprime_test(value_1,value_2):
    """Returns True if GCD(value_1, value_2)=1. False if not."""
    if gcd(value_1, value_2) == 1:
        return True
    else:
        return False

def create_prime_list(max_value):
    """Returns a list of primes that occur less than or equal to max_value."""
    prime_list = []
    for x in range(2,max_value+1):
        temp_list = create_factor_list(x)
        if len(temp_list)==2:
            prime_list.append(x)
    return(prime_list)

def create_prime_factors_list(number):
    """returns a list of prime factors for a number."""
    prime_factor_list = []
    prime_list = create_prime_list(number)
    for x in prime_list:
        while True:
            if number % x == 0:
                prime_factor_list.append(x)
                number = int(number/x)
                continue
            else:
                break
    prime_factor_list = list(set(prime_factor_list))
    if 1 in prime_factor_list:
        prime_factor_list.remove(1)
    return prime_factor_list

def create_totient_list(value):
    """Returns a list of totients for a given number."""
    totient_list=[]
    for x in range(1,value+1):
        if gcd(value, x)==1:
            totient_list.append(x)
    return totient_list

def prime_factorization(value):
    """Returns a list containing the prime factorization of a positive int."""
    prime_factorization = []
    prime_list = create_prime_list(value)
    for x in prime_list:
        while True:
            if value % x == 0:
                prime_factorization.append(x)
                value = int(value/x)
                continue
            else:
                break
    
    if 1 in prime_factorization:
        prime_factorization.remove(1)
    return prime_factorization

def do_mod_multiplication(A,B,C):
    """Simplifies and calculates mod multiplication. (A^B mod C)"""
    from math import prod
    binary_B = bin(B)
    binary_B = list(str(binary_B))
    binary_B = binary_B[2:]
    binary_B = list(map(int, binary_B))
    binary_B.reverse()
    power_2_list=[]
    counter=0
    for x in binary_B:
        if x==1:
            power_2_list.append(2**counter)
        counter+=1
    binary_B.reverse()
    power_2_list.reverse()
    simplified_power_2_list=[]
    for x in power_2_list:
        if x>4:
            number_of_fours=int(x/4)
            while number_of_fours>0:
                simplified_power_2_list.append(4)
                number_of_fours -= 1
        if x==4:
            simplified_power_2_list.append(4)
        if x<4:
            simplified_power_2_list.append(x)

    running_remainders=[]
    for x in simplified_power_2_list:
        running_remainders.append((A**x)%C)

    return (prod(running_remainders)%C)

def check_terminating_denominators(d):
    """Return True if given denominator has only factors of 2 or 5."""
    prime_factors_list= create_prime_factors_list(d)
    if len(prime_factors_list)==1:
        if prime_factors_list == []:
            return None
        if 2 in prime_factors_list:            
            return True
        if 5 in prime_factors_list:
            return True
        else:
            return False
    if len(prime_factors_list)==2:
        if 2 in prime_factors_list and 5 in prime_factors_list:
            return True
        else:
            return False
    if len(prime_factors_list)>2:
        return False

def remove_terminating_denominators(number_list):
    """Returns a list of numbers after removing
    those with strictly prime factors of 2 and/or 5."""
    repeating_denominators_only=[]
    for number in number_list:
        if check_terminating_denominators(number)==False:
            repeating_denominators_only.append(number)
    return repeating_denominators_only



    
list_of_denominators = list(range(2,1000))
list_of_denominators = remove_terminating_denominators(list_of_denominators)
list_of_denominators_and_period_lengths=[]
for d in list_of_denominators:

    original_d = copy.deepcopy(d)
    totient_func_value = len(create_totient_list(d))
    
    #cleans twos and fives out of denominators that have additional factors
    prime_factorized_d = prime_factorization(d)
    
    if 2 in prime_factorized_d or 5 in prime_factorized_d:
        while 2 in prime_factorized_d:
            prime_factorized_d.remove(2)

        while 5 in prime_factorized_d:
            prime_factorized_d.remove(5)
        temp_d = math.prod(prime_factorized_d)
        totient_func_value = len(create_totient_list(temp_d))
        d = temp_d    
                
    factors_of_totient_func_value = create_factor_list(totient_func_value)
    factors_of_totient_func_value.sort()
    for factor in factors_of_totient_func_value:
        result_of_mod_mult = do_mod_multiplication(10,factor,d)
        if result_of_mod_mult == 1:            
            list_of_denominators_and_period_lengths.append((original_d,factor))
            break

for data in list_of_denominators_and_period_lengths:
    print(data)

    
    
