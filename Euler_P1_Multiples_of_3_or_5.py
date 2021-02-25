#Find the sum of the multiples of 3 or 5 less than 1000
#answer = 233168

mult_3_or_5 = [x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(mult_3_or_5))
