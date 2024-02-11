# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax Error: missing parentheses.
print ("\n") # Syntax Errors: missing parentheses and wrong indentation.

age_str = "24 years old" # Syntax Error: wrong indentation and declaring the str removing the extra equal symbol.
age = int(age_str.split(" ")[0]) # Syntax Error: wrong indentation. # Runtime error: fixed age_str parsing.
print(f"I'm {age} years old.") # Syntax Error: wrong indentation. # Runtime error: we cannot concatenate a str with an int.

years_from_now = "3"
years_ahead = int(years_from_now) # Runtime error: we cannot concatenate a str with an int. # Syntax Errors: missing parentheses and wrong indentation.
total_years = age + years_ahead # Syntax Error: wrong indentation.

print(f"\nThe total number of years: {total_years}.") # Logical Error: using f-string to get the expected output.

total_months = (total_years * 12) + 6 # Logical Error: adding "+6" to get the expected output, according to the print statement.
print(f"\nIn 3 years and 6 months, I'll be {total_months} months old.") # Syntax Errors: missing parentheses. # Runtime error: using f-string, we cannot concatenate a str with an int.

#HINT, 330 months is the correct answer!

