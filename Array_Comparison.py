
import random

#This is my master array
Master_Schedule = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [1,1,1]]

#These our my employee arrays

Employee_david = [[1, 0, 0],
                 [0, 0, 1],
                 [0, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [1, 0, 0],
                 [5, "David", 0]]

Employee_Jeoffreyi = [[0, 1, 0],
                     [1, 0, 1],
                     [0, 1, 1],
                     [1, 1, 1],
                     [0, 0, 1],
                     [0, 1, 0],
                     [1, 0, 0],
                     [5, "Jeoffreyi", 0]]

Employee_Button = [[1, 0, 0],
                  [0, 0, 1],
                  [0, 1, 0],
                  [0, 1, 0],
                  [1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [5, "Button", 0]]

Employee_Numpy = [[1, 0, 1],
                 [0, 0, 1],
                 [1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [1, 1, 1],
                 [2, "Numpy", 0]]

Employee_Jeremiah = [[1, 0, 0],
                   [1, 0, 1],
                   [0, 0, 0],
                   [0, 1, 0],
                   [0, 1, 0],
                   [0, 1, 1],
                   [1, 1, 0],
                   [2, "Jeremiah", 0]]
#loop through
#shuffle the master_emp_list
Master_Empl_List = [Employee_david,Employee_Jeoffreyi,Employee_Button, Employee_Jeremiah, Employee_Numpy]
shuffled_Master_Empl_List = random.shuffle(Master_Empl_List)
# change to a while true

for k in range (0,(len(Master_Empl_List))):
    name = Master_Empl_List[k][7][1]
    shiftnumb = Master_Empl_List[k][7][0]
    max_shift_counter = 0
    #print(Master_Empl_List[k])

#find replace
    for i in range(0,(len(Master_Schedule))):
        for j in range (0,3):
            if max_shift_counter != shiftnumb:
                #check for fille shifts= 1
                #break
                if (Master_Schedule[i][j]) == 0 and Master_Empl_List[k][i][j] == 1:
                    (Master_Schedule[i][j]) = name
                    max_shift_counter += 1
                if name in (Master_Schedule)[i]:
                    continue
            if max_shift_counter == shiftnumb:
                break

print(Master_Schedule)

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
                self.entry.insert(END, Master_Schedule[i][j])


total_rows = len(Master_Schedule)
total_columns = len(Master_Schedule[0])

gui = Tk()
table = Table(gui)
gui.mainloop()
'''





'''
for i in Master_Schedule:
    if (i == 0):
        print("Thre are empty shifts")
    else:
        print("naur")
'''


