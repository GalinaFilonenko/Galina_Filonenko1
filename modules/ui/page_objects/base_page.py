from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"C:\cygwin64\home\User\projects\Galina_Filonenko1"
    DRIVER_NAME = "\chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
