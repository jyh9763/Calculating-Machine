from tkinter import Tk
from tkinter import Button

def alert():
    btn.config(text='1')


win = Tk()  # start
win.geometry('400x500')
win.title('계산기')
win.option_add('*Font','맑은고딕')

btn = Button(win)
btn.config(width=5, height=2)
btn.config(text='0')
btn.config(command=alert)


btn.pack()



# end
win.mainloop()
