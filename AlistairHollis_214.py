# modules
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x150")
root.title("Authentication")

# functions
def test_my_button():
  prn_password = ent_password.get()
  frame_auth.tkraise()
  print(prn_password)
  lbl_display_password.config(text=prn_password)

# new frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=5, pady=5)

lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(padx=5, pady=5)

btn_login = tk.Button(frame_login, text="Log In", font="Ariel", command=test_my_button)
btn_login.pack()

# authentication frame

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_display_password = tk.Label(frame_auth)
lbl_display_password.pack()

# initialization
frame_login.tkraise()

# mainloop
root.mainloop()