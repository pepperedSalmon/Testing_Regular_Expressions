def is_phone_number(text):
    if len(text) != 12:
        return False
    elif not text[0:3].isdecimal():
        return False
    elif not text[4:7].isdecimal():
        return False
    elif not text[8:12].isdecimal():
        return False
    elif text[7] != "-" and text[3] != "-":
        return False 
    else:
        return True



def find_phone_numbers(text):
    for i in range(len(text)-12):
        chunk = text[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)
    print('Done')