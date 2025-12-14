n=int(input('Please enter a number: '))
a,b=1,1
sia=[]
sia.append(a)
sia.append(a)
if n<0:
    print('Please enter positive number')
elif n==0:
    sia.append(a)
    sia.append(a)
    print(*sia,end='')
else:
    for i in range(n):
        a,b=b,a+b
        sia.append(b)
print(*sia)