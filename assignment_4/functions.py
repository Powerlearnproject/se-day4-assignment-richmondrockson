# A simple function that adds two numbers from a users input
def add_two_numbers():
    #Get user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    #adds the two numbers 
    result = num1 + num2

    #returns result
    return result

sum_result = add_two_numbers()
print(f"The sum is: {sum_result}")
