inp=input('Please insert the text: ')
cap=inp.title()
sia=[]
sia2=[]
for i in range(len(cap)):
    if cap[i].isalpha():
        sia.append(cap[i])
s=''.join(sia)
for j in range(len(s)):
    if s[j].isupper():
       sia2.append(s[j])
print(*sia2, sep='')

