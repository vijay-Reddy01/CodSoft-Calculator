import tkinter as tkn

is_on = False

def press(num):
    if is_on:
        global expression
        expression = expression + str(num)
        equation.set(expression)

def equalpress():
    if is_on:
        try:
            global expression
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        except:
            equation.set(" error ")
            expression = ""

def clr():
    if is_on:
        global expression
        expression = ""
        equation.set("")

def delete():
    if is_on:
        global expression
        expression = expression[:-1]
        equation.set(expression)

def percent():
    if is_on:
        global expression
        try:
            result = str(eval(expression) / 100)
            equation.set(result)
            expression = ""
        except:
            equation.set(" error ")
            expression = ""

def turn_on():
    global is_on
    is_on = True
    clr()
    entry_box.config(state='normal')

def turn_off():
    global is_on
    is_on = False
    clr()
    entry_box.config(state='disabled')

if __name__ == "__main__":
    gui = tkn.Tk()
    gui.configure(background="yellow")
    gui.title("Simple Calculator")
    gui.geometry("235x285")

    expression = ""
    equation = tkn.StringVar()
    entry_box = tkn.Entry(gui, textvariable=equation, state='disabled', font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
    entry_box.grid(columnspan=4, ipadx=8)
    btn1 = tkn.Button(gui, text=' 1 ', foreground='black', background='yellow', command=lambda: press(1), height=2, width=7)
    btn1.grid(row=2, column=0)
    btn2 = tkn.Button(gui, text=' 2 ', foreground='black', background='yellow', command=lambda: press(2), height=2, width=7)
    btn2.grid(row=2, column=1)
    btn3 = tkn.Button(gui, text=' 3 ', foreground='black', background='yellow', command=lambda: press(3), height=2, width=7)
    btn3.grid(row=2, column=2)
    btn4 = tkn.Button(gui, text=' 4 ', foreground='black', background='yellow', command=lambda: press(4), height=2, width=7)
    btn4.grid(row=3, column=0)
    btn5 = tkn.Button(gui, text=' 5 ', foreground='black', background='yellow', command=lambda: press(5), height=2, width=7)
    btn5.grid(row=3, column=1)
    btn6 = tkn.Button(gui, text=' 6 ', foreground='black', background='yellow', command=lambda: press(6), height=2, width=7)
    btn6.grid(row=3, column=2)
    btn7 = tkn.Button(gui, text=' 7 ', foreground='black', background='yellow', command=lambda: press(7), height=2, width=7)
    btn7.grid(row=4, column=0)
    btn8 = tkn.Button(gui, text=' 8 ', foreground='black', background='yellow', command=lambda: press(8), height=2, width=7)
    btn8.grid(row=4, column=1)
    btn9 = tkn.Button(gui, text=' 9 ', foreground='black', background='yellow', command=lambda: press(9), height=2, width=7)
    btn9.grid(row=4, column=2)
    btn0 = tkn.Button(gui, text=' 0 ', foreground='black', background='yellow', command=lambda: press(0), height=2, width=7)
    btn0.grid(row=5, column=0)

    plus = tkn.Button(gui, text=' + ', foreground='black', background='orange', command=lambda: press("+"), height=2, width=7)
    plus.grid(row=2, column=3)
    minus = tkn.Button(gui, text=' - ', foreground='black', background='orange', command=lambda: press("-"), height=2, width=7)
    minus.grid(row=3, column=3)
    multiply = tkn.Button(gui, text=' * ', foreground='black', background='orange', command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=4, column=3)
    divide = tkn.Button(gui, text=' / ', foreground='black', background='orange', command=lambda: press("/"), height=2, width=7)
    divide.grid(row=5, column=3)

    equal = tkn.Button(gui, text=' = ', foreground='black', background='green', command=equalpress, height=2, width=7)
    equal.grid(row=6, column=0, columnspan=4, sticky="nsew")
    clr = tkn.Button(gui, text='Clear', foreground='black', background='orange', command=clr, height=2, width=7)
    clr.grid(row=1, column=2)
    delete = tkn.Button(gui, text='Del', foreground='black', background='orange', command=delete, height=2, width=7)
    delete.grid(row=1, column=3)
    dot= tkn.Button(gui, text=' . ', foreground='black', background='yellow', command=lambda: press("."), height=2, width=7)
    dot.grid(row=5, column=1)
    percent = tkn.Button(gui, text=' % ', foreground='black', background='orange', command=percent, height=2, width=7)
    percent.grid(row=5, column=2)

    on = tkn.Button(gui, text='ON', foreground='black', background='green', command=turn_on, height=2, width=7)
    on.grid(row=1, column=0)
    off = tkn.Button(gui, text='OFF', foreground='black', background='red', command=turn_off, height=2, width=7)
    off.grid(row=1, column=1)

    gui.mainloop()
