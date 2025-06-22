from pages.first_page import FirstTest


def test_open_contacts(driver):
    page = FirstTest(driver)
    page.open()
    page.go_to_contacts()
    page.find_image()
