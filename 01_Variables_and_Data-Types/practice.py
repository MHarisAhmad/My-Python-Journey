#Topic: Variables and Data-Types
#-----------------------------------
#Task 1: Personal info variables

name = "M.Haris Ahmad"                 #string
age = 17                               #integer
height_m = 1.72                        #float
is_student = True                      #boolean

#print all the information

print("Name: ",name)
print("Age: ",age)
print("Height(meters): ",height_m)
print("Is student: ",is_student)

#____________________________________________________________________
#____________________________________________________________________

# Task 2: Variable naming rules
#-----------------------------------

# 2number = 3            Error: Variable name cannot start with a number!
# twenty$ = 20           Error: No special character is allowed
# Allan Smith = True     Error: No whitespace allowed

# These are correct variable names:

Cat_name = "Billy"       # Obeys rules of variables
cat_age_months = 2       # Obeys rules of variables
cat_status = "Fine"      # Obeys rules of variables

#___________________________________________________________________
#___________________________________________________________________

# Task 3: String and Boolean manipulation
#----------------------------------------

user_str = input("Enter you string here:")                  # string input from the user

# applied some string methods
print(f"Your string {user_str} in upper-case is:",user_str.upper())                                     # Upper-case
print(f"Your string {user_str} in lower-case is:",user_str.lower())                                     # lower-case
print(f"Your string {user_str} in sentence case is:",user_str.capitalize())                             # sentence case  
print(f"Your string {user_str} in title case is:",user_str.title())                                     # title case
print(f"Checking your string {user_str} for alphabets:",user_str.isalpha())                             # checking for alphabets 
print(f"Checking your string {user_str} for numbers:",user_str.isdigit())                               # checking for digits
print(f"Removing extra-spaces from left and right in your string {user_str}:",user_str.strip())         # removing extra spaces
print(f"Replacing the first letter of your string {user_str} to A:",user_str.replace(user_str[0],"A"))  # replacing first character/digit
