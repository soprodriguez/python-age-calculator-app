from tkinter import *  # Import everything from the Tkinter library
import datetime
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x200")  # Set window size as a string "widthxheight"
#root.resizeable(0,0) or root.resizable(width=False, height=False) to not allow people to expand GUI window
#print(root)  # Print the reference of the Tkinter window object in the console

def apple():
    birthdate = datetime.datetime(int(YearVariable.get()), int(MonthVariable.get()), int(DayVariable.get()))
    age = datetime.datetime.now() - birthdate
    convertdays = int(age.days)
    convertyears = round(convertdays / 365, 2)
    Label(text = f"{NameVariable.get()} your age is {convertyears} years old").grid(row = 6, column = 1)





lb1 = Label(root, text = "Your Name").grid(row =1, column =1)
lb2 = Label(root, text = "Your Birth Year").grid(row = 2, column =1)
lb3 = Label(root, text = "Your Birth Month").grid(row = 3, column =1)
lb4 = Label(root, text = "Your Birth Day").grid(row = 4, column =1)

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()

EntryName = Entry(root, textvariable = NameVariable).grid(row = 1, column = 2)
EntryYear = Entry(root, textvariable = YearVariable).grid(row = 2, column = 2)
EntryMonth = Entry(root, textvariable = MonthVariable).grid(row = 3, column = 2)
EntryDay = Entry(root, textvariable = DayVariable).grid(row = 4, column = 2)

button1 = Button(root, text = "Calculate Age", command = apple).grid(row = 5, column = 1)
#button1 = Button(root, text = "Calculate Age")
#button1.grid(row = 5, column = 1)

root.mainloop()  # Use root.mainloop() instead of mainloop()
