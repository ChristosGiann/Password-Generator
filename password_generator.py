import random
import string
while True:
    def generate_password(length, characters):
        password = ''.join(random.choice(characters) for _ in range(length))
        return password


    def check_strength(user_password):
        password_strength = 0
        if any(l.isupper() for l in user_password):
            password_strength += 1
        if any(l.isdigit() for l in user_password):
            password_strength += 1
        if any(l in string.punctuation for l in user_password):
            password_strength += 1
        if len(user_password) >= 12:
            password_strength += 1

        
        if password_strength >= 3:
            print("Ο κωδικός σου είναι ισχυρός")
        elif password_strength == 2:
            print("Ο κωδικός σου είναι μέτριας ισχύς")
        elif password_strength == 1:
            print("Ο κωδικός σου είναι αδύναμος")




    while True:
        try:
            user_length_choice = int(input("Πόσους χαρακτήρες θέλεις; "))

            if user_length_choice < 4:
                print("Ο κωδικός πρέπει να έχει τουλάχιστον 4 χαρακτήρες.")
            elif user_length_choice > 25:
                print("Ο κωδικός δεν μπορεί να έχει πάνω από 25 χαρακτήρες.")
            else:
                break 

        except ValueError:
            print("Παρακαλώ γράψε έναν έγκυρο αριθμό.")




    def ask_include_symbols():
        while True:
            answer = input("Θέλεις ο κωδικός να περιέχει σύμβολα (π.χ. !@#)? (ναι/όχι): ").strip().lower()
            if answer == "ναι":
                return True
            elif answer == "όχι":
                return False
            else:
                print("Παρακαλώ απάντησε με 'ναι' ή 'όχι'.")



    include_symbols = ask_include_symbols()

    if include_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits


    user_password = generate_password(user_length_choice, characters)
    print("Ο τυχαίος κωδικός σου είναι:", user_password)
    check_strength(user_password)

    repeat_generation = input("Θέλεις να δημιουργήσεις άλλο κωδικό; (ναι/όχι): ").strip().lower()
    if repeat_generation != "ναι":
        print("Ευχαριστούμε που χρησιμοποιήσατε το password generator!")
        break
