from functools import reduce

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]
products1=list(filter(lambda y:y[2]>0,products)) #მარაგში არ არის
print(products1)
print(list(map(lambda y:(y[0],round((y[1]*y[2]),2)),products1))) #ჯამური ფასი
total_price = reduce(
    lambda acc, item: acc + (item[1] * item[2] if item[2] > 0 else 0),
    products,
    0
)
print(total_price) #ჯამური ფასი 2
