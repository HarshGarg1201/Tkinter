import tkinter

window = tkinter.Tk()
window.title("My first GUI")

top_frame= tkinter.Frame(window).pack()
bottom_frame= tkinter.Frame(window).pack(side = "bottom")

btn1 = tkinter.Button(bottom_frame, text = "Button 1", fg = "red").pack(side= "left")
btn2 = tkinter.Button(top_frame, text = "button 2", fg = "green").pack(side= "left")
btn3 = tkinter.Button(bottom_frame, text = "button 3", fg = "purple").pack(side = "right")
btn4 = tkinter.Button(top_frame, text = "Button 4",fg = "orange").pack(side = "right")


window.mainloop()