def input_response(generate_value, user_input):
    """Compara el número secreto con la respuesta del usuario."""

    if user_input < generate_value:
        return "Too low! Try a higher number.", False

    elif user_input > generate_value:
        return "Too high! Try a lower number.", False

    else:
        return "Correct! You guessed the number!", True