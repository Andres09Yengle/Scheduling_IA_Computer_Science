'''
This is like a sample table I created in order to learn how to code the table
I am trying to decide whether to have the schedule pop out or to try and input in my main GUI
'''

from tkinter import *
# Table class
class Table:
    # Initialize a constructor
    def __init__(self, gui):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                print(i)
                if i ==0:
                    self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                    self.entry = Entry(gui, width=20, fg='blue',
                               font=('Arial', 16, ''))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, schedule_list[i][j])


# take the data
schedule_list = [('Shift', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
        ('AM', 'Gorge', 'California', 'Gorge', 'California','Gorge', 'California','Gorge' ),
       ('MID', 'Maria', 'New York', 'Gorge', 'California','Gorge', 'California','Gorge'),
       ('PM', 'Albert', 'Berlin', 'Gorge', 'California','Gorge', 'California','Gorge'),]

# find total number of rows and
# columns in list
total_rows = len(schedule_list)
total_columns = len(schedule_list[0])

# create root window
gui = Tk()
table = Table(gui)
gui.mainloop()