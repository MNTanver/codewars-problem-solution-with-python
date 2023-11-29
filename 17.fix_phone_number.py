# import re

# def is_it_a_num(number:str)->str:
     
#     regex = re.compile('[!@#$%^&*()_+|{}<>?/]')

#     if len(number) == 11 and number[0] == '0' and number.isdigit() and regex.search(number) == None:
#         print ("Valid phone number")
#     else:
#         print ("Not a phone number")

# number = "01750940&141"
# is_it_a_num(number)

def is_it_a_num(number: str) -> str:
    # Remove all non-digit characters from the input string
    number = ''.join(filter(str.isdigit, number))
     
    if len(number) == 11 and number[0] == '0':
        return number
    else:
        return "Not a phone number"

    