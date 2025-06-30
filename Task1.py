def my_func(digit_list):
    result = 0
    
    for digit in digit_list:
        result = result * 10 + digit
    
    return result

digit_list = [8,3,5,1]
print(my_func(digit_list))