from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RozetkaPage(BasePage):
    URL = "https://rozetka.com.ua/apple-mphe3ua-a/p364911351/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self, page_url):
        if page_url == None:
            self.driver.get(RozetkaPage.URL)
        else:
            self.driver.get(page_url)

    def add_curent_item_to_cart(self):
        # Знаходимо кнопку buy
        btn_elem = self.driver.find_element(By.CLASS_NAME, "buy-button")
        # Емулюємо клік лівою кнопкою миші
        btn_elem.click()

    def pop_up_close(self):
        # Знаходимо хрестик
        btn_elem = self.driver.find_element(By.CLASS_NAME, "modal__close")
        # Емулюємо клік лівою кнопкою миші
        btn_elem.click()

    def get_cart_badge_text(self):
        cart_badge = self.driver.find_element(By.CLASS_NAME, "badge")

        return cart_badge.text

    def open_cart(self):
        # Знаходимо корзину
        btn_elem = self.driver.find_element(
            By.XPATH,
            "//button[@rzopencart][@class='header__button ng-star-inserted header__button--active']",
        )
        # Емулюємо клік лівою кнопкою миші
        btn_elem.click()

    def open_cart_menu(self):
        # Знаходимо кнопку три точки
        btn_elem = self.driver.find_element(By.ID, "cartProductActions0")
        # Емулюємо клік лівою кнопкою миші
        btn_elem.click()

    def delete_item_from_cart(self):
        # Знаходимо кнопку Видалити
        btn_elem = self.driver.find_element(
            By.XPATH, "//div[@id='cartProductActions0']/ul/li/rz-trash-icon/button"
        )
        # Емулюємо клік лівою кнопкою миші
        btn_elem.click()

    def find_empty_cart(self):
        # Знайти пусту корзину
        empty_cart_elem = self.driver.find_element(
            By.XPATH, "//div[@data-testid='empty-cart']"
        )
        return empty_cart_elem

    def search_text(self, text):
        # Знайти пошук
        search_elem = self.driver.find_element(By.NAME, "search")
        # Вводимо пошуковий текст
        search_elem.send_keys(text)
        search_elem.send_keys(Keys.ENTER)

    def find_catalogue_products(self):
        products = self.driver.find_elements(By.CLASS_NAME, "catalog-grid__cell")
        return products

    def find_empty_catalogue(self):
        catalogue = self.driver.find_element(By.CLASS_NAME, "catalog-empty")
        return catalogue
