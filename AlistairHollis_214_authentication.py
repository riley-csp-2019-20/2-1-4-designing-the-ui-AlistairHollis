import tkinter as tk

# window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

# blue
blue = tk.Frame(bg="blue", width=150, height=100)
blue.grid(row=0, column=0)

# green
green = tk.Frame(bg="green", width=150, height=100)
green.grid(row=0, column=1)

# red
red = tk.Frame(bg="red", width=150, height=100)
red.grid(row=1, column=0)

# yellow
yellow = tk.Frame(bg="yellow", width=150, height=100)
yellow.grid(row=1, column=1)

root.mainloop()