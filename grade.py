from tkinter import *


def calc_grade():
    grade = grade_input.get()
    try:
        # try to convert string to int
        grade = int(grade)
    except:
        # change show grade to invalid input
        show_grade.config(text="INVALID INPUT")
        grade_input.delete(0, END)
        print("Error")

    if grade > 100 or grade < 0:
        show_grade.config(text="INVALID INPUT")

    elif grade >= 90 and grade <= 100:
        show_grade.config(text="Your Grade is: A")

    elif grade >= 80 and grade < 90:
        show_grade.config(text="Your Grade is: B")

    elif grade >= 70 and grade < 80:
        show_grade.config(text="Your Grade is: C")

    elif grade >= 60 and grade < 70:
        show_grade.config(text="Your Grade is: D")

    else:
        show_grade.config(text="Your Grade is: F")

    grade_input.delete(0, END)


# setup window
window = Tk()

# setup size
window.geometry("500x500")
# set title
window.title("Grade Calculator")
# false to resize
window.resizable(False, False)

# setup lable
grade_lable = Label(window, text="Enter Your Grade:", font=("Courier", 15))
grade_lable.pack()

# grade input
grade_input = Entry(window, width=10, font=("Courier", 15))
grade_input.pack()

# calculate Button
grade_calc = Button(window, text="Calculate My Grade", height=3, width=20, command=calc_grade)
grade_calc.pack(side="bottom", pady=50)

# show grade Frame
grade_frame = Frame(window)
# show grade lable
show_grade = Label(grade_frame, text="Your Grade is: NONE", font=("Courier", 15))
show_grade.pack(side="bottom")
grade_frame.pack(side="bottom", pady=100)

window.mainloop()
