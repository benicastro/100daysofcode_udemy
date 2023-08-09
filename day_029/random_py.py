def ButClick():
    try:
        MinNum = int (txt1.get())
        MaxNum = int (txt2.get())
        Num = int (txt3.get())
    except ValueError:
        messagebox.showerror("ValueError", "Check if you typed in correct! You can't type in text! Numbers only!")
    else:
        Nums = ''
        if MinNum <= MaxNum:
            last = MinNum - 1
            i = 0
            while i < Num:
                numOne = randint(MinNum,MaxNum)
                if numOne != last:
                    Nums = Nums + " " + str(numOne)
                    i += 1
                    last = numOne
            scr.config(state="normal")
            scr.insert(INSERT, str(Nums) + "\n")
            scr.see("end")
            scr.config(state="disabled")
        else:
            messagebox.showerror("NumError!", "Your Min Number can't be higher than your Max Number or vice versa!")

def copy(scr):
    root.clipboard_get(scr)
    root.clipboard_append(scr)

def remove_text():
    scr.config(state="normal")
    scr.delete(1.0,END)
    scr.config(state="disabled")

def confirm():
    answer = askyesno(title='Exit',
                    message='Tired of randomness?')
    if answer:
        root.destroy()

root = Tk()
root.title("Hey")
message = Label(root, text= "Welcome to random numbers generator! Developed by Yaroslav Poremsky")
message.pack()

root = Tk()
root.title("Random is so random :)")
# Створення кнопок та текстових полів
lb1 = Label(root, bg = "green", text = "Min number")
lb1.grid(
    row = 0,
    column = 0,
    pady = 10,
    padx = 10)

txt1 = Entry(root, width = 30)
txt1.grid(
    row = 0,
    column = 1,
    pady = 10,
    padx = 10)

lb2 = Label(root, bg = "orange", text = "Max number")
lb2.grid(
    row = 1,
    column = 0,
    pady = 10,
    padx = 10)

txt2 = Entry(root, width = 30)
txt2.grid(
    row = 1,
    column = 1,
    pady = 10,
    padx = 10)

lb3 = Label(root,  bg = "pink", text = "Number")
lb3.grid(
    row = 2,
    column = 0,
    pady = 10,
    padx = 10)

txt3 = Entry(root, width = 30)
txt3.grid(
    row = 2,
    column = 1,
    pady = 10,
    padx = 10)

but = Button(root, width = 15, height = 2,  bg = "magenta", text = "Generate", command = ButClick)
but.grid(
    row = 3,
    column = 0,
    columnspan = 2, # кількість суміжних стовпців, які може охоплювати кнопка
    pady = 10,
    padx = 10)

but_remove = Button(root, width = 15, height = 2, bg = "crimson", text = "Remove", command = remove_text)
but_remove.grid(
    row = 3,
    column = 1,
    columnspan = 2,
    pady = 15,
    padx = 20)

but_quit = Button(root, width = 15, height = 2, bg = "violet", text = "Quit", command = confirm)
but_quit.grid(
    row = 3,
    column = 3,
    columnspan = 2,
    pady = 15,
    padx = 20)

but_copy = Button(root, width = 15, height = 2, bg = "violet", text = "Copy", command = copy)
but_copy.grid(
    row = 4,
    column = 3,
    columnspan = 2,
    pady = 15,
    padx = 20)

scr = scrolledtext.ScrolledText(root, bg = "grey", height = 10, state="disable")
scr.grid(
    row = 4,
    column = 0,
    columnspan = 2,
    pady = 10,
    padx = 10)

root.mainloop()