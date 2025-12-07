import math
import random
def randgen(n):
    counter = 0
    for i in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a**2+b**2)<=1:
            counter+=1
    c=4*counter/n
    return c
print('n=10',randgen(10))
print('n=1000',randgen(1000))
print('n=100000',randgen(100000))
print('n=10000000',randgen(10000000))
# ესა პი რიცხვის მიღების ერთ-ერთი მეთოდი.
# რაც უფრო მეტ იტერაციას ვაკეთებთ მიღებული შედეგი უფრო მეტად უახლოვდება პი-ს რეალურ მნიშვნელობას.