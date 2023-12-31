# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.If the function is passed a valid PIN string, return true, else return false.

#************************************

def validate_pin(pin):
    import re
    if len(pin) == 4 or len(pin) == 6: 
        if re.search('[^0-9]', pin) == None : #contains non-digit chars
            return True
    return False    

pin = "a23456"
validate_pin(pin)

# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()

# import re
# def validate_pin(pin):
#     #return true or false
#     return bool(re.fullmatch("\d{4}|\d{6}", pin))