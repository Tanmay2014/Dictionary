import tkinter as tk
from nltk.corpus import wordnet


def print_meanings():
    word = entry.get()
    synsets = wordnet.synsets(word)
    meanings_text.delete('1.0', tk.END)  # Clear previous text
    if synsets:
        for synset in synsets:
            meanings_text.insert(tk.END, synset.definition() + "\n")
    else:
        meanings_text.insert(tk.END, f"Meanings not found for '{word}'. Please check the spelling or try another word.")


def close_program():
    root.destroy()


# Create the Tkinter window
root = tk.Tk()
root.title("Print Meanings")
root.resizable(height=False, width=False)
root.attributes('-alpha', 0.8)  # Set window opacity
root.configure(bg='black')  # Set window background color

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window width, height, and position to center
window_width = 600
window_height = 300
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 3
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Close button
close_button = tk.Button(root, text="X", command=close_program, bg='black', fg='white', relief=tk.FLAT)
close_button.place(x=5, y=5)  # Position the button in the top left corner

# Entry widget
entry = tk.Entry(root, bg='black', fg='white', width=50)  # Set text color to white, background color to black, and width to 50 characters
entry.pack(pady=10)

# Button to print meanings
print_button = tk.Button(root, text="Explain", command=print_meanings, bg='black', fg='white')  # Set button colors
print_button.pack()

# Text widget to display meanings
meanings_text = tk.Text(root, height=15, width=100, bg='black', fg='white')  # Set text color to white, background color to black, and width to 100 characters
meanings_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
