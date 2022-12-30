from tkinter import *

FONT =("Arial", 20, "normal")

def solve():
    a = int(a_input.get())
    b = int(b_input.get())
    c = int(c_input.get())
    discriminant = b**2-4*a*c
    if discriminant < 0:
        result = "no real roots"





window =Tk()
window.title("Quadratic Equation Solver")
window.minsize(width=500, height=300)
window.config(padx=50, pady=20)

# create labels
standard_form_label = Label(text="Equation in Standard Form", font=FONT)
standard_form_label.grid(column=0,row=0, columnspan=6, sticky='ew')



x_squared_label = Label(text="x² +", font=FONT)
x_squared_label.grid(column=1, row=1)

x_label = Label(text="x +", font=FONT)
x_label.grid(column=3, row=1, sticky='w')

equal_zero_label =Label(text="= 0", font=FONT)
equal_zero_label.grid(column=5, row=1)

solution_text_label = Label(text="Solution:",font=FONT)
solution_text_label.grid(column=0,row=4, columnspan=8, sticky='w')

solution_1_label = Label(text="x=",font=FONT)
solution_1_label.grid(column=0, row=5)

solution_2_label = Label(text="or   x=  ",font=FONT)
solution_2_label.grid(column=2, row=5)
# create Entry boxes
a_input = Entry(width=10)
a_input.insert(END,string="a")
a_input.grid(column=0,row=1)

b_input = Entry(width=10)
b_input.insert(END,string="b")
b_input.grid(column=2,row=1)

c_input = Entry(width=10)
c_input.insert(END,string="c")
c_input.grid(column=4,row=1)

solution_1_output = Entry(width=10)
solution_1_output.insert(END,string="Root 1")
solution_1_output.grid(column=1, row=5)

solution_2_output = Entry(width=10)
solution_2_output.insert(END,string="Root 2")
solution_2_output.grid(column=3, row=5)
# create button
calculate_button = Button(text="Solve Me!", font=FONT, command=solve)
calculate_button.grid(row=3,columnspan=4, sticky='e')




window.mainloop()