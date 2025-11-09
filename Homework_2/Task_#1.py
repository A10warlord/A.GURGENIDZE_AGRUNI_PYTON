while True:
    year1 = int(input('გთხოვთ შეიყვანოთ წელიწადი: '))
    if  year1 <= 0:
        print('გთხოვთ შეიყვანოთ სწორი პარამეტრი')
        continue
    break
if year1%400 <=0 or year1%4 <= 0 < year1%100:
       print('წელიწადი კანიანია')
else:
       print('წელიწადი ნაკიანი არ არის')
