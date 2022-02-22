#user to input the number and saved in the variable called "number"
number = int(input("Which number do you want to check? "))

#the modulo funtion is written with a percentage sign(%) .It gives you the remainder after a division.
# example 6%2 =0 and 7%2 = 1

if number%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
