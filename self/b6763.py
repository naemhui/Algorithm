limit = int(input())
speed = int(input())

how = speed - limit
if how >= 1 and how <= 20:
    fine = 100
elif how >= 21 and how <= 30:
    fine = 270
elif how >= 31:
    fine = 500

if speed <= limit:
    print("Congratulations, you are within the speed limit!")
else:
    print(f"You are speeding and your fine is ${fine}.")