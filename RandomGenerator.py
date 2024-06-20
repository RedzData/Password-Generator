import random
import string

def random_password_generator(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all required character types.")

    # At least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random choices from all character types
    remaining_length = length - 4
    if remaining_length > 0:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(all_characters) for _ in range(remaining_length)]

    # Shuffle the list to ensure random order
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Example usage
print(random_password_generator(12))