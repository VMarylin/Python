f the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip = (int(tip_percent)/100) + 1
total_bill = (bill*tip) + bill
bill_per_person = total_bill/no_of_people
#Format the result to 2 decimal places = 33.60
payment_rounded = round(bill_per_person,2)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
message = f" Each person should pay ${bill_per_person}"
print(message)