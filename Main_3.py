'''
This will be the log in for the manager, I have decided that employees shouldn't have access to it so It will only be able
to log in under one username and password.
'''


from tkinter import *

root = Tk()

# tkinter window
root.geometry("800x800")
# title of window
root.title('Schedule')
# color of window
root.configure(bg='light blue')

root.resizable(0, 0)



'''
Titles and Labels for different buttons
'''


#Welcome Tittle

welcome_title = Label(root, text='Hello User!', font =('calibra', 36, 'bold'), bg='light blue')
welcome_title.grid(column=0, row=0)

login_title = Label(root, text='Please login using your username and password', font=('calibra', 36, 'bold'), bg='light blue')
login_title.grid(column=0, row=1)

username_entry_title = Label(root, text='Username:', font =('calibra', 24), bg= 'light blue')
username_entry_title.grid(column=0, row=2)

username_entry = Entry(root, font=('calibra', 10, 'normal'))
username_entry.grid(column=1, row=2)

Password_entry_title = Label(root, text='Password:', font =('calibra', 24), bg= 'light blue')
Password_entry_title.grid(column=0, row=3)

password_entry = Entry(root, font=('calibra', 10, 'normal'))
password_entry.grid(column=1, row=3)








root.mainloop()