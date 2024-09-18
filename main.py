from tkinter import *

def alert():
    btn.config(text='1')


win = Tk()  # start
win.geometry('400x500')
win.title('계산기')
win.option_add('*Font','맑은고딕')


btn = Button(win, text='7', width=10, height=5).grid(row=1, column=0)
btn = Button(win, text='8', width=10, height=5).grid(row=1, column=1)
btn = Button(win, text='9', width=10, height=5).grid(row=1, column=2)
btn = Button(win, text='C', width=10, height=5).grid(row=1, column=3)

btn = Button(win, text='4', width=10, height=5).grid(row=2, column=0)
btn = Button(win, text='5', width=10, height=5).grid(row=2, column=1)
btn = Button(win, text='6', width=10, height=5).grid(row=2, column=2)
btn = Button(win, text='+', width=10, height=5).grid(row=2, column=3)

btn = Button(win, text='1', width=10, height=5).grid(row=3, column=0)
btn = Button(win, text='2', width=10, height=5).grid(row=3, column=1)
btn = Button(win, text='3', width=10, height=5).grid(row=3, column=2)
btn = Button(win, text='-', width=10, height=5).grid(row=3, column=3)

btn = Button(win, text='*', width=10, height=5).grid(row=4, column=0)
btn = Button(win, text='0', width=10, height=5).grid(row=4, column=1)
btn = Button(win, text='÷', width=10, height=5).grid(row=4, column=2)
btn = Button(win, text='=', width=10, height=5).grid(row=4, column=3)



# end
win.mainloop()
