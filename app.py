import smtplib
from smtplib import SMTPAuthenticationError
import tkinter as tk
from tkinter import messagebox

from_email = "## YOUR GMAIL EMAIL ID HERE ##"
password = "# YOUR PASSWORD HERE #"

def send_mail():
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email.get(),
                                msg=f"Subject:{subject.get()}\n\n{message.get(1.0, tk.END)}")
    except SMTPAuthenticationError:
        messagebox.showerror("AuthenticationError",message="The Email or Password in the code is incorrect\n You can use apps password from google account if not woking")
    else:
        messagebox.showinfo("Successful",message="Email Sent Successfully!! :)")


# -------------------- GUI CODE ---------------- #
root = tk.Tk()
root.title("Email Composer")
root.config(padx=20, pady=20)

t = tk.Label(text="To: ")
t.grid(row=2, column=0)
s = tk.Label(text="Subject: ")
s.grid(row=3, column=0)
b = tk.Label(text="Body:")
b.grid(row=4, column=0)

to_email = tk.Entry(width=50)
to_email.grid(row=2, column=1)

subject = tk.Entry(width=50)
subject.grid(row=3, column=1)

message = tk.Text(width=38)
message.grid(row=4, column=1)

send_btn = tk.Button(text="SEND", relief="groove", command=send_mail, width=20, pady=10)
send_btn.grid(row=5, column=1)

root.mainloop()
