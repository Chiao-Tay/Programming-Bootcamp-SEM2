# Task 1
# This program takes a list of digits and builds the number they represent.
# Instead of converting the digits to strings or using built-in functions like int(), we simulate the
# construction of the number using only mathematical operations.
# The idea is to "build" the number one digit at a time from left to right.
# Each time we add a digit, we multiply the existing number by 10 to shift digits to the left,
# then add the new digit into the ones place.

def my_func(digit_list):
    """
    Convert a list of digits to an integer.
    """
    result = 0 # This variable will store the final number

    # Go through each digit in the list
    for digit in digit_list:
        # Multiply current result by 10 to shift digits to the left, then add the current digit into the ones place
        result = result * 10 + digit
    
    return result

# Test cases
test_cases = [
    [8, 3, 5, 1],
    [1, 2, 3],
    [9],
    [0, 4, 2],
    [1, 0, 0, 0],
    [7, 8, 9, 0, 1, 2]
]


for digit_list in test_cases:
    result = my_func(digit_list)
    print(f"Input: {digit_list} -> Output: {result}")