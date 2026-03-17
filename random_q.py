import random

# establecer semilla
random.seed(123)

# pedir valores al usuario
start = int(input("Enter the start value:\n"))
end = int(input("Enter the end value:\n"))

# generar número aleatorio
num = random.randint(start, end)

# imprimir resultado
print(f"Generated random number: {num}")