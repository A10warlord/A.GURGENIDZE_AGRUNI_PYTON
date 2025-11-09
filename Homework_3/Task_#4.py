def encrypt(text):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = ""

    for ch in text:
        if ch.islower():  # ეხება მხოლოდ დაბალ სიმბოლოებს
            for row in keyboard:
                if ch in row:
                    i = row.index(ch)
                    result += row[(i + 1) % len(row)]  # ანაცვლებს ამრჯვნივ
                    break
        else:
            result += ch  # დანარჩენი სიმბობლოები გადმოაქვს უცვლელად
    return result
def decrypt(text):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = ""

    for ch in text:
        if ch.islower():
            for row in keyboard:
                if ch in row:
                    i = row.index(ch)
                    result += row[(i - 1) % len(row)]  # ეს ფუნქცია ანაცვლებს მარცხნივ
                    break
        else:
            result += ch
    return result
# მთრავარი პროგრამა While ციკლში
while True:
    action = input("Enter action (e/d): ").strip().lower()
    if action in ("e", "d"):
        break
    print("Please enter e or d")

text = input("Enter text: ")

if action == "e":
    print(encrypt(text))
else:
    print(decrypt(text))
