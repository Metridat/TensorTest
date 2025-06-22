from pages.second_page import SecondTest

def test_open_contacts(driver):
    page = SecondTest(driver)
    page.open()
    page.go_to_contact_second_test()
    page.find_region()
    page.find_list_partners()
    page.button_region()
    page.choose_region()
    page.checking_display_and_title_region_name()
    page.checking_name_url()
    page.checking_partners_list_name()