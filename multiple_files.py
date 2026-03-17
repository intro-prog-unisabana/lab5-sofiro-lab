from utils import flip, count_letters

message = input("Please type your message\n")

flipped_message = flip(message)
a_count = count_letters(message, "a")

encoded_message = flipped_message + str(a_count)

print("Your encoded message is:", encoded_message)