from abc import ABC, abstractmethod


class IJSONSchemaService(ABC):

    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def auto_save(self):
        pass

    @abstractmethod
    def validate_schema(self):
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
    def flatten_schema(self):
        pass
