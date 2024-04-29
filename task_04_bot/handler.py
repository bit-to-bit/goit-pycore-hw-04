'''Commands handler'''

import re
from faker import Faker
from utils import format_cmd, format_param, format_greeting

BORDER = "-"*62
DEMO_CONTACTS = 10
GREETING_BANNER = """
  ___          _     _              _     _           _   
 / _ \        (_)   | |            | |   | |         | |  
/ /_\ \___ ___ _ ___| |_ __ _ _ __ | |_  | |__   ___ | |_ 
|  _  / __/ __| / __| __/ _` | '_ \| __| | '_ \ / _ \| __|
| | | \__ \__ \ \__ \ || (_| | | | | |_  | |_) | (_) | |_ 
\_| |_/___/___/_|___/\__\__,_|_| |_|\__| |_.__/ \___/ \__|
"""
contacts = {}

def greeting() -> str:
    '''Print greeting message'''
    result  = f"""
{format_greeting(GREETING_BANNER)}
Welcome to the assistant bot!
{print_menu()}"""
    return result

def hello() -> str:
    '''Print hello message'''
    result  = f"How can I help you? \n{print_menu()}"
    return result

def print_menu()  -> str:
    '''Print bot menu'''
    result  = f"""
You can use commands:
{BORDER}
[0] {format_cmd('hello')} to show command list
[1] {format_cmd('add')} {format_param('[CONTACT_NAME] [+380XXXXXXXXX]')} to add a new contact
[2] {format_cmd('change')} {format_param('[CONTACT_NAME] [+380XXXXXXXXX]')} to update a contact
[3] {format_cmd('delete')} {format_param('[CONTACT_NAME]')} to delete contact
[4] {format_cmd('phone')} {format_param('[CONTACT_NAME]')} to find a phone by name
[5] {format_cmd('all')} to view a full contact list
[6] {format_cmd('demo')} to generate {DEMO_CONTACTS} contacts in the note book
[7] {format_cmd('exit')} or {format_cmd('close')} to app close
{BORDER}"""
    return result

def add_contact(args) -> str:
    '''Add new contact'''
    if  len(args)  < 2:
        result = "Not enough arguments. Try again!"
    elif len(args) > 2:
        result = "Too many arguments. Try again!"
    else:
        contact_name, phone = args
        if contact_name  in contacts:
            result = f"This contact already exists. Use command {format_cmd('change')} to update it!"
        else:
            contacts[contact_name]  = phone
            result = "Contact added."
    return result

def change_contact(args) -> str:
    '''Change contact'''
    if  len(args)  < 2:
        result = "Not enough arguments. Try again!"
    elif len(args) > 2:
        result = "Too many arguments. Try again!"
    else:
        contact_name, phone = args
        if contact_name not in contacts:
            result = f"This contact does not exists. Use command {format_cmd('add')} to add it!"
        else:
            contacts[contact_name]  = phone
            result = "Contact updated."
    return result

def delete_contact(args) -> str:
    '''Delete contact'''
    if  len(args) < 1:
        result = "Not enough arguments. Try again!"
    elif len(args) > 1:
        result = "Too many arguments. Try again!"
    else:
        contact_name = args[0]
        if contact_name not in contacts:
            result = "This contact not found."
        else:
            contacts.pop(contact_name)
            result = "The contact deleted."
    return result

def show_phone(args) -> str:
    '''Change contact'''
    if  len(args) < 1:
        result = "Not enough arguments. Try again!"
    elif len(args) > 1:
        result = "Too many arguments. Try again!"
    else:
        contact_name = args[0]
        if contact_name not in contacts:
            result = "This contact not found."
        else:
            result = contacts[contact_name]
    return  result

def show_all() -> str:
    '''Print all contacts'''
    result = ""
    if len(contacts) >  0:
        map_contacts = (max(map(len, col)) for col in zip(*contacts.items()))
        s = f"{{:<{next(map_contacts)}}} -> {' '.join(f'{{:>{ml}}}' for ml in map_contacts)}"
        for x in contacts.items():
            result += f"{s.format(*x)}\n"
    else:
        result = "The note book does not contain any contacts yet."
    return result

def demo() -> str:
    '''Generate demo contacts in note book'''
    fake = Faker(locale="uk_UA")
    pattern = r"[^\d\+]"
    replacement = ""
    for i in range(DEMO_CONTACTS):
        contact_name = str(fake.unique.name()).replace(" ","_")
        phone = re.sub(pattern, replacement, fake.unique.phone_number())
        contacts[contact_name] = phone
    result = f"{DEMO_CONTACTS} demo contacts generated and added to the note book."
    return  result

def app_exit() -> str:
    '''Print farewell message'''
    return "Good bye!"
