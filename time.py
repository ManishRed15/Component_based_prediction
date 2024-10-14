from datetime import datetime

# datetime object containing current date and time
now = datetime.now()


print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
print('date',date)
print('time',time)
print("date and time =", dt_string)	