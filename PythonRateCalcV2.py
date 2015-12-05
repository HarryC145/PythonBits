# Do our import
import subprocess, sys

# This is a script that is going to work out the hourly rate of pay for an employee. The rate of pay is based
# on the employee number. The higer the employee number, the higher the rate of pay.

# Introduce the script

print("Welcome to the Hourly Rate Calculator for Example Company")

# Collect Employee information -  also declares some of our variables

EmployeeNumber = input("What is your employee number?")

EmployeeNumber = int(EmployeeNumber)

# Sanity check on the employee number - is it 7 charachters long? Is it purely numbers?

if len(str(EmployeeNumber)) == 4:

    # Now we work out the rate of pay - do this using an IF on the employee number. The higher the
    # number the more the rate
    # 3200 - 3300 = £16.66 per hour
    # 3301 - 3400 = £17.66 per hour
    # 3401 - 3500 = £18.66 per hour
    # 3501 - 3600 = £19.66 per hour
    # 3601 - 3610 = £20 per hour

    # Now we do the calculation on that -  or import from another script
    
    if EmployeeNumber  > 3200 < 3300:
        PayRate = 16.66

    if EmployeeNumber  > 3301 < 3400:
        PayRate = 17.66

    if EmployeeNumber  > 3401 < 3500:
        PayRate = 18.66

    if EmployeeNumber  > 3501 < 3600:
        PayRate = 19.66

    if EmployeeNumber  > 3601 < 3610:
        PayRate = 20

    print("Your rate of pay is £",PayRate,"." "Is that correct?")

    RateCorrect = input("Please enter Yes or No")

if RateCorrect == "Yes":
    print ("Thanks. Now we will move on to calculating your total hourly pay")

# This script is now going to calculate the rate of pay

# Import the time functions

from datetime import datetime

# Take the start time from the user

StartTime = input("Please enter your start time - in the format HH:MM so 09:00: ")
EndTime = input("Please enter your end time: ")

# Just declare the format of the time as a variable so I can use it later easier

Format = '%H:%M#'
# Now we do the time calculation

TimeDifference = datetime.strptime(EndTime, Format) - datetime.strptime(StartTime, Format)

print (TimeDifference)



