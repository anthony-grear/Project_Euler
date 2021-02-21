import numpy as np

def track_collatz(num):
  """return length of collatz chain"""

  if num==1:
    return 1
  
  counter=1
  while num!=1:
    if num%2==0:
      num/=2
      counter+=1
    elif num%2==1:
      num = 3*num + 1
      counter+=1
  if num==1 and counter>0:
    return counter

arr= np.array(range(800000,900000))
vfunc_collatz=np.vectorize(track_collatz)
chain_length = vfunc_collatz(arr)
max_length = np.amax(chain_length)
index_value = np.where(chain_length == max_length)
print(f'The longest chain: {max_length}')
#print(index_value)
print(f'Starting value: {arr[index_value]}')


