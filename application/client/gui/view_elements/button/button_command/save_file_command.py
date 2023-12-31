from application.client.gui.view_elements.button.button_command.interface_command import InterfaceCommand
from application.client.client_file_service import ClientFileService


class SaveFileCommand(InterfaceCommand):
    def __init__(self, application_window):
        super().__init__()
        self.application_window = application_window

    def execute(self):
        w = ClientFileService()
        w.choose_tab_for_saving(self.application_window)
