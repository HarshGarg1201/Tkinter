import tkinter

window = tkinter.Tk()
window.title("fill parameter")


tkinter.Label(window, text = "Suf. width", fg = "white", bg = "purple").pack()

tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill ="x")

tkinter.Label(window, text = "Taking all available Y hight", fg = "white", bg = "orange").pack(side="left", fill = "y")

window.mainloop()
