# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            with open('html/contact.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.send_response(200)  # Отправка кода ответа
                self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
                self.end_headers()  # Завершение формирования заголовков ответа
                self.wfile.write(bytes(html_content, "utf-8"))  # Тело ответа

        except FileNotFoundError:
                self.send_response(404)  # Отправка кода ответа 404 Not Found
                self.end_headers()
                self.wfile.write(b"404 Not Found")  # Сообщение об ошибке


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")