import random
import string

def password_generator(min_letters,number=True,spl_char=True):
    letters=string.ascii_letters
    digits=string.digits
    spl=string.punctuation

    characters=letters
    if number:
        characters+=digits
    if spl_char:
        characters+=spl

    pwd = ''
    meet_requ=False
    has_number=False
    has_spl_char=False

    while not meet_requ or len(pwd) < min_letters:
        new_char=random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number= True
        elif new_char in spl:
            has_spl_char= True

        meet_requ = True
        if number:
            meet_requ = has_number
        if spl_char:
            meet_requ=meet_requ and has_spl_char
    return pwd

min_letters=int(input('Type the length of the password: '))
has_number=input('Do you want number in your password: (Y/N) ').lower() == 'y'
has_spl_char=input('Do you want Special character in your password: (Y/N) ').lower() == 'y'

pwd =password_generator(min_letters,has_number,has_spl_char)

print(pwd)