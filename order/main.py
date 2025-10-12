# data types in Python
from pyscript import display, document


def computing_order(e):
    document.getElementById('for').innerHTML = "Order for:" #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('where').innerHTML = "Address:" #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('no_').innerHTML = "Contact Number:" #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('total').innerHTML = "Total:" #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('incomplete').innerHTML = " "

    name = document.getElementById('name').value # collecting value from an input field
    address = document.getElementById('address').value 
    number = document.getElementById('number').value
    total = 0

    if document.getElementById('burger').checked: # .checked checks whether the checkbox is checked, runs code when it is checked
        total = total + float(document.getElementById('burger').value) #if the checkbox is chevcked it will add the value of the food to the current value of total

    if document.getElementById('chicken').checked:
        total = total + float(document.getElementById('chicken').value)

    if document.getElementById('fries').checked:
        total = total + float(document.getElementById('fries').value)

    if document.getElementById('shake').checked:
        total = total + float(document.getElementById('shake').value)

    if document.getElementById('icedtea').checked:
        total = total + float(document.getElementById('icedtea').value)

    if total == 0 or not name or not address or not number:
        display(f'Please complete your order.', target="incomplete") #forces users to input information, if total == 0 that means user has not clicked any checkbox
    
    #displays customer input
    display(f'{name}', target='for')
    display(f'{address}', target='where')
    display(f'{number}', target='no_')
    display(f'₱{total}', target='total')