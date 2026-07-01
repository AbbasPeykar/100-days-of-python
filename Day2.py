# Tip Calculator

print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_person = total_bill / people

print(f"Each person should pay: ${each_person}")