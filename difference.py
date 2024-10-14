from datetime import datetime
NUMBER_OF_SECONDS = 86400 # seconds in 24 hours
first = datetime(2022, 10, 21,15,57,44)
second = datetime(2022, 10, 22,16,24,45)
print((second - first).total_seconds())
if (second - first).total_seconds() > NUMBER_OF_SECONDS:
  print("its been over a day!")
