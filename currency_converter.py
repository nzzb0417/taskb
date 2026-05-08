    #Portfolio Task - Week 4
    
    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.
    
    Name:
    Abdimalik Hussein
""

def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    
    if from_currency.upper() == "GBP":
        new_amount = conversion_rate['GBP'][to_currency] * amount
    elif from_currency.upper() == "CNY":
        new_amount = conversion_rate['CNY'][to_currency] * amount
    elif from_currency.upper() == "PHP":
        new_amount = conversion_rate['PHP'][to_currency] * amount
    elif from_currency.upper() == "INR":
        new_amount = conversion_rate['INR'][to_currency] * amount
    else:
        print("Error: Please enter one of the currencies listed above")
        
    if amount < 0:
        return 0.0
        
    return round(new_amount, 2)


# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function,
# or code to get user input.
