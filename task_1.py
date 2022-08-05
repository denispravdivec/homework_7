import tkinter as tk
def get_entry():
    value = name.get()
    value_1 = name_1.get()
    value_2 = name_2.get()
    if value:
        print(value, value_1, value_2)
    else:
        print("empty")
window = tk.Tk()
window.geometry(f"400x500+100+200")
tk.Label(window, text="нік").grid(row=0,column=0)
tk.Label(window, text="електронна пошта").grid(row=1,column=0)
tk.Label(window, text="пароль").grid(row=2,column=0)
name = tk.Entry(window)
name.grid(row=0, column=1)
name_1 = tk.Entry(window)
name_1.grid(row=1, column=1)
name_2 = tk.Entry(window)
name_2.grid(row=2, column=1)
tk.Button(window,text='register', command= get_entry).grid(row=3,column=1)
window.grid_columnconfigure(0,minsize=200)
window.grid_columnconfigure(1,minsize=100)
window.mainloop()