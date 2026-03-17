from utils import *

def main():
    message = input("Please type your message\n")

    flipped = flip(message)
    count = count_letters(message, "a")

    encoded = flipped + str(count)

    print("Your encoded message is: " + encoded)