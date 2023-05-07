age = input("What is your current age?\n")
day = (90 - int(age))*365
week = (90 - int(age))*54
year = 90 - int(age)
if year != 1:
  print(f"You have {day} days, {week} weeks, {year} years left")
else:
  print(f"You have {day} days, {week} weeks, {year} year left")