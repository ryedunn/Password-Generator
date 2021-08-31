from tkinter import messagebox
import tkinter as tk
from random import SystemRandom
import string
from re import sub
from tk_ToolTip import CreateToolTip
import Login


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        app = parent

        # File Section of Menubar
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=fileMenu)

        fileMenu.add_command(label="User Login", command=lambda: Login.main(self))
        fileMenu.add_command(label="New User")
        openFileMenu = tk.Menu(self)
        openFileMenu.add_command(label="Recent")
        openFileMenu.add_command(label="Browse")
        fileMenu.add_cascade(label="Open User File", menu=openFileMenu)
        fileMenu.add_command(label="Add Site")
        fileMenu.add_command(label="Exit", underline=1, command=app.custom_quit)

        # Edit Section of Menubar
        editMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Clear", command=app.clear_pass)
        editMenu.add_cascade(label="Redo")
        editMenu.add_command(
            label="Cut",
            command=lambda: [app.copy_pass(), app.clear_pass()],
        )
        editMenu.add_command(label="Copy", command=app.copy_pass)

        # Tools Section of Menubar
        toolsMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Tools", menu=toolsMenu)
        toolsMenu.add_command(label="Password Strength")
        toolsMenu.add_cascade(label="Placeholder")

        runMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Run", menu=runMenu)
        runMenu.add_command(label="Placeholder")

        # Options Section of Menubar
        optionsMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Options", menu=optionsMenu)

        # Pre-Set Option SubMenu
        psoMenu = tk.Menu(self)
        psoMenu.add_command(
            label="Easy to Say",
            command=lambda: [app.var_rbtn.set(1), app.setCheckbutton(1)],
        )
        psoMenu.add_command(
            label="Easy to Read",
            command=lambda: [app.var_rbtn.set(2), app.setCheckbutton(2)],
        )
        psoMenu.add_command(
            label="Unrestricted",
            command=lambda: [app.var_rbtn.set(3), app.setCheckbutton(3)],
        )
        optionsMenu.add_cascade(label="Pre-Set Options", menu=psoMenu)
        optionsMenu.add_command(label="Placeholder")

        # Window Section of Menubar
        windowMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Window", menu=windowMenu)
        windowMenu.add_command(label="Resize window")
        windowMenu.add_command(label="Large window")

        # Help Section of Menubar
        helpMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About PassGen")
        helpMenu.add_cascade(label="PassGen Help")
        helpMenu.add_command(label="Contact")


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("Password Generator")
        parent.geometry("400x320")

        menubar = MenuBar(self)
        parent.config(menu=menubar)

        # Checkbox Variables that determines whats included in the password
        self.varNumbers = tk.IntVar(value=1)
        self.varLowercase = tk.IntVar(value=1)
        self.varUppercase = tk.IntVar(value=1)
        self.varSymbols = tk.IntVar(value=1)

        # Variable for radio button and set default
        self.var_rbtn = tk.IntVar()
        self.var_rbtn.set(2)

        # Text and values to dynamically create radio buttons
        self.modes_rbtn = [
            ("Easy to Say", 1),
            ("Easy to Read", 2),
            ("Unrestricted", 3),
        ]

        # Lists used to store the dynamic checkboxes & radio buttons
        self.dynamic_cbox = []
        self.dynamic_rbuttons = []

        self.vars_cbox = [
            (self.varUppercase, "Uppercase"),
            (self.varLowercase, "Lowercase"),
            (self.varNumbers, "Numbers"),
            (self.varSymbols, "Symbols"),
        ]

        # Create Widgets for the Form
        tk.Frame.__init__(self)
        self.pack()

        # Entry Box for our returned password
        self.entry_Pass = tk.Entry(
            self,
            text="",
            font=("Helvetica", 20),
            bd=0,
            bg="#D8D8D8",
            justify="center",
            highlightthickness=0,
        )
        self.entry_Pass.pack(pady=10)

        # Frame for Options
        self.frame_Options = tk.Frame(self)
        self.frame_Options.pack(pady=10)

        # Character Types Frame
        self.frame_ct = tk.LabelFrame(
            self.frame_Options,
            text="Character Types",
        )
        self.frame_ct.grid(
            row=0,
            column=1,
            pady=10,
            padx=10,
            rowspan=2,
        )

        # Create checkboxes dynamically
        # 0 Upper - 1 Lower - 2 Number - 3 Symbol
        for varType, cbox_label in self.vars_cbox:
            self.checkbutton = tk.Checkbutton(
                self.frame_ct,
                text=cbox_label,
                variable=varType,
                pady=5,
                padx=5,
            )
            self.dynamic_cbox.append(self.checkbutton)
            self.checkbutton.pack(anchor=tk.W)

        # Password Length Frame
        self.frame_pl = tk.LabelFrame(
            self.frame_Options,
            text="Password Length",
        )
        self.frame_pl.grid(
            row=0,
            column=0,
            padx=10,
        )

        # Slide designate password length (Default to 12)
        self.scale_pl = tk.Scale(
            self.frame_pl,
            from_=1,
            to=99,
            orient=tk.HORIZONTAL,
            length=150,
        )
        self.scale_pl.set(12)
        self.scale_pl.pack()

        # Pre-set Option Frame
        self.frame_pso = tk.LabelFrame(
            self.frame_Options,
            text="Pre-set Options",
        )
        self.frame_pso.grid(
            row=1,
            column=0,
            ipadx=10,
            padx=10,
            pady=10,
        )

        for text, mode in self.modes_rbtn:
            self.radiobutton = tk.Radiobutton(
                self.frame_pso,
                text=text,
                variable=self.var_rbtn,
                value=mode,
                command=lambda: self.setCheckbutton(self.var_rbtn.get()),
                padx=5,
            )
            self.dynamic_rbuttons.append(self.radiobutton)
            self.radiobutton.pack(anchor=tk.W)

        # ToolTips for each Pre-set option
        CreateToolTip(
            self.dynamic_rbuttons[0],
            "Avoid numbers and\nspecial characters",
        )
        CreateToolTip(
            self.dynamic_rbuttons[1],
            "Avoid ambiguous\ncharacters, such\nas l, I, 0, and O",
        )
        CreateToolTip(
            self.dynamic_rbuttons[2],
            "Any character combination",
        )

        # Frame for the Buttons
        self.frame_btn = tk.Frame(self)
        self.frame_btn.pack(pady=5)

        # Button to Generate Password and display it
        self.btn_GenPass = tk.Button(
            self.frame_btn,
            text="Generate\nPassword",
            command=self.genPass,
            width=10,
            bd=3,
        ).grid(
            row=0,
            column=0,
            padx=5,
        )

        # Button to copy Password to clipboard
        self.btn_Copy = tk.Button(
            self.frame_btn,
            text="Copy to\nClipboard",
            command=self.copy_pass,
            width=10,
            bd=3,
        ).grid(
            row=0,
            column=1,
            padx=5,
        )

        # Button to save data to file
        self.btn_Copy = tk.Button(
            self.frame_btn,
            text="Save to\nPassword DB",
            command=lambda: self.saveFile(),
            width=10,
            bd=3,
        ).grid(
            row=0,
            column=2,
            padx=5,
        )

    # Generate Password
    def genPass(self):

        # Clear Entry Box
        self.clear_pass()

        # Get PW Length
        passLength = int(self.scale_pl.get())

        # Variable to hold the password
        randChars = ""

        try:
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
            if self.var_rbtn.get() == 2:
                randChars = sub(r"""[ILO0l"(),./:; <>[\]\\^_`'{|}~]""", "", randChars)

            # Aggregate all random chars into a string
            generatedPassword = "".join(
                SystemRandom().choice(randChars) for x in range(passLength)
            )
        except IndexError:
            tk.messagebox.showinfo(
                "ERROR",
                "No options selected.",
            )

        # Output password to the screen
        self.entry_Pass.insert(0, generatedPassword)

    # Copy to clipboard
    def copy_pass(self):
        self.clipboard_clear()
        self.clipboard_append(self.entry_Pass.get())

    # Send to Login page to Encrypt and Save
    def saveFile(self):
        # If user is logged in, save file, if not send to login screen
        # FileManager.FileStuff.fileStuff(self, self.entry_Pass.get())
        # Login.Login.form(self)
        Login.main(self)

    # When a pre-set option is selected, set checkboxes accordingly
    def setCheckbutton(self, value):
        if value == 1:  # Easy to Say
            self.varNumbers.set(0)
            self.varSymbols.set(0)
            self.varLowercase.set(1)
            self.varUppercase.set(1)
            self.dynamic_cbox[2]["state"] = tk.DISABLED
            self.dynamic_cbox[3]["state"] = tk.DISABLED
        else:
            self.varNumbers.set(1)
            self.varSymbols.set(1)
            self.varLowercase.set(1)
            self.varUppercase.set(1)
            self.dynamic_cbox[2]["state"] = tk.NORMAL
            self.dynamic_cbox[3]["state"] = tk.NORMAL

    def clear_pass(self):
        self.entry_Pass.delete(0, tk.END)

    def custom_quit(self):
        answer = messagebox.askokcancel(
            "Exit Program", "Are you sure you want to exit?"
        )
        if answer:
            quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.mainloop()
