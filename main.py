import tkinter as tk
from tkinter import messagebox

# Function to save the diary entry to a file
def save_entry():
    entry_text = entry.get("1.0", "end-1c")
    if entry_text.strip():
        with open("diary.txt", "a") as diary_file:
            diary_file.write(entry_text + "\n")
        messagebox.showinfo("Success", "Diary entry saved successfully!")
        entry.delete("1.0", "end")

# Function to view previous diary entries
def view_entries():
    try:
        with open("diary.txt", "r") as diary_file:
            entries = diary_file.readlines()
            if entries:
                view_window = tk.Toplevel(root)
                view_window.title("Diary Entries")

                scrollbar = tk.Scrollbar(view_window)
                scrollbar.pack(side="right", fill="y")

                text_box = tk.Text(view_window, wrap="word", yscrollcommand=scrollbar.set)
                text_box.pack()

                scrollbar.config(command=text_box.yview)

                for entry in entries:
                    text_box.insert("end", entry)

                text_box.config(state="disabled")
            else:
                messagebox.showinfo("No Entries", "No diary entries found.")
    except FileNotFoundError:
        messagebox.showinfo("No Entries", "No diary entries found.")

# Create the main application window
root = tk.Tk()
root.title("Personal Diary App")

# Create a text box for entering diary entries
entry = tk.Text(root, wrap="word", width=40, height=10)
entry.pack(pady=10)

# Create buttons to save and view diary entries
save_button = tk.Button(root, text="Save Entry", command=save_entry)
view_button = tk.Button(root, text="View Entries", command=view_entries)
save_button.pack()
view_button.pack()

# Run the Tkinter main loop
root.mainloop()
