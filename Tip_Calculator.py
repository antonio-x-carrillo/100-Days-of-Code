# User instructions & inputs
print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

# Calculation
bill_plus_tip = bill * (1 + tip/100)
bill_split = bill_plus_tip / people
payment = round( bill_split, 2)

# Output
print(f"Each person should pay: ${payment}")