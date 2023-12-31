class JSONSchema:
    def __init__(self, json_id, json_name, json_data, json_file_path):
        self._json_id = json_id
        self._json_name = json_name
        self._json_data = json_data
        self._json_file_path = json_file_path

    @property
    def json_id(self):
        return self._json_id

    @json_id.setter
    def json_id(self, value):
        self._json_id = value

    @property
    def json_name(self):
        return self._json_name

    @json_name.setter
    def json_name(self, value):
        self._json_name = value

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, value):
        self._json_data = value

    @property
    def json_file_path(self):
        return self._json_file_path

    @json_file_path.setter
    def json_file_path(self, value):
        self._json_file_path = value


