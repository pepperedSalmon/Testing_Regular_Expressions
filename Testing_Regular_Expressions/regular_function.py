import re

def regular_function(text):
    phone_num_regex=re.compile(r"\d{3}-\d{3}-\d{4}")
    numbers=phone_num_regex.findall(text)
    for number in numbers:
        print('Phone number found: ' + number)
