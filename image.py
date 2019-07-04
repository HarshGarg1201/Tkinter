import  tkinter

window = tkinter.Tk()
window.title("printing an image")

icon =tkinter.PhotoImage( file ="C:\Users\Harsh_Garg\141812_original_3670x5506.png")

label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()