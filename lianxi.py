#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from tkinter import *
import tkinter as tk
import requests,json

#创建主窗口及Label组件

window = tk.Tk()
window.title('json post window')
window.geometry('500x300')

# var = tk.StringVar()#创建字符串对象
# var1 = tk.StringVar()#创建字符串对象
# l = tk.Label(window,textvariable=var,bg='green',font=('Arial,12'),width=60,height=10)#创建label对象
# l1 = tk.Label(window,textvariable=var1,bg='skyblue',font=('Arial,12'),width=60,height=2)#创建label对象
# l.pack()
# l1.pack()

# window.mainloop()

##################################Button窗口组件
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         url = 'http://www.xj.com/api/Pmcreport/pythonCheck'
#         data = {'company_id':1,'member_id':16}
#         r =requests.post(url,data)
#         var.set(r.content)
#         var1.set(url)
#     else:
#         on_hit = False
#         var.set('')
# b = tk.Button(window,text='post',font=('Arial',12),width=10,height=1,command=hit_me)
# b.pack()
# window.mainloop()

##################################Entry窗口部件
#在图形界面上设定输入框空间entry并放置
# e1 = tk.Entry(window,show='*',font=('Arial',14))#显示成密码形式
# e2 = tk.Entry(window,show=None,font=('Arial',14))#显示成明文形式
# e1.pack()
# e2.pack()
# window.mainloop()

##################################Text窗口部件
e = tk.Entry(window,show = None)
e.pack()
def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end',var)
b1 = tk.Button(window,text='insert point',width=10,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',width=10,height=2,command=insert_end)
b2.pack()
t = tk.Text(window,height=3)
t.pack()
window.mainloop()