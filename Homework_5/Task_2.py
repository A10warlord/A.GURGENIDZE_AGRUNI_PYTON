employees = [
{"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
{"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
{"name": "Charlie", "tasks": [8, 7, 6], "department": "IT"},
{"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"},
{"name": "George", "tasks": [2, 7, 6], "department": "IT"}
]

employees1=list(map(lambda x:{
    'name':x['name'], 'department':x['department'], 'average tasks':sum(x['tasks'])/len(x['tasks'])
},employees))
print(*employees1)
print('კლებადობით დალაგებული',sorted(employees1,key=lambda x:-x['average tasks']))
print('ყველაზე მაღალი საშუალოს მქონდე',max(employees1,key=lambda x:x['average tasks']))
print('ექვსზე მაღალი საშუალოს მქონდე',list(filter(lambda x:x['average tasks']>6,employees1)))