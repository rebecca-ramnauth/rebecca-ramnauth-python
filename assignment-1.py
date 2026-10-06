#Section 1: Variables and Types
name = "Finneas"
age = 28
height = 6.3
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print ("                           ")


#Section 2: User Input and Math
user_name = input("What is your name? ")
birth_year = int(input("What is your year of birth? "))
approx_age = 2026-birth_year
print(f"Hello,{user_name}! You are approximately {approx_age} years old!")
print ("                           ")

#Section 3: Type Conversion and f-strings
num_1 = float(input("Please enter a number: "))
num_2 = float(input("Please enter a second number: "))
result = num_1*num_2
print(f"The product of {num_1} and {num_2} is {result:.1f}")
print ("                           ")

#Section 4: Formatted Receipt
item = "Pen"
price = 0.99
quantity = 4

print ("**********************")
print ("        Receipt       ")
print ("                      ")
print (f"Item     :{item}     ")
print (f"Price    :${price}   ")
print (f"Quantity :{quantity} ")
print (f"Your total is ${price*quantity:.2f}")
print ("                      ")
print ("**********************")
print ("                           ")

#Section 5: Mini-Project - Profile Card
username = input("What is your name? ")
hometown = input("What is hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("What is a fun fact about yourself? ")
birthyear = int(input("What is your year of birth? "))

print ("                           ")
print ("===========================")
print (f" Profile: {username}      ")
print ("===========================")
print ("                           ")
print (f"Hometown :{hometown}      ")
print (f"Hobby    :{hobby}         ")
print (f"Fun Fact :{fun_fact}      ")
print (f"Age      :{2026-birthyear}")
print ("                           ")
print ("===========================")
