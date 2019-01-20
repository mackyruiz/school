# Ch9 ex 9.7
# Macky Ruiz
# CIS 007

from tkinter import * # Import tkinter

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Grid") # Set a title

        width = 200
        height = 200
        canvas = Canvas(window, bg = "white", width = width, height = height)
        canvas.pack()

        count = 25
        while count < 180:
            canvas.create_line(count, 10, count, 190, fill="red", width = 1)
            canvas.create_line(10, count, 190, count, fill="blue", width = 1)
            count += 25

        window.mainloop()
        
MainGUI()
