
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



#converting the height and weight from str to float
new_height = float(height)
new_weight = float(weight)
 #using the ** as exponent operator and PEMDAS
BMI = new_weight/(new_height**2) 
#converting the floating type to integer
print(int(BMI))

