# ============================== Методы для первого сценария ==============================

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FirstTest(BasePage):
    CONTACT_BUTTON = (By.XPATH, "//div[text()='Контакты']")
    CONTACT_BUTTON_CONTACTS = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items .sbisru-link')
    GO_TO_TENSOR = (By.CSS_SELECTOR, 'a[title = "tensor.ru"]')
    BUTTON_ABOUT_TENSOR = (By.CSS_SELECTOR, 'a[href="/about"].tensor_ru-link')
    FIND_IMAGE = (By.CSS_SELECTOR, '.tensor_ru-About__block3 img')

    #Метод для поиска кнопки 'Контакты' и дальнейшей работы с ней, (но наверное нужно было разбить на методы)
    def go_to_contacts(self):
        self.click_element_contacts(self.CONTACT_BUTTON, self.CONTACT_BUTTON_CONTACTS, self.GO_TO_TENSOR,
                                    self.BUTTON_ABOUT_TENSOR)
    #Метод для получения списка картинок
    def find_image(self):
        self.check_images_size(self.FIND_IMAGE)


