from gdc import gcd
def lcm(a, b):
    return a * b // gcd(a, b)
a = int(input('ჩაწერეთ a: '))
b = int(input('ჩაწერეთ b: '))
if a < 1 or b < 1 or a > 10000 or b > 10000:
    print('გთხოვთ შეიყვანოთ ნატურალური რიცხვები 1 - დან 10000 - მდე.')
else:
    result = lcm(a, b)
    print(f'LCM of {a} and {b} is {result}.')