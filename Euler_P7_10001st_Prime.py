#What is the 10 001st prime number?

def prime_number_generator():
	"""returns a generator of prime numbers"""

	dividend = 2
	divisor = 1

	while True:
		factor_counter = 0
		while dividend >= divisor:
			if dividend%divisor==0:
				factor_counter+=1
			divisor+=1
		if factor_counter == 2:
			yield dividend
		dividend+=1
		divisor = 1


infinite_prime_gen = prime_number_generator()

max_limit = 0
with open('output.txt','w') as f:
	while max_limit<10001:
		max_limit +=1
		print(f'{max_limit}')
		f.write((f'Prime Number {max_limit} is: ' + str(next(infinite_prime_gen))+'\n'))

	