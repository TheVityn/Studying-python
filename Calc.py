import tkinter as tk

def add_symb(num):
    value = panel.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    panel.delete(0, tk.END)
    panel.insert(0, value + str(num))

def make_dot():
    value = panel.get()
    if '+' in value or '-' in value or '/' in value or '*' in value:
        for i in range(len(value) -1, -1, -1):
            if value[i] in '+-*/':
                operant = value[i:]
                if '.' not in operant:
                    if len(operant) <= 1:
                        value += '0.'
                    else:
                        value += '.'
                break
    else:
        if '.' not in value:
            value += '.'


    panel.delete(0, tk.END)
    panel.insert(0, value)

def add_operation(symb):
    value = panel.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculation()
        value = panel.get()
    panel.delete(0, tk.END)
    panel.insert(0, value + symb)


def calculation():
    value = panel.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    panel.delete(0, tk.END)
    result = str(eval(value))
    panel.insert(0, result)

def clear():
    panel.delete(0, tk.END)
    panel.insert(0, '0')

def make_num_bottom(num):
    return tk.Button(win, text=num, font=FONT, bd=4, command= lambda: add_symb(num))

def make_operation_bottom(symb):
    return tk.Button(win, text= symb, font=FONT, bd=4, command= lambda: add_operation(symb))

def make_calculate_bottom(symb):
    return tk.Button(win, text= symb, font=FONT, bd=4, command= calculation)

def make_C_bottom(num):
    return tk.Button(win, text=num, font=FONT, bd=4, command= clear)

def make_dot_bottom(num):
    return tk.Button(win, text=num, font=FONT, bd=4, command= make_dot)

win = tk.Tk()
win.title('First Calculator')
win.geometry('305x280+500+500')
win.maxsize(305, 280)
win.minsize(305, 280)
win.config(bg= "#00CCCC")
photo = tk.PhotoImage(file='img.png')
win.iconphoto(False, photo)
FONT = ('Arial', 15, 'bold')


win.grid_columnconfigure(0, minsize=70)
win.grid_columnconfigure(1, minsize=70)
win.grid_columnconfigure(2, minsize=70)
win.grid_columnconfigure(3, minsize=70)

win.grid_rowconfigure(0, minsize=50)


panel = tk.Entry(win, bg='white', font=FONT, relief= tk.RAISED, bd= -2, justify=tk.RIGHT)
panel.insert(0, '0')
panel.grid(row=0 , column= 0, columnspan=3, stick= 'nswe', padx= 8, pady=8)


bottom1 = make_num_bottom('1').grid(row=1, column=0, stick= 'nswe', padx= 5, pady=5)
bottom2 = make_num_bottom('2').grid(row=1, column=1, stick= 'nswe', padx= 5, pady=5)
bottom3 = make_num_bottom('3').grid(row=1, column=2, stick= 'nswe', padx= 5, pady=5)
bottom4 = make_num_bottom('4').grid(row=2, column=0, stick= 'nswe', padx= 5, pady=5)
bottom5 = make_num_bottom('5').grid(row=2, column=1, stick= 'nswe', padx= 5, pady=5)
bottom6 = make_num_bottom('6').grid(row=2, column=2, stick= 'nswe', padx= 5, pady=5)
bottom7 = make_num_bottom('7').grid(row=3, column=0, stick= 'nswe', padx= 5, pady=5)
bottom8 = make_num_bottom('8').grid(row=3, column=1, stick= 'nswe', padx= 5, pady=5)
bottom9 = make_num_bottom('9').grid(row=3, column=2, stick= 'nswe', padx= 5, pady=5)
bottom0 = make_num_bottom('0').grid(row=4, column=0, stick= 'nswe', padx= 5, pady=5)

bottomPlus = make_operation_bottom('+').grid(row=1, column=3, stick= 'nswe', padx= 5, pady=5)
bottomMinus = make_operation_bottom('-').grid(row=2, column=3, stick= 'nswe', padx= 5, pady=5)
bottomMult = make_operation_bottom('*').grid(row=3, column=3, stick= 'nswe', padx= 5, pady=5)
bottomDev =  make_operation_bottom('/').grid(row=4, column=3, stick= 'nswe', padx= 5, pady=5)

bottomEqual = make_calculate_bottom('=').grid(row=4, column=2, stick= 'nswe', padx= 5, pady=5)
bottomC = make_C_bottom('C').grid(row=0, column=3, stick= 'nswe', padx= 5, pady=5)
bottomDot =  make_dot_bottom('.').grid(row=4, column=1, stick= 'nswe', padx= 5, pady=5)



win.mainloop()
