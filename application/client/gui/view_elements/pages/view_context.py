from application.client.gui.view_elements.pages.interface_view_strategy import InterfaceViewStrategy


class ViewContext:
    strategy = InterfaceViewStrategy

    def __init__(self, strategy: InterfaceViewStrategy):
        super().__init__()
        self.strategy = strategy

    def view_page_strategy(self, application_window, name):
        return self.strategy.create_application_tab_frame(application_window, name)


