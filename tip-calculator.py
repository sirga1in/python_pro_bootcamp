bill = input("What is your total bill?\n")
tips = input("What percentage tip?\n")
bill_to_float = float(bill)
tips_to_float = float(tips)
ammount_of_tips = bill_to_float * tips_to_float / 100

total_bill = bill_to_float + ammount_of_tips
split_bill = input("How many people to split the bill\n")
person_pay = round(total_bill / int(split_bill), 2)
print(f"Each person should pay {person_pay} dollars")
