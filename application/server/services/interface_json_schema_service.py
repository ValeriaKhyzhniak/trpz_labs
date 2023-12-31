from abc import ABC, abstractmethod


class InterfaceJSONSchemaService(ABC):
    @abstractmethod
    def open_file(self, schema_text):
        pass

    @abstractmethod
    def save_file(self, schema_text, file_name):
        pass

    @abstractmethod
    def validate_schema(self, json_text):
        pass

    @abstractmethod
    def export_schema_as_markdown_table(self):
        pass

    @abstractmethod
    def flatten_schema(self, json_text_frame):
        pass
    pass
