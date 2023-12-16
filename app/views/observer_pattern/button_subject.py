from tkinter import *
from app.views.command_pattern.interface_command import InterfaceCommand
from app.views.observer_pattern.subject import Subject


class ButtonSubject(Button, Subject):
    def __init__(self, main_frame, text, _command: InterfaceCommand):
        Subject.__init__(self)
        Button.__init__(self)
        self.button = Button(main_frame, text=text, command=self.press_button)
        self.button.pack()
        self.main_frame = main_frame
        self._command = _command

    def press_button(self):
        print("Кнопка була натиснута.")
        message = self._command.execute()
        # Викликаємо метод notify_observers
        self.notify_observers(message)
