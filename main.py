'''
Andres Yengle
5/19/22
This is my GUI program for my scheduling IA Project
This will take a csv file and make a schedule with it
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

# tkinter window
root.geometry("1000x800")
# title of window
root.title('Schedule')
# color of window
root.configure(bg='light blue')

root.resizable(0, 0)

#configure the grid


'''
Titles and Labels for different buttons
'''
#Hello title
hello_title = Label(root, text='Hello Manager!', font =('calibra', 36, 'bold'), bg='light blue')
hello_title.grid(column=6, row=0)

#welcome title
welcome_title = Label(root, text='Welcome to my scheduling program!', font =('calibra', 36, 'bold'), bg='light blue')
welcome_title.grid(column=6, row=1,)

#Schedule Label
schedule_label = Label(root, text='This is the current schedule for next week', font =('calibra', 20, 'bold'), bg='light blue')
schedule_label.grid(column=6, row=2)

'buttons for first window'

#Edit Employee profile button
prof_button = Button(root, text='Edit Employee Profiles', font=('calibra',12,), bg='light blue' )
prof_button.grid(column=0, row=3)

#Add or remove employee button
add_or_remove = Button(root, text='Add or remove employees', bg='light blue')
add_or_remove.grid(column=0, row=4)


root.mainloop()

'buttons for first window'

#Edit Employee profile button
prof_button = Button(root, text='Edit Employee Profiles', font=('calibra',12,), bg='light blue' )
prof_button.grid(column=0, row=3)

#Add or remove employee button
add_or_remove = Button(root, text='Add or remove employees', bg='light blue')
add_or_remove.grid(column=0, row=4)


root.mainloop()