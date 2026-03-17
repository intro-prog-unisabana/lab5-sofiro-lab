from utils import flip, count_letters

def main():
    message = input("Please type your message\n")

    reversed_message = flip(message)
    a_count = count_letters(message, "a")

    encoded_message = reversed_message + str(a_count)

    print("Your encoded message is: " + encoded_message)

main()