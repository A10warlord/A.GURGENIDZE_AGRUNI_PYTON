def typeofnumber(n):
    if n<0:
        return False
    if n==1 or n==0:
        return 'არც შედგენილია და არ მარტივი'
    if n==2:
        return True
    if n%2==0:
        return False
    if n>=3:
        while i < n:
           if n%i==0:
            return False
    return True

rincxvebi=[1,5,12,22,21,75]
for i in rincxvebi:
    print(i, typeofnumber(i))