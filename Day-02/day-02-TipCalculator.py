#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10%, 12% or 15%? ")
no_of_people = input("How many people to split the bill? ")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip = (int(tip_percent)/100) + 1
payment = (float(bill)*tip)/float(no_of_people)
#Format the result to 2 decimal places = 33.60
payment_rounded = round(payment,2)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
message = f" Each person should pay ${payment_rounded}"
print(message)