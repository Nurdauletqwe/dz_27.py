import sys
import os
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Placeholder Downloader")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel(
            "Нажмите кнопку, чтобы скачать данные с JSON Placeholder")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Скачать данные")
        self.button.clicked.connect(self.download_data)
        self.layout.addWidget(self.button)

    def download_data(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            data = response.json()
            self.save_data(data)
            QMessageBox.information(
                self, "Успех", "Данные успешно скачаны и сохранены!")
        else:
            QMessageBox.critical(
                self, "Ошибка", "Не удалось загрузить данные.")

    def save_data(self, data):
        folder_name = "json_data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_path = os.path.join(folder_name, "posts.json")
        with open(file_path, "w") as file:
            json.dump(data, file)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
