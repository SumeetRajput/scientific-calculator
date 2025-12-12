import tkinter as tk
import math

# ----------------------------
# SCIENTIFIC CALCULATOR
# ----------------------------
class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("420x550")
        self.root.config(bg="#1e1e1e")  # Dark theme

        self.equation = tk.StringVar()

        # Display screen
        self.display = tk.Entry(
            root, textvariable=self.equation, font=("Arial", 22),
            bd=10, insertwidth=2, width=24, borderwidth=4,
            relief="ridge", bg="#000000", fg="#00FF00"
        )
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

        self.create_buttons()

    def create_buttons(self):
        # Scientific buttons
        sci_buttons = [
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2),
            ("log", 1, 3), ("√", 1, 4), ("x²", 1, 5),

            ("asin", 2, 0), ("acos", 2, 1), ("atan", 2, 2),
            ("ln", 2, 3), ("^", 2, 4), ("π", 2, 5),
        ]

        for (txt, r, c) in sci_buttons:
            self.make_button(txt, r, c, "#333333", "#ffffff")

        # Normal calculator buttons
        buttons = [
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('+', 3, 3), ('C', 3, 4), ('AC', 3, 5),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3), ('(', 4, 4), (')', 4, 5),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('*', 5, 3), ('.', 5, 4), ('%', 5, 5),
            ('0', 6, 0), ('00', 6, 1), ('=', 6, 2), ('/', 6, 3), ('EXP', 6, 4), ('ANS', 6, 5),
        ]

        for (txt, r, c) in buttons:
            self.make_button(txt, r, c, "#444444", "#00FFAA")

    def make_button(self, txt, r, c, bg, fg):
        button = tk.Button(
            self.root, text=txt, padx=20, pady=20, font=("Arial", 14),
            bg=bg, fg=fg, activebackground="#555555",
            command=lambda t=txt: self.on_button_click(t)
        )
        button.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        eq = self.equation.get()

        if char == "C":
            self.equation.set("")

        elif char == "←":
            self.equation.set(eq[:-1])

        elif char == "=":
            try:
                result = str(eval(eq))
                self.equation.set(result)
            except:
                self.equation.set("Error")

        elif char == "sin":
            self.equation.set(str(math.sin(math.radians(float(eq)))))
        elif char == "cos":
            self.equation.set(str(math.cos(math.radians(float(eq)))))
        elif char == "tan":
            self.equation.set(str(math.tan(math.radians(float(eq)))))

        elif char == "asin":
            self.equation.set(str(math.degrees(math.asin(float(eq)))))
        elif char == "acos":
            self.equation.set(str(math.degrees(math.acos(float(eq)))))
        elif char == "atan":
            self.equation.set(str(math.degrees(math.atan(float(eq)))))

        elif char == "log":
            self.equation.set(str(math.log10(float(eq))))
        elif char == "ln":
            self.equation.set(str(math.log(float(eq))))

        elif char == "√":
            self.equation.set(str(math.sqrt(float(eq))))
        elif char == "x²":
            self.equation.set(str(float(eq) ** 2))

        elif char == "π":
            self.equation.set(eq + str(math.pi))

        elif char == "^":
            self.equation.set(eq + "**")

        elif char == "EXP":
            self.equation.set(eq + "e")

        else:
            self.equation.set(eq + char)


# ----------------------------
# MAIN PROGRAM
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
