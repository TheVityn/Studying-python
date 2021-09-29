import tkinter as tk

FONT = ('Arial', 12, 'bold')

def get_label(text):
    label = tk.Label(window, text= text, font= FONT, bg= '#4C4AFF', justify= tk.RIGHT)
    return label

def bmi_calculation(heigh, weight):
    BMI = round((weight / heigh ** 2), 1)
    return BMI

def get_color(bmi):
    if bmi < 18.5:
        color = '#A7F7F7'
        text = 'Underweight. Please contact Your doctor.'
    elif bmi > 25:
        color = '#FAFA6E'
        text = 'Overweight. Do something with it.'
        if bmi > 30:
            color = '#FA8E6E'
            text = 'Obese. Please contact Your doctor.'
    else:
        color = '#8DFC90 '
        text = 'Congratulation! You have normal weight.'

    return color, text

def get_digits(entry):
    object = entry.get()
    for no in object:
        if no not in '1234567890':
            print(no)
            answer = get_label('Enter not digit value...')
            return False




def make_it(weight, height):
    weight = get_digits(weight)
    height = get_digits(height)
    if weight == False or height == False:
        return None




window = tk.Tk()
window.title('MY BMI PROGRAM')
window.geometry('400x300+500+500')
image = tk.PhotoImage(file='img.png')
window.iconphoto(False, image)
window.config(bg= '#4C4AFF')
window.grid_columnconfigure(0, minsize= 100)
window.grid_columnconfigure(1, minsize= 100)
window.grid_columnconfigure(2, minsize= 100)
window.grid_columnconfigure(3, minsize= 100)

window.grid_rowconfigure(0, minsize= 30)
window.grid_rowconfigure(1, minsize= 30)
window.grid_rowconfigure(2, minsize= 30)
window.grid_rowconfigure(3, minsize= 30)

nameLabel = get_label('Username:')
weightLabel = get_label('Weight:')
heightLabel = get_label('Height:')
answer = get_label('')
name = tk.Entry(window, font= FONT, bg= '#4D4AFF')
weight = tk.Entry(window, font= FONT, bg= '#4C4AFF')
height = tk.Entry(window, font= FONT, bg= '#4C4AFF')

button = tk.Button(window,font= FONT, text= 'Calculate', bg= '#4C4AFF', command= lambda: make_it(weight, height))

name.grid(row= 0, column= 1, stick= 'nswe', padx= 5, pady= 5)
weight.grid(row= 1, column= 1, stick= 'nswe', padx= 5, pady= 5)
height.grid(row= 2, column= 1, stick= 'nswe', padx= 5, pady= 5)
nameLabel.grid(row= 0, column= 0, stick= 'e', padx= 5, pady= 5)
weightLabel.grid(row= 1, column= 0, stick= 'e', padx= 5, pady= 5)
heightLabel.grid(row= 2, column= 0, stick= 'e', padx= 5, pady= 5)
button.grid(row= 0, column= 2, stick= 'nswe', rowspan=3, padx= 5, pady= 5)
answer.grid(row= 3, column= 0,  stick= 'e',  columnspan= 3, rowspan= 3, padx= 5, pady= 5)

window.mainloop()

