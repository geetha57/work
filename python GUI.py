import tkinter as tk

WIDTH = 500
HEIGHT = 500

def show_output_page():
    output_window = tk.Toplevel(root)
    output_window.title("Output")
    output_window.geometry("300x200")
    output_label = tk.Label(output_window, text="Clicked", font=("Arial", 14))
    output_label.pack(expand=True, pady=40)

def on_click():
    show_output_page()

root = tk.Tk()
root.title("500x500 GUI")
root.geometry(f"{WIDTH}x{HEIGHT}")

label = tk.Label(root, text="Hello World", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

root.mainloop()