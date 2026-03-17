from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

# pedir semilla
seed = int(input("Enter a seed number:\n"))

# inicializar generador
seed_secret_numbers(seed)

# generar número secreto
secret = generate_secret_number()

tries = 0
correct = False

# bucle del juego
while not correct:
    guess = int(input("What is your guess:\n"))
    tries += 1

    message, correct = input_response(secret, guess)
    print(message)

# resultado final
print(f"It took you {tries} tries!")