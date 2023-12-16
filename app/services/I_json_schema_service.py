from abc import ABC, abstractmethod


class IJSONSchemaService(ABC):
    @abstractmethod
    def open_file(self, schema_text):
        pass

    @abstractmethod
    def save_as_file(self, schema_text):
        pass

    @abstractmethod
    def save_file(self, schema_text, file_name):
        pass

    @abstractmethod
    def auto_save(self, schema_text, opened_file):
        pass

    @abstractmethod
    def validate_schema(self, json_text):
        pass

    @abstractmethod
    def syntax_highlighting(self):
        pass

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def export_schema(self):
        pass

    @abstractmethod
    def flatten_schema(self, json_text_frame):
        pass
