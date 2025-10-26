import math

A=float(input('Edge A: '))
B=float(input('Edge B: '))
C=float(input('Base C: '))
if A+B<C or A+C<B or C+B<A:
    print('Wrong parameter')
else:
    P=A+B+C
    S=P/2
    Area=math.sqrt(S*(S-A)*(S-B)*(S-C))
    print('Rectangle Area is: ',Area)
    print('Rectangle Perimeter is: ',P)