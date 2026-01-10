import random
for i in range(1,11):
    A = int(random.randint(0, 10))
    B = int(random.randint(0, 10))
    c=int(input(f'Question #{i}: {A} * {B} = '))
    if A*B==c:
        print('Right!')
        continue
    else:
        print('Wrong. The answer is',A*B)

