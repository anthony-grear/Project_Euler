#Find the sum of the even fibonacci numbers less than 4 million
#answer = 3_524_578

fib_numbers=[1,1]
a=1
b=1

while True:
	a,b=b,a+b
	if b%2==0 and b<4000000:
		fib_numbers.append(b)
	
	
	if b>=4000000:
		break

fib_numbers.remove(1)
fib_numbers.remove(1)
print(fib_numbers)
print(sum(fib_numbers))

    
