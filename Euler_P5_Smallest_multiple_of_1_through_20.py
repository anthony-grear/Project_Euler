#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
value = 9699690 #product of primes less than 20
smallest_multiple=[]
while True:
	print(value)
	if (value%2==0 and value%3==0 and value%4==0 and 
	   value%5==0 and value%6==0 and value%7==0 and
	   value%8==0 and value%9==0 and value%10==0 and
	   value%11==0 and value%12==0 and value%13==0 and
	   value%14==0 and value%15==0 and value%16==0 and
	   value%17==0 and value%18==0 and value%19==0 and
	   value%20==0):
	   smallest_multiple.append(value)
	   break
	value+=9699690
print(smallest_multiple)
x=input()