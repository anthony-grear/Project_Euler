#Find the sum of all the primes below two million.

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(primes(1000000))

prime_list = primes(2000000)
print(prime_list)
print(sum(prime_list))


output_file = open('output.txt','w')
output_file.write(str(prime_list))
output_file.write(f'The sum of the primes below 2,000,000 is {str(sum(prime_list))}.')
output_file.close()
