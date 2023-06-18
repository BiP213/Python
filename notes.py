import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

MAX_CHARACTERS = 1000  # Maximum character limit


def save_note():
    note_content = note_text.get("1.0", tk.END).strip()
    if not note_content:
        messagebox.showwarning("Empty Note", "Please write something before saving.")
        return

    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if not filename:
        return

    try:
        with open(filename, "w") as file:
            file.write(note_content)
        messagebox.showinfo("Note Saved", "Note saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save note: {str(e)}")


def clear_note():
    note_text.delete("1.0", tk.END)
    update_character_count()


def update_character_count(event=None):
    content = note_text.get("1.0", tk.END)
    current_characters = len(content.replace("\n", ""))

    char_count_var.set(f"Words: {current_characters}/{MAX_CHARACTERS}")

    if current_characters > MAX_CHARACTERS:
        char_count_label.config(fg="red")
    else:
        char_count_label.config(fg="black")


def shortcuts(event):
    if event.keysym == "Delete":
        clear_note()
    elif event.keysym == "s" and (event.state & 0x4):  # Check for "Ctrl + S"
        save_note()
    elif event.keysym == "o" and (event.state & 0x4):  # Check for "Ctrl + O"
        saved_notes()


def saved_notes():
    filename = filedialog.askopenfilename(defaultextension=".txt")
    if not filename:
        return

    try:
        with open(filename, "r") as file:
            note_content = file.read()
            note_text.delete("1.0", tk.END)
            note_text.insert("1.0", note_content)
            update_character_count()  # Update character count after opening note
            messagebox.showinfo("Note Loaded", "Note loaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load note: {str(e)}")


def change_font_size(event=None):
    selected_font_size = font_size_combo.get()
    note_text.configure(font=("TkDefaultFont", selected_font_size))


def on_closing():
    # Custom exit message
    exit_message = "See ya! \N{HEAVY BLACK HEART}"
    messagebox.showinfo("Exiting", exit_message)
    window.destroy()


def show_welcome_message():
    # Show a welcoming message with available shortcuts
    welcome_message = "Welcome to the Note Taker!\n\n"
    welcome_message += "Available Shortcuts:\n"
    welcome_message += "Ctrl + S: Save Note\n"
    welcome_message += "Ctrl + O: Open Note\n"
    welcome_message += "Delete: Clear Note\n"
    messagebox.showinfo("Welcome", welcome_message)
    note_text.focus_set()  # Focus the text window


# Create the main window
window = tk.Tk()
window.title("Note Taker")

# Create a text area widget with a border
note_text = tk.Text(window, highlightthickness=2, highlightbackground="black")
note_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
note_text.bind("<KeyRelease>", update_character_count)  # Bind key release event

# Configure grid to resize the text window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Bind key press events for shortcuts
note_text.bind("<KeyPress-Delete>", shortcuts)
window.bind("<Control-s>", shortcuts)
window.bind("<Control-o>", shortcuts)

# Create a label to display character count
char_count_var = tk.StringVar()
char_count_var.set(f"Words: 0/{MAX_CHARACTERS}")  # Initialize character count
char_count_label = tk.Label(window, textvariable=char_count_var)
char_count_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create a frame to hold the bottom buttons
button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Create a save button
save_button = tk.Button(button_frame, text="Save", command=save_note)
save_button.pack(side="left", padx=5)

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_note)
clear_button.pack(side="left", padx=5)

# Create a saved notes button
saved_notes_button = tk.Button(button_frame, text="Open Note", command=saved_notes)
saved_notes_button.pack(side="left", padx=5)

# Configure grid to resize the button frame
button_frame.grid_columnconfigure(0, weight=1)

# Create a frame to hold the font size selector
font_frame = tk.Frame(window)
font_frame.grid(row=1, column=0, pady=5)

# Create a label for the font size selector
font_label = tk.Label(font_frame, text="Font Size:")
font_label.pack(side="left")

# Create a font size selector using Combobox
font_size_values = ["10", "12", "14", "16", "18"]
font_size_combo = ttk.Combobox(font_frame, values=font_size_values, width=3)  # Set width to 3
font_size_combo.pack(side="left")
font_size_combo.set("12")  # Set default font size
font_size_combo.bind("<<ComboboxSelected>>", change_font_size)  # Bind event to font size selector

# Create a button to apply font size change
font_size_button = tk.Button(font_frame, text="Apply", command=change_font_size)
font_size_button.pack(side="left")

# Bind the custom closing function to the window's close button
window.protocol("WM_DELETE_WINDOW", on_closing)


# Start the main event loop
window.after(100, show_welcome_message)
window.mainloop()
