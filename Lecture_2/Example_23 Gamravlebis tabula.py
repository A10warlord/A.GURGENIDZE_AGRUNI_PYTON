from itertools import product

for i in range(1,10):
    print(i, '-', end=' ')
    for j in range(1,10):
        product= i * j
        if product <10:
            product=' '+str(product)
        print(product, end=' ')
    print()