distance = float(input("How far would you like to travel in miles? "))

if abs(distance) < 3:
    print("I suggest Bicycle to your destination")
elif abs(distance) < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")