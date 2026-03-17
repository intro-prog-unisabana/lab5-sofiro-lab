from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

# pedir semilla
seed = int(input("Enter a seed number:\n"))

# inicializar random
seed_secret_numbers(seed)

# generar número secreto
secret_number = generate_secret_number()

tries = 0
correct = False

while not correct:
    guess = int(input("What is your guess:\n"))
    tries += 1

    message, correct = input_response(secret_number, guess)
    print(message)

print(f"It took you {tries} tries!")