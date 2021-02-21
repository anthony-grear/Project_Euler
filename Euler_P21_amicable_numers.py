def divisors(number):
  """return a list of divisors"""

  divisor_list= []
  sqrt = int(number**(0.5))
  for x in range(1, sqrt+1):
    if (number % x) == 0:
      divisor_list.append(x)
      divisor_list.append(int(number/x))
  divisor_list = list(set(divisor_list))
  divisor_list.sort()
  if len(divisor_list) > 1:
    divisor_list.pop()
  return divisor_list

# print(divisors(220))

amicable_numbers = []
for x in range(2,10000):
  ami_2 = sum(divisors(x))
  ami_1 = sum(divisors(ami_2))
  if ami_1 == x and ami_1 != ami_2:
    amicable_numbers.append(ami_1)
    amicable_numbers.append(ami_2)

amicable_numbers = list(set(amicable_numbers))
amicable_numbers.sort()
print((amicable_numbers))
print(sum(amicable_numbers))


