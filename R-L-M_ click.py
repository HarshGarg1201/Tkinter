import tkinter

window = tkinter.Tk()
window.title("right-left-middle-click")

def left_click(event):
    tkinter.Label(window, text = "left ckick").pack()

def middle_click(event):
    tkinter.Label(window, text = "middle click").pack()

def right_click(event):
    tkinter.Label(window, text = "right click").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()