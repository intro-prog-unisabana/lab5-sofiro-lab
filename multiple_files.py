from utils import flip, count_letters

mensaje = input("Please type your message\n")

# invertir el mensaje
mensaje_invertido = flip(mensaje)

# contar las letras 'a'
cantidad_a = count_letters(mensaje, 'a')

# crear mensaje codificado
mensaje_codificado = mensaje_invertido + str(cantidad_a)

print(f"Your encoded message is: {mensaje_codificado}")