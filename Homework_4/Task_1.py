def typeofnumber(n):
    if n<0:
        return False
    if n==1 or n==0:
        return 'არც შედგენილია და არ მარტივი'
    if n==2:
        return True
    if n%2==0:
        return False
    i=3
    while i < n:
        if n%i==0:
            i+=2
            return False
    return True
rincxvebi=[1,0,27,12,15,-12]
for i in rincxvebi:
    print(i, typeofnumber(i))