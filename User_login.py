import  tkinter

window = tkinter.Tk()
window.title("Grid")

def say_hi():
    tkinter.Label(window, text = "Welcome to Your Account").pack()

tkinter.Label(window,text ="Username").grid(row= 0)

tkinter.Entry(window).grid(row = 0, column = 1)

tkinter.Label(window, text="Password").grid(row = 1)

tkinter.Entry(window).grid(row =1, column = 1)

tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)

tkinter.Button(window, text = "Log In", command = say_hi, fg = "white", bg = "blue").grid()
window.mainloop()



