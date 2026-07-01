#Welcome to the Tip Calculator!

#What was the total bill? 150

#How much tip would you like to give? 10

#How many people to split the bill? 3

#Each person should pay: 55.0

bill = float(input("Enter your bill: "))
tip = float(input("Enter your tip percentage: "))
people = int(input("Enter number of people: "))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_person = total_bill / people

print(tip_amount)
print(total_bill)


print(f"Each person should pay: {each_person}")