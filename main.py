import tkinter as tk
from PyDictionary import PyDictionary

def print_meanings():
    word = entry.get()
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    meanings_text.delete('1.0', tk.END)  # Clear previous text
    if meanings:
        for part_of_speech, meaning_list in meanings.items():
            meanings_text.insert(tk.END, part_of_speech + ":\n")
            for meaning in meaning_list:
                meanings_text.insert(tk.END, "- " + meaning + "\n")
    else:
        meanings_text.insert(tk.END, "Meanings not found")

# Create the Tkinter window
root = tk.Tk()
root.title("Print Meanings")
root.resizable(height=False, width=False)
root.attributes('-alpha', 0.7)  # Set window opacity
root.configure(bg='black')  # Set window background color

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window width, height, and position to center
window_width = 600
window_height = 400
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Entry widget
entry = tk.Entry(root, bg='black', fg='white', width=50)  # Set text color to white, background color to black, and width to 50 characters
entry.pack(pady=10)

# Button to print meanings
print_button = tk.Button(root, text="Print Meanings", command=print_meanings, bg='black', fg='white')  # Set button colors
print_button.pack()

# Text widget to display meanings
meanings_text = tk.Text(root, height=15, width=100, bg='black', fg='white')  # Set text color to white, background color to black, and width to 100 characters
meanings_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
