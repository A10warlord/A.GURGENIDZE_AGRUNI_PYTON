N=int(input('Enter number: '))
if N > 1000 or N<0:
    print('Wrong Number')
else:
     for i in range(1,N+1):
       if not N%i:
           print(i,end=' ')