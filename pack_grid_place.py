#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

# 放置4个方位
# tk.Label(window,text=1).pack(side="top")
# tk.Label(window,text=1).pack(side='bottom')
# tk.Label(window,text=1).pack(side="left")
# tk.Label(window,text=1).pack(side="right")

# 4*3 排列
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i,column=j,ipadx=10,ipady=10)


# 放置到指定的x,y 位置
tk.Label(window, text=1).place(x=10,y=100,anchor='nw')

window.mainloop()