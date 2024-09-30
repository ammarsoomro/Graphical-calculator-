import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(background="#ADD8E6")  

        self.entry = tk.Entry(master, width=20, font=("Arial", 18), relief="sunken")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',s
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            btn = tk.Button(master, text=button, width=5, font=("Arial", 14), relief="raised", 
                            command=lambda button=button: self.click_button(button))
            btn.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()