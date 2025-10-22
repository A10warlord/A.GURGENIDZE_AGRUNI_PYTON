N=int(input('Enter number: '))
if N > 1000:
    print('Number is greater than 1000')
else:
     for i in range(1,N+1):
       if not N%i:
           print(i,end=' ')