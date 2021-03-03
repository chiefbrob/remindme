import time

print("What shall I remind you about?")

reminder = str(input())
print("in how many minutes?")
minutes = float(input())
time.sleep(minutes * 60)

print(reminder)