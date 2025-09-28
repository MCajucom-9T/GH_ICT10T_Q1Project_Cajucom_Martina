# data types in Python
from pyscript import display


restaurant_name = 'Midnight Grill Diner'  # string (text)
owner_name = 'Martina Nina Louise C. Cajucom'  # string (text)
year_established = 2025  # integer (whole number)
popular_item_price = 219.99  # float (number with decimals)
has_delivery = True  # boolean (True/False value)
product_names = ['Cheese Burger', 'Fried Chicken', 'Fries']  # list (ordered collection of strings)
business_hours = {'opening': '5pm', 'closing': '1am'}   # dictionary (key-value pairs, both values are strings)
menu_prices = {'Chicken': '280.00', 'Fries': '94.99', 'MilkShake': '148.90', 'IcedTea': '100.75', 'Salad': '120', 'Sandwich': '240'}  # dictionary (key-value pairs, keys are strings, values are strings too)
common_allergens = ['glutten', 'eggs', 'milk', 'nuts']  # list (ordered collection of strings)
tax_rate = 0.09  # float (number with decimals)

display(f'{restaurant_name}', target='name')
display(f'{owner_name}', target='owner')
display(f'{year_established}', target='year')
display(f'{product_names[0]}', target='item1')
display(f'{product_names[1]}', target='item2')
display(f'{product_names[2]}', target='item3')
display(f'₱{popular_item_price}', target='price1')
display(f'₱{menu_prices['Chicken']}', target='price2')
display(f'₱{menu_prices['Fries']}', target='price3')
display(f'₱{menu_prices['MilkShake']}', target='price4')
display(f'₱{menu_prices['IcedTea']}', target='price5')
display(f'Open from {business_hours['opening']}-{business_hours['closing']}', target='hours')
#calling the ids and filling it up with data