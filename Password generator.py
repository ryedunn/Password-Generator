# Password generator
from tkinter import *
import random
from tk_ToolTip import CreateToolTip
import string

# Main window
root = Tk()
root.title('Password Generator')
root.geometry("400x300")

# Checkbox Variables which determines what will be included in the password
varNumbers = IntVar(value=1)
varLowercase = IntVar(value=1)
varUppercase = IntVar(value=1)
varSymbols = IntVar(value=1)

# Generate Password
def genPass():

    # Clear Entry Box
    entry_Pass.delete(0, END)

    # Get PW Length
    passLength = int(scale_pl.get())

    # Variable to hold the password
    randChars = ''

    # Generate Pass
    # Check if the easy to read radio button is set, else use individual checkboxes
    if var_rbtn.get() == 2:  
        randChars += easyToRead() 
    else:
        if varUppercase.get() == 1:
            randChars += string.ascii_uppercase
        if varLowercase.get() == 1:
            randChars += string.ascii_lowercase
        if varNumbers.get() == 1:
            randChars += string.digits
        if varSymbols.get() == 1:
            randChars += string.punctuation

    # Aggregate all random chars into a string
    generatedPassword = ''.join(random.choice(randChars) for x in range(passLength))

    # Output password to the screen
    entry_Pass.insert(0, generatedPassword)

# Removal of ambiguous characters
def easyToRead():
    randChars = string.ascii_letters + string.punctuation
    return randChars.translate(str.maketrans('', '', r"""'IOl0+,-./:;<>[\]"()_`{|}~"""))

# Copy to clipboard
def copyPass():
    root.clipboard_clear()
    root.clipboard_append(entry_Pass.get())

# When a pre-set option is selected, set checkboxes accordingly
def setCheckboxes(value):
    if value == 1: # Easy to read
        varNumbers.set(0); varSymbols.set(0); varLowercase.set(1); varUppercase.set(1)
    else: 
        varNumbers.set(1); varSymbols.set(1); varLowercase.set(1); varUppercase.set(1)

# Entry Box for our returned password
entry_Pass = Entry(root, text='', font=('Helvetica', 20), bd=0, bg='#D8D8D8', justify='center', highlightthickness=0)
entry_Pass.pack(pady=10)

# Frame for Options
frame_Options = Frame(root)
frame_Options.pack(pady=10)

# Character Types Frame
frame_ct = LabelFrame(frame_Options, text='Character Types')
frame_ct.grid(row=0, column=1, pady=10, padx=10, rowspan=2)

# List used to store the dynamic checkbox/buttons
dynamic_cbox = []

vars_cbox = [
    (varUppercase, 'Uppercase'),
    (varLowercase, 'Lowercase'),
    (varNumbers, 'Numbers'),
    (varSymbols, 'Symbols')
]

# Create checkboxes
for varType, cbx_label in vars_cbox:
    checkbutton = Checkbutton(frame_ct, text=cbx_label, variable=varType, pady=5, padx=5)
    dynamic_cbox.append(checkbutton)
    checkbutton.pack(anchor=W)  # Pack (grid, etc..) method returns None so it must be on a separate line

# Password Length Frame
frame_pl = LabelFrame(frame_Options, text='Password Length')
frame_pl.grid(row=0, column=0, padx=10)

# Slide designate password length (Default to 12)
scale_pl = Scale(frame_pl, from_=1, to=99, orient=HORIZONTAL, length=150)
scale_pl.set(12)
scale_pl.pack()

# Pre-set Option Frame
frame_pso = LabelFrame(frame_Options, text='Pre-set Options')
frame_pso.grid(row=1, column=0, ipadx=10, padx=10, pady=10)

# Add text and values to dynamically create radio buttons
modes_rbtn = [
    ('Easy to Say', 1),
    ('Easy to Read', 2),
    ('All characters', 3)
]

# Variable for radio button and set default
var_rbtn = IntVar()
var_rbtn.set(2)

# List of radio buttons so they can be referenced for ToolTip
dynamic_rbuttons = []

# Dynamically create RadioButtons appending them to a list
for text, mode in modes_rbtn:
    radiobutton = Radiobutton(frame_pso, text=text, variable=var_rbtn,
                              value=mode, command=lambda: setCheckboxes(var_rbtn.get()), padx=5)
    dynamic_rbuttons.append(radiobutton)
    radiobutton.pack(anchor=W)

# ToolTips for each Pre-set option
rbtn_Say_ttp = CreateToolTip(dynamic_rbuttons[0], 'Avoid numbers and\nspecial characters')
rbtn_Read_ttp = CreateToolTip(dynamic_rbuttons[1], 'Avoid ambiguous\ncharacters, such\nas l, I, 0, and O')
rbtn_All_ttp = CreateToolTip(dynamic_rbuttons[2], 'Any character combination')

# Frame for the Buttons
frame_btn = Frame(root)
frame_btn.pack(pady=10)

# Button to Generate Password and display it
btn_GenPass = Button(frame_btn, text='Generate Password', command=genPass)
btn_GenPass.grid(row=0, column=0, padx=10)

# Button to copy Password to clipboard
btn_Copy = Button(frame_btn, text='Copy to Clipboard', command=copyPass)
btn_Copy.grid(row=0, column=1, padx=10)

root.mainloop()
