def encrypt(text):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = ""

    for ch in text:
        if ch.islower():  # მხოლოდ დაბალი რეგისტრის ასოები
            for row in keyboard:
                if ch in row:
                    i = row.index(ch)
                    result += row[(i + 1) % len(row)]  # მარჯვნივ წანაცვლება
                    break
        else:
            result += ch  # სხვა სიმბოლო უცვლელად
    return result


def decrypt(text):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = ""

    for ch in text:
        if ch.islower():
            for row in keyboard:
                if ch in row:
                    i = row.index(ch)
                    result += row[(i - 1) % len(row)]  # მარცხნივ წანაცვლება
                    break
        else:
            result += ch
    return result


# მთავარი პროგრამა
while True:
    action = input("Enter action (e/d): ").strip().lower()
    if action in ("e", "d"):
        break
    print("Invalid input! Please enter 'e' for encrypt or 'd' for decrypt.")

text = input("Enter text: ")

if action == "e":
    print(encrypt(text))
else:
    print(decrypt(text))
