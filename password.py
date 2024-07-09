python
import random
import string

def generate_password():
    password_length = 10
    num_uppercase = 2
    num_digits = 1
    num_special = 1
    
    password = ''.join(random.choices(string.ascii_uppercase, k=num_uppercase))
    password += ''.join(random.choices(string.digits, k=num_digits))
    password += ''.join(random.choices(string.punctuation, k=num_special))
    password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length - num_uppercase - num_digits - num_special))
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

print(generate_password())
