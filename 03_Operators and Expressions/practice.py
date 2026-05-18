# This program takes two numbers from user and finds out the remainder after division

#----------------------------------------------------------

while True:
    first_number = float(input("Enter first number:"))
    second_number = float(input("Enter second number:"))
    if second_number != 0: 
        remainder = first_number % second_number
        print(f"Remainder of {first_number} divided by {second_number} is {remainder}")
        break
    else:
        print("Error! Can't divide by zero")
        continue
   
   #-----------------------------------------------------

#This program is built to convert temperature from Fahrenheit to Celsius
T_C = float(input("Enter the temperature in Celsius:"))
T_F = (T_C * 9/5) +32
print(f"{T_F} degree Fahrenheit\nSo, the temperature {T_C} degree Celsius is equal to {T_F} degree Fahrenheit")

#---------------------------------------------------------




    