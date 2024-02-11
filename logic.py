# This is a program is meant to demonstrate a logical error.
# Input from the user a list of numbers to play at the UK Lottery.
 
print ("Welcome to the UK Lottery! Today is your luck day! ")
print ("\n")

numbers_list = []

for i in range(6):
       
    try:
        number = int(input(f"Please, enter the number {i+1} of the game, to Try one's luck! "))
        if number < 0: # Logical error: the code do not check the value appropriately.
            raise ValueError("Please enter just numbers between 1 to 50.")
        numbers_list.append(number)
        numbers_list_sorted = sorted(numbers_list)

    except:
        print("Please enter just integers and positive numbers")

print ("\n")
print(f"Your game is {numbers_list_sorted}! Good luck!")

