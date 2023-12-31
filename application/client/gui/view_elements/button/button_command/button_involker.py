class ButtonInvoker:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        # Виликаємо метод execute() для команди
        self.command.execute()
