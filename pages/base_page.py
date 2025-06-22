# Импорты стандартных, сторонних и пользовательских модулей:
# - явные ожидания и условия для Selenium
# - обработка исключений Selenium
# - кастомный логгер проекта
# - драйвер браузера из conftest для тестов
# - работа со временем

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logger import logger
from tests.conftest import driver
import time
import os

class BasePage:
    BASE_URL = 'https://saby.ru/'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.BASE_URL)

#=========================================== Методы для первого сценария ==============================================

    #Метод задействуется первым и вторым сценарием для работы с кнопкой "Контакты"
    def click_element_contacts(self, *locators):
        for i, locator in enumerate(locators, start=1):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                logger.info(f"Клик по элементу №{i} с локатором {locator} прошёл успешно")

                if len(self.driver.window_handles) == 2:
                    self.driver.switch_to.window(self.driver.window_handles[-1])


            except TimeoutException:
                logger.error(f"Элемент №{i} с локатором {locator} не появился или не кликабелен")
            except Exception as q:
                logger.error(f'Произошла ошибка {q}')

    #Поиск картинок и дальнейшее их сравнение
    def check_images_size(self, locator):
        image_list = self.wait.until(EC.presence_of_all_elements_located(locator))

        if not image_list:
            logger.info("Картинки не найдены")
            return

        first_width = image_list[0].get_attribute("width")
        first_height = image_list[0].get_attribute("height")
        logger.info(f"Размер картинки № 1 - (высота - {first_height}, ширина - {first_width})")

        for i, img in enumerate(image_list[1:], start=2):
            width = img.get_attribute("width")
            height = img.get_attribute("height")
            logger.info(f'Размер картинки № {i + 1} - (высотка - {height}, ширина - {width})')
            assert width == first_width, f"У картинки №{i} ширина {width}, отличается от первой {first_width}"
            assert height == first_height, f"У картинки №{i} высота {height}, отличается от первой {first_height}"

