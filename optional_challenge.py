# This is a program is meant to demonstrate two compilations errors, a logical and a runtime errors.
# Input from the user informations to send a News Years Eve Card message.

print("Welcome to the New Years Eve Card Message!" # Compilation error: missing parentheses.
print("\n")

    sender_name = input("Please, enter your name: ") # Compilation error: unexpected indentation.
sender_address = input("Please, enter your address: ")
recipient_name = input("Please, enter the name of the recipient: ")
recipient_address = input("Please, enter the address of the recipient: ")
upcoming_year = input("Please, enter the upcoming year: ")
card_layout = input("Please, choose between 1 or 2 card layout: ")

if card_layout == "1": 
    print("\nFrom: {sender_name}") # Logical error: it'll output the variable name instead it's value. 
    print(f"Return Address: {sender_address}")
    print(f"\nTo: {recipient_name}")
    print(f"{recipient_address}") 
    print(f"\nHappy New Year {recipient_name}! May {upcoming_year} bring you happiness, peace, and prosperity! ") 

elif card_layout == "2": 
    print(f"\nTo: {recipient_name} / {recipient_address}")
    print(f"\nHappy New Year {recipient_name}! May" + upcoming_year + "bring you happiness, peace, and prosperity! ") # Runtime error: we cannot concatenate a str with an int.
    print(f"\nFrom: {sender_name} / Return Address: {sender_address}")
    
else:
    raise ValueError("Please choose between 1 or 2 layouts!")