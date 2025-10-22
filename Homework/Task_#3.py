n=int(input('Enter a number: '))
n1, n2 = 0, 1
count=0
if n<0 or n>100:
    print('Wrong number')
elif n==1:
    print('Pibonachi',n,':')
    print(n1)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
