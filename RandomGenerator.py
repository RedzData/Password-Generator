import random
import string

def random_password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Example usage
print(random_password_generator(12))