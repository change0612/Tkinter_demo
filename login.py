#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title("my window")
window.geometry("450x300")

#welcom image
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')


#user infomation
tk.Label(window,text='User name:').place(x=50,y=150)
tk.Label(window,text='password:').place(x=50,y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_user_name = tk.Entry(window,textvariable=var_usr_name)
entry_user_name.place(x=160,y=150)

var_usr_pwd = tk.StringVar()
entry_user_pwd = tk.Entry(window,textvariable=var_usr_pwd)
entry_user_pwd.place(x=160,y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb')as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome',message='How are you?'+usr_name)
        else:
            tk.messagebox.showwarning(message='Error,you password is weong,try again.')
    else:
        is_sign_up = tk.messagebox.askyesno("Welcome","you have not sign up yet. Sign up today?")
        if is_sign_up:
            usr_sign_up()
def usr_sign_up():
    def sign_to_judge():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error','The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo("Welcome",'You have successfully signed up!')
            window_sign_up.destroy()


    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title("Sign up window")

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up,text="User name:").place(x=10,y=10)
    entry_user_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_user_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    entry_user_pwd = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_user_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="Confirm password:").place(x=10,y=90)
    entry_user_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_user_pwd_confirm.place(x=150,y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up,text='Sign up',command=sign_to_judge)
    btn_comfirm_sign_up.place(x=150,y=130)


#login and sign up button
btn_login = tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=150,y=230)
btn_sign_up = tk.Button(window,text='Sign Up',command=usr_sign_up)
btn_sign_up.place(x=250,y=230)

window.mainloop()