with open("data.txt", "r", encoding="utf-8") as infile, \
     open("small.txt", "w", encoding="utf-8") as small_file, \
     open("high.txt", "w", encoding="utf-8") as high_file:

    for line in infile:
        line = line.strip()
        if not line:
            continue  # ცარიელი ხაზის გამოტოვება

        user, product, amount, price = line.split(",")

        amount = int(amount)
        price = float(price)

        total_cost = amount * price

        if total_cost < 10:
            small_file.write(line + "\n")
        else:
            high_file.write(line + "\n")
