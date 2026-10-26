from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'Madagascar':'Antananarivo', 
    'Taiwan':'Taipei',
    'Egypt':'Cairo',
    'Philippines':'Manila',
    'USA':'Washington D.C.',
    'Denmark':'Copenhagen',
    'Chile':'Santiago'
    }

    countries_checker = user_input in countries
    display_message = (f'NOOO {user_input} in THIS list', f'{user_input} is in the list YAYYY!')
    display(display_message[countries_checker], target='output')