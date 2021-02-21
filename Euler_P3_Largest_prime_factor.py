#What is the largest prime factor of the number 600851475143 ?

#Answer = 6857

def prime_number_list(length):
	"""generates a list of prime numbers to a specified length"""
	
	dividend=2
	divisor=1

	while True:
		factor_counter = 0
		while dividend >= divisor:
			if dividend%divisor == 0:
				factor_counter+=1
			divisor+=1
		if factor_counter==2:
			yield dividend
		dividend+=1
		divisor=1
		if dividend == length:
			break

target = 600851475143
prime_factor_list=[]
sqrt_target=int(target**(0.5))
prime_list = prime_number_list(sqrt_target)	
current_prime = (next(prime_list))

while True:
	if target == 1:
		break
	elif target % current_prime == 0:
		prime_factor_list.append(current_prime)
		target/=current_prime
	else:
		current_prime = (next(prime_list))	

print(prime_factor_list)
print(max(prime_factor_list))
