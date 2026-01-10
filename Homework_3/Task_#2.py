from collections import Counter

s1 = input('შეიყვანეთ პირველი სიტყვა: ').lower()
s2 = input('შეიყვანეთ მეორე მეორე: ').lower()

c1 = Counter(s1)
c2 = Counter(s2)

possible = c1==c2

if possible:
    print('Yes')
else:
    print('No')