def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input('ჩაწერეთ a: '))
b = int(input('ჩაწერეთ b: '))
if a < 1 or b < 1 or a > 10000 or b > 10000:
    print('გთხოვთ შეიყვანოთ ნატურალური რიცხვები 1 - დან 10000 - მდე.')
else:
    result = gcd(a, b)
    print(f'GCD of {a} and {b} is {result}.')