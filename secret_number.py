import random

def seed_secret_numbers(seed):
    """Inicializa el generador de números aleatorios."""
    random.seed(seed)


def generate_secret_number(start=1, end=100):
    """Retorna un número secreto entre start y end."""
    return random.randint(start, end)