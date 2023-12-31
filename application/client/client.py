import socket


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_validation_request(self, data):
        return self.send_request(f"VALIDATE|{data}|")

    def send_json_to_flatten_view_request(self, data):
        return self.send_request(f"FLATTEN_VIEW|{data}|")

    def export_schema_as_markdown_table(self, data):
        return self.send_request(f"EXPORT_MARKDOWN|{data}|")

    def send_request(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                # Встановлення з'єднання
                client_socket.connect(("localhost", 12345))
                # Перевірка з'єднання перед відправкою даних
                if client_socket.fileno() == -1:
                    raise ConnectionError("Connection failed")
                # Відправлення даних
                client_socket.send(data.encode('utf-8'))
                # Отримання відповіді
                response = client_socket.recv(1024).decode('utf-8')
                return response
        except Exception as e:
            return f"Error: {str(e)}"
