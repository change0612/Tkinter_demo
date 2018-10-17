#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import tkinter as tk

window = tk.Tk()
#设置窗体标题
window.title("my window")
# 设置窗体大小
window.geometry("200x100")

var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window,text="hit me",width=15,height=2,command=hit_me)

b.pack()

window.mainloop()
