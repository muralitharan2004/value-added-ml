import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.equation = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget to display the equation
        entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
        
        # Clear button
        clear_button = tk.Button(self.root, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")
    
    def on_button_click(self, char):
        current_text = self.equation.get()
        if char == '=':
            try:
                result = str(eval(current_text))
                self.equation.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.equation.set("")
        else:
            new_text = current_text + char
            self.equation.set(new_text)
    
    def clear(self):
        self.equation.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
