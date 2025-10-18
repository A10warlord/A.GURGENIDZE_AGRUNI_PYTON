a=1
print(id(a))

a=1
print(id(a))

a=12
print(id(a))

b=[1,2]
print(id(b))

b.append(5)
print(id(b))

c=a
a=10
print(a,c)

d=[1,2]
print(id(d))
d.append(3)
print(id(d),id(r))



