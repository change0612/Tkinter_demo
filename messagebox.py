#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# 弹窗
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

def hit_me():
    tk.messagebox.showinfo(title='Hi',message='hahaha')
    tk.messagebox.showwarning(title="HI",message="nonono")
    tk.messagebox.showerror(title="HI", message="No!never")
    tk.messagebox.askquestion(title="HI", message="hahahah")
    tk.messagebox.askyesno(title="HI", message="hahahah")
    tk.messagebox.asktrycancel(title="HI", message="hahahah")
    tk.messagebox.askokcancel(title="HI", message="hahahah")


tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()