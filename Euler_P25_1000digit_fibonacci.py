a=1
print(a)
b=1
print(b)
counter = 2
while True:
    
    c=b+a
    counter +=1
    print(c)
    c=str(c)
    if len(c) == 1000:
        print(f"{counter} is the answer.")
        break
    c=int(c)
    a=b
    b=c
print()
print()
print(f"Index of first fibonacci with 1000 digits = {counter}.")