import tkinter as tk
import random
import string
import pyperclip

# Define the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x270")
root.resizable(False, False)

# Define the function to generate the password
def generate_password():
    # Choose a random length between 8 and 16 characters
    length = length_slider.get()
    
    # Define the allowed characters for the password
    letters = string.ascii_letters
    digits = string.digits
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    allowed_chars = letters + digits
    if special_chars_var.get():
        allowed_chars += punctuation
    
    # Generate the random password
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    
    # Show the password in the GUI label
    password_label.config(text=password)
    
    # Copy password to clipboard and show message
    pyperclip.copy(password)
    copied_label.config(text="Password copied to clipboard!", fg="green")

# Define the label for the password
password_label = tk.Label(root, text="", font=("Arial", 16))
password_label.pack(pady=10)

# Define the slider for the password length
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT)
length_slider = tk.Scale(length_frame, from_=8, to=16, orient=tk.HORIZONTAL, length=200)
length_slider.set(12)
length_slider.pack(side=tk.LEFT)

# Define the checkbox for special characters
special_chars_var = tk.BooleanVar()
special_chars_var.set(True)
special_chars_check = tk.Checkbutton(root, text="Include special characters", var=special_chars_var)
special_chars_check.pack(pady=5)

# Define the button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#4286f5')
generate_button.pack(pady=10)

# Define the label for the copy message
copied_label = tk.Label(root, text="")
copied_label.pack(pady=5)

# Add attribution label
attribution_label = tk.Label(root, text="@python.tools", font=("Arial", 8))
attribution_label.place(relx=1.0, rely=1.0, anchor="se")

# Start the main window
root.mainloop()
