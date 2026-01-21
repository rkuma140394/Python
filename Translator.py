import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
from textblob import TextBlob

translator = Translator()

# Main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("900x520")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="Language Translator",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

# Main frame
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Input text
input_label = tk.Label(
    main_frame,
    text="Enter Text",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
)
input_label.grid(row=0, column=0, sticky="w")

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

# Output text
output_label = tk.Label(
    main_frame,
    text="Translated Text",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
)
output_label.grid(row=0, column=2, sticky="w")

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

# Language selectors
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru"
}

from_lang = ttk.Combobox(
    root,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
from_lang.set("English")
from_lang.pack(pady=5)

to_lang = ttk.Combobox(
    root,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
to_lang.set("Hindi")
to_lang.pack(pady=5)

# Translate function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate")
            return

        src = languages[from_lang.get()]
        dest = languages[to_lang.get()]

        # Using TextBlob for English detection
        blob = TextBlob(text)
        translated = translator.translate(str(blob), src=src, dest=dest)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Translate",
    font=("Segoe UI", 14),
    bg="#007acc",
    fg="white",
    bd=0,
    padx=20,
    pady=8,
    command=translate_text
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
