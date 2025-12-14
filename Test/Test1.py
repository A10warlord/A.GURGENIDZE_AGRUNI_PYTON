import csv
filename="user2.csv"
users=[
    {"name":"aladina","age":32},
    {"name":"gia","age":69},
    {"name":"nino","age":58}
]
user={"name":"aladina","age":32}
with open(filename,'w',newline='') as file:
    column=['name','age']
    writer=csv.DictWriter(file,fieldnames=column)
    writer.writeheader()
    writer.writerow(users)