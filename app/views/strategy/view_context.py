from app.views.strategy.I_view_strategy import IViewStrategy


class ViewContext:
    strategy = IViewStrategy

    def __init__(self, strategy: IViewStrategy):
        super().__init__()
        self.strategy = strategy

    def view_page_strategy(self, page):
        return self.strategy.create_operating_window(page)


