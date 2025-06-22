from pages.third_page import ThirdTest

def test_download(driver):
    page = ThirdTest(driver)
    page.open()
    page.click_download_button()
    page.click_download_plugin()
    page.wait_file_exe()
    page.check_file_size()
    page.check_file_size_local()
    page.compering_files()