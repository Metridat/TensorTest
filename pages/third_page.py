# Импорты стандартных и сторонних модулей:
# - локаторы Selenium для поиска элементов на странице
# - базовый класс страниц проекта (общие методы и функциональность)

# ============================== Методы для второго третьего ==============================

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ThirdTest(BasePage):
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[href='/download']")
    DOWNLOAD_EXE = (By.CSS_SELECTOR, 'a[href*="setup-web"]')
    FILE_NAME = 'saby-setup-web.exe'

    #Нажимаем кнопку "Скачать локальные версии"
    def click_download_button(self):
        self.go_to_download_button(self.DOWNLOAD_BUTTON)

    # Скачиваем exe файл
    def click_download_plugin(self):
        self.download_plugin_setup(self.DOWNLOAD_EXE)

    # Ждем и убеждаемся, что файл скачан
    def wait_file_exe(self):
        self.wait_for_file(self.FILE_NAME)

    # Получаем размер файла на сайте
    def check_file_size(self):
        self.check_plugin_exe_size(self.DOWNLOAD_EXE, self.FILE_NAME)

    # Получаем размер скачанного на диск файла
    def check_file_size_local(self):
        self.check_plugin_local(self.FILE_NAME)

    # Сравниваем размер файла на диске и на сайте
    def compering_files(self):
        self.compare_files(self.FILE_NAME)





