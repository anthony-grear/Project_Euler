"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def norm_easy_to_read(vector, p=2):
  """returns p_norm or default Euclidean norm of a vector"""
  temp_list=[]
  for i in range(len(vector)):
    temp_list.append((abs(vector[i]))**p) #abs each element raised to p
  return (sum(temp_list)**(1/p))




	
for a in range(1,1001):
	for b in range(1,1001):
		if (a + b + norm_easy_to_read([a,b])) == 1000.0:
			print([a,b])
			break

print(1000-200-375)
print(200*375*425)