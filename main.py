import tkinter as tk
from PIL import Image, ImageTk
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ===================== MAIN WINDOW =====================
root = tk.Tk()
root.title("Pastel Calculator")
root.geometry("360x520")
root.resizable(False, False)

# ===================== BACKGROUND IMAGE =====================
bg_img = Image.open(resource_path("bg.png"))
bg_img = bg_img.resize((360, 520))
bg_image = ImageTk.PhotoImage(bg_img)

canvas = tk.Canvas(root, width=360, height=520, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# ===================== DISPLAY =====================
expression = ""

display = tk.Entry(
    root,
    font=("Segoe UI", 22),
    bd=0,
    justify="right",
    bg="#ffffff"
)
display.place(x=20, y=40, width=320, height=50)


def press(key):
    global expression
    expression += str(key)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def delete():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

transparent_bg = "#ffffff"
pastel_pink = "#f6b1c3"

def btn(text, x, y, cmd, bg, fg="black"):
    tk.Button(
        root,
        text=text,
        command=cmd,
        font=("Segoe UI", 14),
        bd=0,
        bg=bg,
        fg=fg,
        activebackground=bg,
        relief="flat"
    ).place(x=x, y=y, width=70, height=50)

# ===================== NUMBER BUTTONS =====================
numbers = [
    (7, 20, 140), (8, 100, 140), (9, 180, 140),
    (4, 20, 200), (5, 100, 200), (6, 180, 200),
    (1, 20, 260), (2, 100, 260), (3, 180, 260),
    (0, 100, 320)
]

for num, x, y in numbers:
    btn(num, x, y, lambda n=num: press(n), transparent_bg)

# ===================== OPERATOR BUTTONS =====================
btn("+", 260, 140, lambda: press("+"), pastel_pink)
btn("-", 260, 200, lambda: press("-"), pastel_pink)
btn("×", 260, 260, lambda: press("*"), pastel_pink)
btn("÷", 260, 320, lambda: press("/"), pastel_pink)

btn("C", 20, 320, clear, pastel_pink)
btn("DEL", 180, 320, delete, pastel_pink)
btn("=", 20, 380, equal, pastel_pink)
btn(".", 100, 380, lambda: press("."), transparent_bg)

# ===================== RUN =====================
root.mainloop()
