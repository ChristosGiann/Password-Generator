import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def check_strength(password):
    password_strength = 0
    if any(l.isupper() for l in password):
        password_strength += 1
    if any(l.isdigit() for l in password):
        password_strength += 1
    if any(l in string.punctuation for l in password):
        password_strength += 1
    if len(password) >= 12:
        password_strength += 1
    
    if password_strength >= 3:
        label_strength.config(text="Ο κωδικός σου είναι ισχυρός", fg="green")
    elif password_strength == 2:
        label_strength.config(text="Ο κωδικός σου είναι μέτριας ισχύς", fg="yellow")
    elif password_strength == 1:
        label_strength.config(text="Ο κωδικός σου είναι αδύναμος", fg="red")

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 4 or length > 25:
            messagebox.showerror("Σφάλμα", "Ο κωδικός πρέπει να έχει τουλάχιστον 4 και το πολύ 25 χαρακτήρες.")
            return
    except ValueError:
        messagebox.showerror("Σφάλμα", "Εισάγετε έναν έγκυρο αριθμό για το μήκος.")
        return
    
    chars = string.digits

    if var_only_lower.get():
        chars += string.ascii_lowercase
    else:
            chars += string.ascii_letters
    
    if var_symbols.get():
        chars += string.punctuation
    
    pwd = generate_password(length, chars)
    entry_password.config(state='normal')
    entry_password.delete(0, tk.END)
    entry_password.insert(0, pwd)
    entry_password.config(state='readonly')
    
    check_strength(pwd) 

def copy_to_clipboard():
    root.clipboard_clear() 
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Αντιγραφή", "Ο κωδικός αντιγράφηκε στο πρόχειρο!")




root = tk.Tk()
root.title("Password Generator")
root.geometry("700x700") 


frame = tk.Frame(root)
frame.pack(expand=True) 

tk.Label(frame, text="Μήκος κωδικού (4-25):", font=("Arial", 30)).pack(pady=5)
entry_length = tk.Entry(frame, font=("Arial", 30), justify='center')
entry_length.pack(pady=5, padx=20)
entry_length.insert(0, "12")

var_symbols = tk.BooleanVar()
chk_symbols = tk.Checkbutton(frame, text="Να περιέχει σύμβολα;", variable=var_symbols, font=("Arial", 30))
chk_symbols.pack(pady=5, padx=20)

var_only_lower = tk.BooleanVar()
chk_only_lower = tk.Checkbutton(frame, text="Μόνο μικρά γράμματα;", variable=var_only_lower, font=("Arial", 30))
chk_only_lower.pack(pady=5, padx=20)

btn_generate = tk.Button(frame, text="Δημιουργία κωδικού", command=on_generate, font=("Arial", 30))
btn_generate.pack(pady=10, padx=20)

entry_password = tk.Entry(frame, font=("Arial", 30), fg="blue", justify='center')
entry_password.pack(pady=5, padx=20)
entry_password.config(state='readonly')

label_strength = tk.Label(frame, text="", font=("Arial", 30, "bold"))
label_strength.pack(pady=5, padx=20)

btn_copy = tk.Button(frame, text="Αντιγραφή κωδικού", command=copy_to_clipboard, font=("Arial", 30))
btn_copy.pack(pady=10, padx=20)


root.update_idletasks()  
width = root.winfo_width()
height = root.winfo_height()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
