from tkinter import messagebox
import tkinter as tk
from random import SystemRandom
import string
from re import sub
from tk_ToolTip import CreateToolTip
import FileManager


class PassGen(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()

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

        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        menu1 = tk.Menu(root)
        root.configure(menu=menu1)

        submenu1 = tk.Menu(menu1)
        menu1.add_cascade(label="File", menu=submenu1)

        submenu1.add_command(label="New User")
        sub1menu = tk.Menu(menu1)
        sub1menu.add_command(label="Recent")
        sub1menu.add_command(label="Browse")
        submenu1.add_cascade(label="Open User File", menu=sub1menu)
        submenu1.add_command(label="Add Site")
        submenu1.add_command(label="Quit", command=self.custom_quit)

        # adding command to menu elements
        submenu2 = tk.Menu(menu1)
        menu1.add_cascade(label="Edit", menu=submenu2)
        submenu2.add_command(label="Clear", command=self.clear_pass)
        submenu2.add_cascade(label="Redo")
        submenu2.add_command(label="Cut", command=lambda: [self.copy_pass(), self.clear_pass()])
        submenu2.add_command(label="Copy", command=self.copy_pass)

        submenu3 = tk.Menu(menu1)
        menu1.add_cascade(label="Tools", menu=submenu3)
        submenu3.add_command(label="Password Strength")
        submenu3.add_cascade(label="Placeholder")

        submenu4 = tk.Menu(menu1)
        menu1.add_cascade(label="Run", menu=submenu4)
        submenu4.add_command(label="Placeholder")

        submenu5 = tk.Menu(menu1)
        menu1.add_cascade(label="Options", menu=submenu5)
        sub5menu = tk.Menu(menu1)
        sub5menu.add_command(label="Easy to Say", command=lambda: [self.var_rbtn.set(1),
                             self.setCheckbutton(1)])
        sub5menu.add_command(label="Easy to Read", command=lambda: [self.var_rbtn.set(2),
                             self.setCheckbutton(2)])
        sub5menu.add_command(label="Unrestricted", command=lambda: [self.var_rbtn.set(3),
                             self.setCheckbutton(3)])
        submenu5.add_cascade(label="Pre-Set Options", menu=sub5menu)
        submenu5.add_command(label="Placeholder")

        submenu6 = tk.Menu(menu1)
        menu1.add_cascade(label="Window", menu=submenu6)
        submenu6.add_command(label="Resize window")
        submenu6.add_command(label="Large window")

        submenu7 = tk.Menu(menu1)
        menu1.add_cascade(label="Help", menu=submenu7)
        submenu7.add_command(label="About PassGen")
        submenu7.add_cascade(label="PassGen Help")
        submenu7.add_command(label="Contact")

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
            command=self.saveFile,
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
        FileManager.FileStuff.fileStuff(self, self.entry_Pass.get())

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
        answer = messagebox.askokcancel("Exit Program", "Are you sure you want to exit?")
        if answer:
            quit()


if __name__ == "__main__":
    # Main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x320")
    app = PassGen(root)
    root.mainloop()
