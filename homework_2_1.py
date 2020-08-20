# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = input('enter first number: ')
second_number = input('enter second number: ')
if first_number > second_number:
 result_1 = first_number
 print('first number'+ result_1+ 'is greater')
#elif first_number<second_number:
else:
 result_1=second_number
 print('second number' + result_1)


# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = input('enter a number')
if int(number_1) >=20:
 result_2 = "Too high"
 print(result_2)
else: result_2="Thank you"
print(result_2)



# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = 'Eyerusalem'
last_name = 'Gebregiorgis'
if len(first_name) < 5:
    result_3 = first_name+last_name
    print(result_3.upper())
else: 
    result_3=first_name
    print(result_3.lower())

# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = int(input("enter a number between 10 and 20"))
if 10 <= number_2 <= 20:
    result_4 = "Thank you"
    print(result_4)
else:
    result_4="incorrect answer"
    print(result_4)


# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = int(input('enter your age'))
if age >= 18:
    result_5 = "you can vote"
    print(result_5)
elif age == 17:
    result_5 = "you can learn to drive"
    print(result_5)
elif age == 16:
    result_5 = "you can buy a lottery ticket"
    print(result_5)
else:
    result_5 = "You can go Trick-or-Treating"
    print(result_5)



# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = int(input("enter a number between 1 and 12"))
if month == 1:
    result_month = "January"
    print(result_month.lower())
elif month == 2:
    result_month = "February"
    print(result_month.lower())
elif month == 3:
    result_month = "March"
    print(result_month.lower())
elif month == 4:
    result_month = "April"
    print(result_month.lower())
elif month == 5:
    result_month = "May"
    print(result_month.lower())
elif month == 6:
    result_month = "June"
    print(result_month.lower())
elif month == 7:
    result_month = "July"
    print(result_month.lower())
elif month == 8:
    result_month = "August"
    print(result_month.lower())
elif month == 9:
    result_month = "September"
    print(result_month.lower())
elif month == 10:
    result_month = "October"
    print(result_month.lower())
elif month == 11:
    result_month = "November"
    print(result_month.lower())
else:
    result_month = "December"
    print(result_month)