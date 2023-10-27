def convert_to_indian_currency(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Reverse the string to make it easier to add commas
    number_str = number_str[::-1]
    
    # Initialize variables to keep track of commas and the result
    result = ''
    comma_count = 0
    
    # Iterate through the reversed string
    for digit in number_str:
        # Add a comma after every 2 digits (except for the first)
        if comma_count == 2:
            result += ','
            comma_count = 0
        result += digit
        comma_count += 1
    
    # Reverse the result to get the correct order
    result = result[::-1]
    
    return result

# Test the function
number = 50467
indian_currency = convert_to_indian_currency(number)
print(indian_currency)
