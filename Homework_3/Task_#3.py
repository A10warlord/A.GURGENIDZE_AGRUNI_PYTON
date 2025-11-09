from datetime import datetime
date_str = "2024-03-22T13:07:40.956376+10:00"
dt = datetime.fromisoformat(date_str)
# UTC offset-ის გამოთვლა საათებში
offset = dt.utcoffset()
if offset is not None:
    hours = int(offset.total_seconds() / 3600)
    tz_str = f"{hours:+d}"
else:
    tz_str = ""
# საბოლოო ფორმატირება
formatted = f"{dt.strftime('%d-%m-%Y %I:%M:%S')} {tz_str}"
# მოვაცილოთ 0 საათში
divided=formatted.split()
Time=divided[1]
if Time[0]=='0':
    Time1=Time[1:]
    print(divided[0]+' '+Time1+' '+divided[2])
else:
    print(formatted)