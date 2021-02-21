number_dict ={1:'one', 2:'two', 3:'three', 4:'four',
                   5:'five', 6:'six', 7:'seven', 8:'eight',
                   9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
                   13:'thirteen', 14:'fourteen', 15:'fifteen',
                   16:'sixteen', 17:'seventeen', 18:'eighteen',
                   19:'nineteen', 20:'twenty', 30:'thirty', 
                   40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
                   80:'eighty', 90:'ninety', 100:'onehundred', 200:'twohundred', 300:'threehundred', 400:'fourhundred', 500:'fivehundred',600:'sixhundred',
                   700:'sevenhundred', 800:'eighthundred', 900:'ninehundred', 1000:'onethousand',
                   'and':'and'
                  }

def num_to_val(num):
    """return place values for each number"""

    num = list(str(num))
    num.reverse()
    num = list(map(int, num))
    power = 0
    num_list=[]
    for val in num:
      num_list.append(val*(10**power))
      power+=1
    num_list.reverse()
    num_list=[x for x in num_list if x!=0]
    if len(num_list)==3 and num_list[1]==10:
      del num_list[1]
      num_list[1]+=10
    if len(num_list)==2 and num_list[0]==10:
      del num_list[0]
      num_list[0]+=10
    
    return (num_list)

def num_to_word(num_list):
  """convert number to words using dictionary"""
  
  word_list=[]
  for num in num_list:
    word_list.append(number_dict.get(num))
  return word_list

all_nums=[]
for x in range(1,1001):
  all_nums.append(num_to_val(x))

for z in all_nums: 
  if z[0]>=100 and len(z)>1:
    z.insert(1, 'and')

all_word_list=[]
for w in all_nums:
  all_word_list.append(num_to_word(w))



joined_word_list=[]
for p in all_word_list:
  joined_word_list.append(''.join(p))

counter=0
for a in joined_word_list:
  counter+=len(a)
  print(a)

print(counter)




