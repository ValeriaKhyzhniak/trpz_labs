class JSONSchema:
    def __init__(self, json_id, json_name, json_data):
        self.json_id = json_id
        self.json_name = json_name
        self.json_data = json_data

    @property
    def json_id(self):
        return self.json_id

    @json_id.setter
    def json_id(self, value):
        self.json_id = value

    @property
    def json_name(self):
        return self.json_name

    @json_name.setter
    def json_name(self, value):
        self.json_name = value.upper()

    @property
    def json_data(self):
        return self.json_data

    @json_data.setter
    def json_data(self, value):
        self.json_data = value.upper()


