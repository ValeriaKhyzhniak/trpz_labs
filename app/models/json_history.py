class JSONHistory:
    def __init__(self, history_id, json_id, date_of_saving):
        self.history_id = history_id
        self.json_id = json_id
        self.date_of_saving = date_of_saving

    @property
    def history_id(self):
        return self.history_id

    @history_id.setter
    def history_id(self, value):
        self.history_id = value

    @property
    def json_id(self):
        return self.json_id

    @json_id.setter
    def json_id(self, value):
        self.json_id = value

    @property
    def date_of_saving(self):
        return self.date_of_saving

    @date_of_saving.setter
    def date_of_saving(self, value):
        self.date_of_saving = value.upper()


