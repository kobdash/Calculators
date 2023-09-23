import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#a1a1a1")

entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
entry.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)

button_frame = tk.Frame(root, bg="#a1a1a1")
button_frame.pack(fill=tk.BOTH, expand=True)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for button in buttons:
    button = tk.Button(button_frame, text=button, font=("Arial", 18), bd=5, padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.configure(bg="#007acc", fg="white")
    col += 1
    if col > 3:
        col = 0
        row += 1

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

for widget in button_frame.winfo_children():
    widget.configure(font=("Arial", 18))

for widget in button_frame.winfo_children():
    widget.configure(bg="#007acc", fg="white")

entry.bind("<Return>", on_button_click)

for widget in button_frame.winfo_children():
    widget.bind("<Button-1>", on_button_click)

root.mainloop()
