import tkinter as tk


def main(parent):
    parent = tk.Frame(parent)
    Register(parent)
    parent.mainloop()
    return None


class Register:
    def __init__(self, parent, *args, **kwargs):

        self.parent = parent
        self.parent = tk.Toplevel()
        self.parent.title("Registration Form")
        self.parent.geometry("425x300")

        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.verifypass = tk.StringVar()
        self.dob = tk.StringVar()

        tk.Label(self.parent, text="Please enter details below:").pack()

        # Main Frame
        frame_Main = tk.Frame(self.parent)
        frame_Main.pack()

        # User Details Frame
        frame_user = tk.LabelFrame(
            frame_Main,
            text="User Details",
        )
        frame_user.grid(
            pady=5,
            padx=5,
        )
        # First Name Label
        tk.Label(frame_user, text="First Name:").grid(
            row=0,
            column=0,
            sticky=tk.E,
            pady=5,
        )
        # First Name Textbox
        self.entry_firstName = tk.Entry(
            frame_user,
            textvariable=self.firstname,
            width=10,
        )
        self.entry_firstName.grid(
            row=0,
            column=1,
            sticky=tk.W,
            padx=5,
            pady=5,
        )
        # Last Name Label
        tk.Label(frame_user, text="Last Name:").grid(
            row=0,
            column=2,
            sticky=tk.E,
            pady=5,
        )
        # Last Name Textbox
        self.entry_lastName = tk.Entry(
            frame_user,
            textvariable=self.lastname,
            width=10,
        )
        self.entry_lastName.grid(
            row=0,
            column=3,
            sticky=tk.W,
            padx=5,
            pady=5,
        )
        # DOB Label
        tk.Label(frame_user, text="DOB:").grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
        )
        # DOB Textbox
        self.entry_DOB = tk.Entry(
            frame_user,
            textvariable=self.dob,
            width=10,
        )
        self.entry_DOB.grid(row=1, column=1)

        # Account Frame
        frame_acct = tk.LabelFrame(
            frame_Main,
            text="Account Information",
        )
        frame_acct.grid(
            row=2,
            column=0,
            columnspan=4,
            pady=5,
            padx=5,
        )
        # Username Label
        tk.Label(frame_acct, text="Username:").grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )
        # Username Textbox
        self.entry_username = tk.Entry(
            frame_acct,
            textvariable=self.username,
            width=10,
        )
        self.entry_username.grid(row=0, column=1)

        # Password Label
        tk.Label(frame_acct, text="Password:").grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
        )
        # Password Textbox
        self.entry_password = tk.Entry(
            frame_acct,
            textvariable=self.password,
            show="*",
            width=10,
        )
        self.entry_password.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
        )
        # Verify Password Label
        tk.Label(frame_acct, text="Verify Password:").grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
        )
        # Verify Password Textbox
        self.entry_verifypass = tk.Entry(
            frame_acct,
            textvariable=self.verifypass,
            show="*",
            width=10,
        )
        self.entry_verifypass.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
        )

        # Button Frame
        frame_button = tk.Frame(frame_Main)
        frame_button.grid(pady=5)

        # Register Button
        btn_register = tk.Button(
            frame_button,
            text="Register",
            width=10,
            bd=3,
            # command=register_user,
        )
        btn_register.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        # Clear all Textboxes
        btn_clear = tk.Button(
            frame_button,
            text="Clear",
            width=10,
            bd=3,
            command=self.clear_form,
        )
        btn_clear.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

    def register(self):
        pass

    def register_user():
        # username_info = username.get()
        # password_info = password.get()

        # file = open(".pfdoc", "w")
        # file.write(username_info)
        # file.write(password_info)
        # file.close()

        # entry_username.delete(0, tk.END)
        # entry_password.delete(0, tk.END)
        pass

    def clear_form(self):
        self.entry_firstName.delete(0, tk.END)
        self.entry_lastName.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_verifypass.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.entry_DOB.delete(0, tk.END)
        # e.DOB.set("mm/dd/yy")
