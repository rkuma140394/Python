import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("360x520")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Segoe UI", 24),
    bd=0,
    relief=tk.FLAT,
    bg="#252526",
    fg="white",
    justify="right"
)
display.pack(fill=tk.BOTH, padx=10, pady=20, ipady=15)

# Button click function
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        action = (
            lambda x=btn: calculate() if x == "=" else click(x)
        )
        tk.Button(
            row_frame,
            text=btn,
            font=("Segoe UI", 16),
            bg="#3c3c3c",
            fg="white",
            activebackground="#007acc",
            activeforeground="white",
            bd=0,
            command=action,
            height=2,
            width=6
        ).pack(side=tk.LEFT, expand=True, fill="both", padx=5, pady=5)

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Segoe UI", 16),
    bg="#d83b01",
    fg="white",
    bd=0,
    command=clear
).pack(fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
