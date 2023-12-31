import traceback
from application.server.services.json_schema_service import JSONSchemaService
import socket
import threading


class Server:
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            with self.socket as s:
                s.bind((self.host, self.port))
                s.listen(5)
                print(f"Server listening on {self.host}:{self.port}")
                while True:
                    client_socket, addr = s.accept()
                    print(f"Accepted connection from {addr}")
                    client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                    client_handler.start()
        except KeyboardInterrupt:
            print("Server terminated by user.")
        except Exception as e:
            print(f"Error in start method: {str(e)}")
            traceback.print_exc()

    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(1024).decode("utf-8")
            # Отримання типу запиту та даних від клієнта
            request_type, data, path = data.split("|", 2)
            # Логіка обробки запиту в залежності від типу
            if request_type == "VALIDATE":
                state, response = self.validate_json(data)
            elif request_type == "FLATTEN_VIEW":
                response = self.json_to_flatten_view(data)
            elif request_type == "OPEN_FILE":
                response = self.open_json_file()
            elif request_type == "SAVE_FILE":
                response = self.save_json_file(data, path)
            elif request_type == "EXPORT_MARKDOWN":
                response = self.export_json_as_markdown_table(data)
            # Відправка відповіді клієнту
            client_socket.sendall(response.encode("utf-8"))
        except Exception as e:
            # Зареєструвати деталі винятку
            print(f"Помилка у функції handle_client: {str(e)}")
            traceback.print_exc()  # Вивести повний стек винятку для отримання повної інформації

            # Відправити відповідь із помилкою клієнту
            error_response = "Помилка: щось пішло не так на сервері"
            client_socket.sendall(error_response.encode('utf-8'))
        finally:
            # Закриття сокету у будь-якому випадку
            client_socket.close()

    def open_json_file(self):
        return self.json_schema_service.open_file()

    def save_json_file(self, data, path):
        return self.json_schema_service.save_file(data, path)

    def validate_json(self, message):
        return self.json_schema_service.validate_schema(message)

    def json_to_flatten_view(self, message):
        return self.json_schema_service.flatten_schema(message)

    def export_json_as_markdown_table(self, message):
        return self.json_schema_service.export_schema_as_markdown_table(message)
