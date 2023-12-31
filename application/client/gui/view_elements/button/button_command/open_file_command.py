from application.client.gui.view_elements.button.button_command.interface_command import InterfaceCommand
from application.client.client import Client
from application.client.gui.view_elements.pages.edit_page_view_strategy import EditPageViewStrategy
from application.client.gui.view_elements.pages.view_context import ViewContext
from application.client.client_file_service import ClientFileService


class OpenFileCommand(InterfaceCommand):
    def __init__(self, application_window):
        super().__init__()
        self.application_window = application_window

    def execute(self):
        w = ClientFileService()
        w.open_file(self.application_window)
