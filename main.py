from tkinter import *

screen = Tk()
screen.title("GPA Calculator")
screen.minsize(width=300, height=300)


def gpa():
    #obtain data from textbox and convert to list
    grades = grade_enter.get("1.0", END)
    grades = grades.split()
    grades = [float(num) for num in grades]
    classes = len(grades)

    #calculate gpa from num of classes and sum of grades
    final_gpa = sum(grades) / classes
    message = Label(text=f"(gpa for {classes} classes)", font=("Roboto Slab", 8))
    message.place(x=102, y=159)
    result.config(text=f"{final_gpa:.2f}%", font=("Roboto Slab", 8))

    #save calculation to history
    with open("calc_history.txt", mode="a") as history:
        history.writelines(f"{str(final_gpa)}\n")


def read_history():
    with open("calc_history.txt", mode ="r") as history:
        history = history.readlines()

    # create history widget
    history_box = Listbox(width = 10, height=10)
    history_box_append = [history_box.insert(END,item) for item in history]
    history_box.place(x=0, y=180)

    # create a scroll bar
    scrollbar = Scrollbar()
    scrollbar.pack(fill = BOTH)
    scrollbar.place(x=46, y=181.5)

    # add scroll bar to list widget
    history_box.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = history_box.yview)







# initial layout
my_title = Label(text="GPA Calculator", font=("Roboto Slab", 20, "bold"), fg="red", bg="lightgrey")
my_title.pack()

info_label = Label(text="Enter your grades\n**seperate each grade with a space**",
                       font=("Roboto Slab", 10, "italic"),
                       fg="grey")
info_label.pack()

# create grade input
grade_enter = Text(height=4, width=15)
grade_enter.pack()

# create calculation button and label
calc_button = Button(text="Calculate", bg="grey", fg="white", command=gpa)
calc_button.place(x=120, y=183)
calc_info = Label(text="Click to Calculate", font=("Roboto Slab", 6,))
calc_info.place(x=116, y=207)

# create result label
result = Label(text="")
result.place(x=130, y=145)

# create history button
history_button = Button(text="History", bg="grey", fg="white", command=read_history)
history_button.place(x=125, y=240)

history_but_info = Label(text="Click to see history", font=("Roboto Slab", 6,))
history_but_info.place(x=116, y=265)









screen.mainloop()
