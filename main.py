from tkinter import *


root = Tk()
root.geometry("250x250")
root.title("Calculadora")
mi_frame = Frame(root, width=230, height=230)
mi_frame.pack()

display = Entry(mi_frame)
display.grid(row=1 , columnspan=6, sticky=W+E)

i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i +=1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()

def calculate():
    display_state = display.get()
    try:
        #math_exp = parser.expr(display_state).compile()
        resultado = eval(display_state)
        clear_display()
        display.insert(0, resultado)
    #except expression as identifier:
    except:
        clear_display()
        display.insert(0, "Error")

#Numeric buttons
Button(mi_frame, text="1", command=lambda : get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(mi_frame, text="2", command=lambda : get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(mi_frame, text="3", command=lambda : get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(mi_frame, text="4", command=lambda : get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(mi_frame, text="5", command=lambda : get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(mi_frame, text="6", command=lambda : get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(mi_frame, text="7", command=lambda : get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(mi_frame, text="8", command=lambda : get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(mi_frame, text="9", command=lambda : get_numbers(9)).grid(row=4, column=2, sticky=W+E)

#Buttons

Button(mi_frame, text="AC", command=lambda: clear_display()).grid(row=5, column=0, sticky=W+E)
Button(mi_frame, text="0", command=lambda : get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(mi_frame, text="%", command=lambda: get_operation("%")).grid(row=5, column=2, sticky=W+E)

Button(mi_frame, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=W+E)
Button(mi_frame, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(mi_frame, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(mi_frame, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=W+E)

Button(mi_frame, text="⌫", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(mi_frame, text="exp", command=lambda: get_operation("**")).grid(row=3, column=4, sticky=W+E)
Button(mi_frame, text="^2", command=lambda: get_operation("**2")).grid(row=3, column=5, sticky=W+E)
Button(mi_frame, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=W+E)
Button(mi_frame, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(mi_frame, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()