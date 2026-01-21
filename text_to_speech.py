import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3

engine = pyttsx3.init()

# Main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("800x450")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Text to Speech Converter",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=10)

# Main frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Text input
tk.Label(
    frame,
    text="Enter Text",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=0, sticky="w")

text_area = tk.Text(
    frame,
    height=10,
    width=60,
    font=("Segoe UI", 12),
    bg="#252526",
    fg="white",
    insertbackground="white",
    bd=0
)
text_area.grid(row=1, column=0, columnspan=3, pady=10)

# Voice selection
voices = engine.getProperty("voices")

tk.Label(
    frame,
    text="Voice",
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="white"
).grid(row=2, column=0, sticky="w")

voice_combo = ttk.Combobox(frame, state="readonly", width=25)
voice_combo["values"] = ["Male", "Female"]
voice_combo.set("Male")
voice_combo.grid(row=3, column=0, pady=5)

# Rate selection
tk.Label(
    frame,
    text="Speech Rate",
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="white"
).grid(row=2, column=1, sticky="w")

rate_slider = tk.Scale(
    frame,
    from_=100,
    to=200,
    orient=tk.HORIZONTAL,
    bg="#1e1e1e",
    fg="white",
    troughcolor="#252526",
    highlightthickness=0
)
rate_slider.set(150)
rate_slider.grid(row=3, column=1, padx=10)

# TTS function
def speak_text():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text")
        return

    engine.setProperty("rate", rate_slider.get())

    if voice_combo.get() == "Female":
        engine.setProperty("voice", voices[1].id)
    else:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Speak",
    font=("Segoe UI", 14),
    bg="#007acc",
    fg="white",
    bd=0,
    padx=25,
    pady=8,
    command=speak_text
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    font=("Segoe UI", 14),
    bg="#d83b01",
    fg="white",
    bd=0,
    padx=25,
    pady=8,
    command=lambda: text_area.delete("1.0", tk.END)
).grid(row=0, column=1, padx=10)

root.mainloop()
