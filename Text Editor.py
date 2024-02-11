import tkinter as tk
from tkinter import filedialog

import customtkinter

bright = True
def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def dark_mode():
    txt_edit.configure(bg="black")
    txt_edit.configure(fg="white")
    frm_buttons.configure(bg="#202020")
    global bright
    bright = False

def white_mode():
    txt_edit.configure(bg="white")
    txt_edit.configure(fg="black")
    frm_buttons.configure(bg="#E0E0E0")
    global bright
    bright = True

def theme():
    global bright
    if bright == True:
        dark_mode()
    else:
        white_mode()


window = customtkinter.CTk()
window.title("Text Editor")
window.iconbitmap('text-editor.ico')
window.configure(fg_color="black")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window,font=("Calibri", "18"))
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = customtkinter.CTkButton(frm_buttons,
                                   text="Abrir",
                                   command=open_file,
                                   fg_color="black")
btn_save = customtkinter.CTkButton(frm_buttons,
                                   text="Salvar",
                                   command=save_file,
                                   fg_color="black")
btn_darkmode = customtkinter.CTkButton(frm_buttons,
                                    text="Dark Mode",
                                    command=theme,
                                    fg_color="black")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_darkmode.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()