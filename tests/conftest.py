import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def driver():
    # 1. Путь до папки downloads внутри проекта
    download_dir = os.path.join(os.getcwd(), "downloads")

    # 2. Опции Chrome
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,  # скачивание в нашу папку
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 3. Создаем драйвер с этими опциями
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

