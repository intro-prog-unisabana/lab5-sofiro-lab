from utils import *

message = input("Please type your message\n")

flipped = flip(message)
a_count = count_letters(message, "a")

encoded_message = flipped + str(a_count)

print(f"Your encoded message is: {encoded_message}")