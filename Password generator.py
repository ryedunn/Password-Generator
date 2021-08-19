from tkinter import *
from random import SystemRandom
from tk_ToolTip import CreateToolTip
import string
from re import sub

class PassGen(Frame):
    def __init__(self, master=None):
        
        # Checkbox Variables which determines what will be included in the password
        self.varNumbers = IntVar(value=1)
        self.varLowercase = IntVar(value=1)
        self.varUppercase = IntVar(value=1)
        self.varSymbols = IntVar(value=1)

        # Variable for radio button and set default
        self.var_rbtn = IntVar()
        self.var_rbtn.set(2)

        # Text and values to dynamically create radio buttons
        self.modes_rbtn = [
            ('Easy to Say', 1),
            ('Easy to Read', 2),
            ('All characters', 3)
        ]

        # Lists used to store the dynamic checkboxes & radio buttons
        self.dynamic_cbox = []
        self.dynamic_rbuttons = []

        self.vars_cbox = [
            (self.varUppercase, 'Uppercase'),
            (self.varLowercase, 'Lowercase'),
            (self.varNumbers, 'Numbers'),
            (self.varSymbols, 'Symbols')
        ]

        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        # Entry Box for our returned password
        self.entry_Pass = Entry(self)
        self.entry_Pass['text'] = ''
        self.entry_Pass['font'] = ('Helvetica', 20)
        self.entry_Pass['bd'] = 0
        self.entry_Pass['bg'] = '#D8D8D8'
        self.entry_Pass['justify'] = 'center'
        self.entry_Pass['highlightthickness'] = 0
        self.entry_Pass.pack(pady=10)

        # Frame for Options
        self.frame_Options = Frame(self)
        self.frame_Options.pack(pady=10)

        # Character Types Frame
        self.frame_ct = LabelFrame(self.frame_Options)
        self.frame_ct['text'] = 'Character Types'
        self.frame_ct.grid(row=0, column=1, pady=10, padx=10, rowspan=2)

        # Create checkboxes dynamically
         # 0 Upper - 1 Lower - 2 Number - 3 Symbol
        for varType, cbox_label in self.vars_cbox:
            self.checkbutton = Checkbutton(self.frame_ct, pady=5, padx=5)
            self.checkbutton['text'] = cbox_label
            self.checkbutton['variable'] = varType
            self.checkbutton['command'] = lambda: self
            self.dynamic_cbox.append(self.checkbutton)
            self.checkbutton.pack(anchor=W)

        # Password Length Frame
        self.frame_pl = LabelFrame(self.frame_Options)
        self.frame_pl['text'] = 'Password Length'
        self.frame_pl.grid(row=0, column=0, padx=10)

        # Slide designate password length (Default to 12)
        self.scale_pl = Scale(self.frame_pl, from_= 1, to = 99)
        self.scale_pl['orient'] = HORIZONTAL
        self.scale_pl['length'] = 150
        self.scale_pl.set(12)
        self.scale_pl.pack()

        # Pre-set Option Frame
        self.frame_pso = LabelFrame(self.frame_Options)
        self.frame_pso['text'] = 'Pre-set Options'
        self.frame_pso.grid(row=1, column=0, ipadx=10, padx=10, pady=10)

        for text, mode in self.modes_rbtn:
            self.radiobutton = Radiobutton(self.frame_pso)
            self.radiobutton['text'] = text
            self.radiobutton['variable'] = self.var_rbtn
            self.radiobutton['value'] = mode
            self.radiobutton['command'] = lambda: self.setCheckbutton(self.var_rbtn.get())
            self.radiobutton['padx'] = 5
            self.dynamic_rbuttons.append(self.radiobutton)
            self.radiobutton.pack(anchor=W)

        # ToolTips for each Pre-set option
        CreateToolTip(self.dynamic_rbuttons[0], 'Avoid numbers and\nspecial characters')
        CreateToolTip(self.dynamic_rbuttons[1], 'Avoid ambiguous\ncharacters, such\nas l, I, 0, and O')
        CreateToolTip(self.dynamic_rbuttons[2], 'Any character combination')

        # Frame for the Buttons
        self.frame_btn = Frame(self)
        self.frame_btn.pack(pady=5)

        # Button to Generate Password and display it
        self.btn_GenPass = Button(self.frame_btn, text='Generate\nPassword', command=self.genPass, width=10, bd=3)
        self.btn_GenPass.grid(row=0, column=0, padx=5)

        # Button to copy Password to clipboard
        self.btn_Copy = Button(self.frame_btn, text='Copy to\nClipboard', command=self.copyPass, width=10, bd=3)
        self.btn_Copy.grid(row=0, column=1, padx=5)

        # Button to save data to file
        self.btn_Copy = Button(self.frame_btn, text='Save to\nPassword DB', command=self.saveFile, width=10, bd=3)
        self.btn_Copy.grid(row=0, column=2, padx=5)


    # Generate Password
    def genPass(self):

        # Clear Entry Box
        self.entry_Pass.delete(0, END)

    # Get PW Length
        passLength = int(self.scale_pl.get())

        # Variable to hold the password
        randChars = ''

        # Generate Pass
        if self.varUppercase.get() == 1:
            randChars += string.ascii_uppercase
        if self.varLowercase.get() == 1:
            randChars += string.ascii_lowercase
        if self.varNumbers.get() == 1:
            randChars += string.digits
        if self.varSymbols.get() == 1:
            randChars += string.punctuation
        
        # If the easy to read radio button is set, remove ambiguous characters
        if self.var_rbtn.get() ==2:
            randChars = sub(r'''[ILO0l"(),./:;<>[\]\\^_`'{|}~]''', '', randChars)

        # Aggregate all random chars into a string
        generatedPassword = ''.join(SystemRandom().choice(randChars) for x in range(passLength))

        # Output password to the screen
        self.entry_Pass.insert(0, generatedPassword)


    # Copy to clipboard
    def copyPass(self):
        root.clipboard_clear()
        root.clipboard_append(self.entry_Pass.get())


    # Add Site, Encrypt and Save
    def saveFile(self):
        with open('.pfdoc', 'w') as file:
            file.write(self.entry_Pass.get())
            file.close()


    # When a pre-set option is selected, set checkboxes accordingly
    def setCheckbutton(self, value):
        if value == 1: # Easy to Say
            self.varNumbers.set(0)
            self.varSymbols.set(0)
            self.varLowercase.set(1)
            self.varUppercase.set(1)
            self.dynamic_cbox[2]['state'] = DISABLED
            self.dynamic_cbox[3]['state'] = DISABLED
        else:
            self.varNumbers.set(1)
            self.varSymbols.set(1)
            self.varLowercase.set(1)
            self.varUppercase.set(1)
            self.dynamic_cbox[2]['state'] = NORMAL
            self.dynamic_cbox[3]['state'] = NORMAL


if __name__ == '__main__':
    # Main window
    root = Tk()
    root.title('Password Generator')
    root.geometry('400x320')
    app = PassGen(root)
    app.mainloop()
