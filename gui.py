import tkinter as tk
from tkinter import messagebox
from send_email import send_email
from receive_email import receive_email

def send_email_action():
    sender = sender_entry.get()
    password = password_entry.get()
    reciever = reciever_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)
    # check if all fields are filled
    if sender and password and reciever and subject and body.strip():
        send_email(sender, password, reciever, subject, body)
        messagebox.showinfo("Success", "Email sent successfully!")
    #show warning if there is a field missing
    else:
        messagebox.showwarning("Warning", "Please fill in all fields!")

def receive_email_action():
    sender = sender_entry.get()
    password = password_entry.get()
    # check if sender email and password are provided
    if sender and password:
        email_content = receive_email(sender, password)
        messagebox.showinfo("Received Email", email_content)
    else:
        messagebox.showwarning("Warning", "Please enter your email and password!")

#Create the main application window
root = tk.Tk()
root.title("Email Client")
root.geometry("500x400")

tk.Label(root, text="Email:").pack()
sender_entry = tk.Entry(root, width=50)
sender_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, width=50, show="*") #hides password
password_entry.pack()

tk.Label(root, text="Reciever Email:").pack()
reciever_entry = tk.Entry(root, width=50)
reciever_entry.pack()

tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Body:").pack()
body_entry = tk.Text(root, width=40, height=3)
body_entry.pack()

send_button = tk.Button(root, text="Send Email", command=send_email_action)
send_button.pack(pady=10)

receive_button = tk.Button(root, text="Receive Email", command=receive_email_action)
receive_button.pack(pady=10)

root.mainloop()