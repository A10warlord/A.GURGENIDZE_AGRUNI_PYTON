import json
# დაგროვება
max_single_amount = {}
total_user_cost = {}
product_sales = {}

total_cost_sum = 0
total_amount_sum = 0
purchase_count = 0

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        user, product, amount, price = line.split(",")
        amount = int(amount)
        price = float(price)

        cost = amount * price

        # a) მაქსიმალური რაოდენობა ერთ შესყიდვაში (user-ზე)
        max_single_amount[user] = max(
            max_single_amount.get(user, 0),
            amount
        )

        # b) მომხმარებლის ჯამური ღირებულება
        total_user_cost[user] = total_user_cost.get(user, 0) + cost

        # e) პროდუქტის გაყიდვების რაოდენობა
        product_sales[product] = product_sales.get(product, 0) + amount

        # c, d მონაცემები
        total_cost_sum += cost
        total_amount_sum += amount
        purchase_count += 1


# a) მაქსიმალური რაოდენობა ერთ შესყიდვაში ---
max_amount_value = max(max_single_amount.values())
max_amount_users = [
    user for user, val in max_single_amount.items()
    if val == max_amount_value
]

# b) მაქსიმალური ჯამური ღირებულება ---
max_cost_value = max(total_user_cost.values())
max_cost_users = [
    user for user, val in total_user_cost.items()
    if val == max_cost_value
]

# c) საშუალო ღირებულება ---
average_cost = total_cost_sum / purchase_count if purchase_count else 0

# d) საშუალო რაოდენობა ---
average_amount = total_amount_sum / purchase_count if purchase_count else 0

# e) ყველაზე გაყიდვადი პროდუქტი ---
max_product_amount = max(product_sales.values())
top_products = [
    product for product, val in product_sales.items()
    if val == max_product_amount
]

# საბოლოო სტატისტიკა
stats = {
    "max_single_purchase_amount": {
        "amount": max_amount_value,
        "users": max_amount_users
    },
    "max_total_purchase_cost": {
        "cost": round(max_cost_value, 2),
        "users": max_cost_users
    },
    "average_purchase_cost": round(average_cost, 2),
    "average_purchase_amount": round(average_amount, 2),
    "top_selling_products": {
        "amount": max_product_amount,
        "products": top_products
    }
}

# ჩაწერა JSON ფაილში
with open("stats.json", "w", encoding="utf-8") as json_file:
    json.dump(stats, json_file, indent=4, ensure_ascii=False)