# =========================================== Методы для второго сценария ===========================================

    #Проверка правильно ли отобразился регион
    def check_region(self, locator):
        try:
            region_element = self.wait.until(EC.visibility_of_element_located(locator))
            region = region_element.text
            if region == 'Тюменская обл.':
                logger.info(f'Регион совпадает: {region}')
            else:
                logger.error(f'Регион не совпадает: {region}')
        except TimeoutException:
            logger.error('Элемент региона не появился на странице')
        except Exception as e:
            logger.error(f'Ошибка при проверке региона: {e}')

    #Проверка списка партнеров по региону
    def check_list_partners(self, locator):
        try:
            list_partners = self.wait.until(EC.presence_of_all_elements_located(locator))

            if list_partners:
                logger.info(f'Список партнёров из количества {len(list_partners)} отображён')
            else:
                logger.error('Список партнёров пуст')
        except TimeoutException:
            logger.error('Список партнёров не появился на странице')
        except Exception as e:
            logger.error(f'Ошибка при проверке списка партнёров: {e}')


    #Клик по кнопке с регионом для отображения дилогового окна со всеми регионами
    def region_button_click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info('Диалоговая панель с регионами отображена')
        except TimeoutException:
            logger.error('Диалоговая панель с регионами не отобразилась')
        except Exception as q:
            logger.error(f'Произошла ошибка {q}')

    #Смена региона на Камчатский край
    def region_chooser(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            time.sleep(2)
            element.click()
            logger.info('Регион изменен на Камчатский край')
        except TimeoutException:
            logger.info('Смена региона не удалась')
        except Exception as q:
            logger.error(f'Произошла ошибка {q}')

    #Проверка изменился ли регион на Камчатский край в title и на страние рядом с 'Контакты'
    def checking_title_and_chooser_region(self, locator, expected_region):
        try:
            display_region = self.wait.until(EC.visibility_of_element_located(locator)).text
            title_region = self.driver.title.split('—')[-1].strip()
            assert title_region == expected_region, (
                f"В title ожидали регион '{expected_region}', а получили '{title_region}'"
            )
            assert display_region == expected_region, (
                f"На странице рядом с 'Контакты' ожидали регион '{expected_region}', а получили '{display_region}'"
            )

            logger.info(f"Регион корректно отображается в title и на странице: {expected_region}")

        except TimeoutException:
            logger.error("Элемент с отображением региона не найден на странице")
        except Exception as q:
            logger.error(f'Произошла ошибка {q}')

    #Проверка региона в url
    def checking_ulr_region(self, url_name):
        try:
            url_region = ' '.join(self.driver.current_url.split('-')[1:]).split('?')[0]
            assert url_region == url_name, (
                f'В url ожидали {url_name}, а получили {url_region}'
            )
            logger.info(f'Регион корректно отображается в url: {url_region}')
        except TimeoutException:
            logger.error('Не удалось получить url')
        except Exception as q:
            logger.error(f'Произошла ошибка {q}')


    def checking_partners_list_kamchatka(self, locator, expected_region):
        try:
            kamchatka = self.wait.until(EC.visibility_of_element_located(locator)).text
            assert kamchatka == expected_region, (
                f'Список партнеров не отображен согласно региона: {expected_region}'
            )
            logger.info(f'Список партнеров отображается согласно региона: {kamchatka}')
        except TimeoutException:
            logger.error('Не удалось получить список партнеров')
        except Exception as q:
            logger.error(f'Произошла ошибка: {q}')


# =========================================== Методы для третьего сценария ===========================================
    #Нажимаем кнопку "Скачать локальные версии"
    def go_to_download_button(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            time.sleep(5)
            logger.info('Перешли по кнопке "Скачать локальные версии"')
        except TimeoutException:
            logger.error('Перейти по кнопке "Скачать локальные версии" не удалось"')
        except Exception as q:
            logger.error(f'Произошла ошибка: {q} при попытке перейти по кнопке "Скачать локальные версии"')

    #Скачиваем exe файл
    def download_plugin_setup(self, locator):
        try:
            plugin = self.wait.until(EC.element_to_be_clickable(locator))
            plugin.click()
            logger.info('Нажали на кнопку скачать плагин')
        except TimeoutException:
            logger.error(f'Не удалось нажать на кнопку плагин')
        except Exception as q:
            logger.error(f'Произошла ошибка {q}')

    #Ждем и убеждаемся, что файл скачан
    def wait_for_file(self, filename, timeout=10):
        download_path = os.path.join(os.getcwd(), "downloads")
        file_path = os.path.join(download_path, filename)
        logger.info(f"Ждем файл {filename} в папке {download_path}...")
        try:
            for i in range(timeout):
                if os.path.exists(file_path):
                    logger.info(f"Файл {filename} найден.")
                    break
                time.sleep(1)
        except Exception as q:
            logger.error(f"Ошибка: {q}. Файл {filename} не появился за {timeout} секунд.")

    #Получаем размер файла на сайте
    def check_plugin_exe_size(self, locator, filename):
        try:
            size_on_site = self.wait.until(EC.visibility_of_element_located(locator))
            size_on_site = ' '.join(size_on_site.text.split()[2:]).strip(')')
            logger.info(f'Размер файла {filename} на сайте: {size_on_site}')
            self.size_on_site = size_on_site.split()[0]
        except TimeoutException:
            logger.error(f'Не удалось получить размер файла {filename} на сайте')

    #Получаем размер скачанного на диск файла
    def check_plugin_local(self, filename):
        try:
            download_path = os.path.join(os.getcwd(), "downloads")
            file_path = os.path.join(download_path, filename)
            if os.path.exists(file_path):
                size_bytes = os.path.getsize(file_path)
                size_mb = size_bytes / (1024 * 1024)
                logger.info(f"Размер файла {filename} на диске: {size_mb:.2f} МБ")
                self.size_mb = round(float(size_mb), 2)
            else:
                logger.error(f'Не удалось получить размер локального файла {filename}')
        except Exception as q:
            logger.error(f'Произошла ошибка при получения размера локального файла: {q}')

    #Сравниваем размер файла на диске и на сайте
    def compare_files(self, filename):
        try:
            if not hasattr(self, 'size_mb') or not hasattr(self, 'size_on_site'):
                logger.error("Данные о размерах не получены. Выполни сначала методы получения размеров.")
                return

            if float(self.size_mb) == float(self.size_on_site):
                logger.info(f"Размеры файлов- {filename} совпадают: {self.size_mb} МБ")
            else:
                logger.error(f"Размеры не совпадают! Локально: {self.size_mb} МБ, на сайте: {self.size_on_site} МБ")
        except Exception as e:
            logger.error(f"Ошибка при сравнении размеров: {e}")







