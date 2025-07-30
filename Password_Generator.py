import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Generate password given user requirements
# password = ""
password = []
for l in range(0,nr_letters):
    random_letter = random.randint(0,len(letters) - 1) # Can be replaced with: random.choice(letters)
    password.append(letters[random_letter])
    # password = password + letters[random_letter]

for n in range(0,nr_numbers):
    random_number = random.randint(0,len(numbers) - 1) # Can be replaced with: random.choice(numbers)
    password.append(numbers[random_number])
    # password = password + numbers[random_number]

for s in range(0,nr_symbols):
    random_symbol = random.randint(0,len(symbols) -1)  # Can be replaced with: random.choice(symbols)
    password.append(symbols[random_symbol])
    # password = password + symbols[random_symbol]

# Scramble the password. NOTE: Previous code modified to work with shuffle function
random.shuffle(password)
final_password = ""
for characters in password:
    final_password = final_password + characters

# Output password
print(final_password)
