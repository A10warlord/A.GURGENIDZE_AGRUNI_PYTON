high=int(input('Please enter a high: '))
tvla=(high//2)+1
for i in range(1,high,2):
    biji=tvla-1
    tvla=biji
    print(' '*biji,'*'*i)
count=0
for i in range(0,high,2):
    biji=count+1
    count=biji
    print(' '*biji+'*'*(high-i))