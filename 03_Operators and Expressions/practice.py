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
   

    