from is_phone_number import is_phone_number
from is_phone_number import find_phone_numbers

from regular_function import regular_function

print('Is 415-555-4242 a phone number?')
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(is_phone_number('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
find_phone_numbers(message)

regular_function(message)