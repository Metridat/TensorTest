# Импорты стандартных и сторонних модулей:
# - локаторы Selenium для поиска элементов на странице
# - базовый класс страниц проекта (общие методы и функциональность)
# - работа со временем
# ============================== Методы для второго сценария ==============================

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class SecondTest(BasePage):
    CONTACT_BUTTON = (By.XPATH, "//div[text()='Контакты']")
    CONTACT_BUTTON_CONTACTS = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items .sbisru-link')
    CHECK_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text.sbis_ru-link')
    CHECK_LIST_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__item')
    CHOOSER_REGION = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    URL_REGION_NAME = (By.CSS_SELECTOR, 'meta[property="og:url"]')
    CHECK_LIST_PARTNER_KAMCHATKA = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')


    #Метод для последовательного клика по кнопке 'контакты' и перехода на тензор
    def go_to_contact_second_test(self):
        self.click_element_contacts(self.CONTACT_BUTTON, self.CONTACT_BUTTON_CONTACTS)

    #Метод для проверки правильно ли отобразился регион 'Тюменская обл.'
    def find_region(self):
        self.check_region(self.CHECK_REGION)

    #Метод для проверки списка партнеров для своего региона
    def find_list_partners(self):
        self.check_list_partners(self.CHECK_LIST_PARTNERS)

    #Метод для открытия диалоговой панели для выбора региона
    def button_region(self):
        self.region_button_click(self.CHECK_REGION)

    #Метод для выбора региона 'Камчатский край'
    def choose_region(self):
        self.region_chooser(self.CHOOSER_REGION)
        time.sleep(3)

    #Метод для проверки отображения региона в title
    def checking_display_and_title_region_name(self):
        self.checking_title_and_chooser_region(self.CHECK_REGION, 'Камчатский край')

    #Метод для проверки региона в url
    def checking_name_url(self):
        self.checking_ulr_region('kamchatskij kraj')


    def checking_partners_list_name(self):
        self.checking_partners_list_kamchatka(self.CHECK_LIST_PARTNER_KAMCHATKA,'Saby - Камчатка')