from app.views.strategy.interface_view_strategy import InterfaceViewStrategy


class ViewContext:
    strategy = InterfaceViewStrategy

    def __init__(self, strategy: InterfaceViewStrategy):
        super().__init__()
        self.strategy = strategy

    def view_page_strategy(self, page):
        return self.strategy.create_operating_window(page)


