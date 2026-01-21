import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

# Main window
root = tk.Tk()
root.title("Spelling Checker")
root.geometry("850x500")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Spelling Checker",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=10)

# Main frame
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Input label
tk.Label(
    main_frame,
    text="Enter Text",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=0, sticky="w")

# Input text
input_text = tk.Text(
    main_frame,
    height=12,
    width=45,
    font=("Segoe UI", 12),
    bg="#252526",
    fg="white",
    insertbackground="white",
    bd=0
)
input_text.grid(row=1, column=0, padx=10, pady=5)

# Output label
tk.Label(
    main_frame,
    text="Corrected Text",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=2, sticky="w")

# Output text
output_text = tk.Text(
    main_frame,
    height=12,
    width=45,
    font=("Segoe UI", 12),
    bg="#252526",
    fg="white",
    insertbackground="white",
    bd=0
)
output_text.grid(row=1, column=2, padx=10, pady=5)

# Spell check function
def check_spelling():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to check")
        return

    try:
        blob = TextBlob(text)
        corrected = blob.correct()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(corrected))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Check Spelling",
    font=("Segoe UI", 14),
    bg="#007acc",
    fg="white",
    bd=0,
    padx=20,
    pady=8,
    command=check_spelling
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    font=("Segoe UI", 14),
    bg="#d83b01",
    fg="white",
    bd=0,
    padx=20,
    pady=8,
    command=lambda: [input_text.delete("1.0", tk.END),
                     output_text.delete("1.0", tk.END)]
).grid(row=0, column=1, padx=10)

root.mainloop()
