import tkinter as tk
import registration


def main(parent):
    parent = tk.Frame(parent)
    Login(parent)
    parent.mainloop()
    return None


class Login:
    def __init__(self, parent, *args, **kwargs):

        root = tk.Toplevel()
        root.title("User Login")
        root.geometry("225x150")

        # Main Frame
        frame_Main = tk.Frame(root)
        frame_Main.pack()

        self.lbl_Username = tk.Label(
            frame_Main,
            text="Username:",
        ).pack()
        username_login_entry = tk.Entry(
            frame_Main,
            textvariable="123",
        )
        username_login_entry.pack()

        self.lbl_Password = tk.Label(
            frame_Main,
            text="Password:",
        ).pack()
        password_login_entry = tk.Entry(
            frame_Main,
            textvariable="456",
            show="*",
        )
        password_login_entry.pack()
        tk.Label(
            frame_Main,
            text="",
        ).pack()

        self.btn_frame = tk.Frame(frame_Main)
        self.btn_frame.pack()

        self.btn_Login = tk.Button(
            self.btn_frame,
            text="Login",
            width=5,
            bd=3,
        )
        self.btn_Login.pack(
            side=tk.LEFT,
            padx=5,
        )

        # create a register button
        self.btn_Register = tk.Button(
            self.btn_frame,
            text="Register",
            width=5,
            bd=3,
            command=lambda: registration.main(root),
        )
        self.btn_Register.pack(
            side=tk.RIGHT,
            padx=5,
        )
