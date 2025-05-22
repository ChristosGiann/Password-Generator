import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(user_password):
    password_strength = 0
    if any(w.isupper() for w in user_password):
        password_strength += 1
    if any(c.isdigit() for c in user_password):
        password_strength += 1
    if len(user_password) >= 12:
        password_strength += 1

    
    if password_strength == 3:
        print("Ο κωδικός σου είναι ισχυρός")
    elif password_strength == 2:
        print("Ο κωδικός σου είναι μέτριας ισχύς")
    elif password_strength == 1:
        print("Ο κωδικός σου είναι αδύναμος")

user_length_choice = int(input("Πόσους χαρακτήρες θέλει να έχει ο κωδικός σου;"))
user_password = generate_password(user_length_choice)
print("Ο τυχαίος κωδικός σου είναι:", user_password)
check_strength(user_password)

