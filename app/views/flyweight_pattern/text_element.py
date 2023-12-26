from tkinter import *


class TextElement:
    def __init__(self, master, text, style):
        self.label = Label(master, text=text)
        self.style = style

    def apply_style(self):
        self.label.config(
            font=(self.style.font_family, self.style.font_size),
            fg=self.style.text_color
        )

    def display(self):
        self.apply_style()
        self.label.pack()
