# input the user's age
age = input("What is your current age?")

#the total age is assumed to be 90 years
t_age = 90
t_age_days = t_age*365  #converting 90 years into days
t_age_weeks = t_age*52  #converting 90 years into weeks
t_age_months = t_age*12 #converting 90 years into months

c_age_days = int(age)*365 #converting current age into days
c_age_weeks = int(age)*52 #converting current age into weeks
c_age_months = int(age)*12 #converting current age into months

days_left = t_age_days - c_age_days  #calculating days left
weeks_left = t_age_weeks - c_age_weeks #calculating weeks left
months_left = t_age_months - c_age_months #calculating months left

#printing the output using fstring
print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")