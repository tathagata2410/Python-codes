import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hours = int(time.strftime('%H'))
print(hours)

minutes = int(time.strftime('%M'))
print(minutes)

seconds = int(time.strftime('%S'))
print(seconds)

# https://docs.python.org/3/library/time.html#time.strftime

if hours < 12:
    print("Good Morning")
elif hours == 12 and minutes == 0:
    print("Good Noon")
elif hours >= 18:
    print("Good Evening")
else:
    print("Good Night")
