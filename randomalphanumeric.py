import random
import string

def generate_alphanumeric_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Example usage:
alphanumeric_string = generate_alphanumeric_string(6) # generates a 10 character long string
print(alphanumeric_string)
