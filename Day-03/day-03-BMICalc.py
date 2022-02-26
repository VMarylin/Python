height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = round(weight / height**2)

#Under 18.5 they are underweight
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
#Over 18.5 but below 25 they have a normal weight
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
#Over 25 but below 30 they are slightly overweight
elif BMI <= 30:
    print(f"Your BMI is {BMI} you are slightly overweight")
#Over 30 but below 35 they are obese
elif BMI <=35:
    print(f"Your BMI is {BMI} you are obese")
#Above 35 they are clinically obese.
else:
    print(f"Your BMI is {BMI} you are clinically obese")
