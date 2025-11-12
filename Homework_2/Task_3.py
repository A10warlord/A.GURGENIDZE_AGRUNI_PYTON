import random
A=random.randrange(1,4)
B=random.randrange(1,4)
C=random.randrange(1,4)
D=random.randrange(1,4)
E=random.randrange(1,4)
List=[A,B,C,D,E]
New_list=[]
for i in List:
    New_list.extend([i]*i)
print(New_list)
print('Length: ', len(New_list))