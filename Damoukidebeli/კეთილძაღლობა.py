highest=int(input('Please Enter the score: '))
lowest=highest
highhold=highest
lowhold=lowest
s=highest
c=0
c2=1
if highest>100:
    c=c+1
for i in range(2,11):
    score=int(input('Please Enter the score: '))
    s=s+score
    c2=c2+1
    if score >100:
        c=i
    if score>highest:
        highhold=highest
        highest=score
    if score<lowest:
        lowhold=lowest
        lowest=score
avarage=s/c2

print('Highest score is: ',highest, 'Lowest score is:',lowest,'AVG=',avarage.__round__(2), sep='\n')
if c>0:
    print(f'user has value over 100')
print(highhold,lowhold)
