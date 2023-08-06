from modules.ui.page_objects.rozetka import RozetkaPage
import pytest
import time


@pytest.mark.selenium
def test_check_rozetka_add_item_to_cart():
    rozetkaPage = RozetkaPage()
    rozetkaPage.go_to(None)

    rozetkaPage.add_curent_item_to_cart()

    time.sleep(1)

    rozetkaPage.pop_up_close()

    time.sleep(1)

    cart_badge = rozetkaPage.get_cart_badge_text()
    assert cart_badge == "1"

    # Закриваємо браузер
    rozetkaPage.close()


@pytest.mark.selenium
def test_check_rozetka_remove_item_to_cart():
    rozetkaPage = RozetkaPage()
    rozetkaPage.go_to(None)

    rozetkaPage.add_curent_item_to_cart()

    time.sleep(1)

    rozetkaPage.pop_up_close()

    cart_badge = rozetkaPage.get_cart_badge_text()
    assert cart_badge == "1"

    # Відкрити корзину
    rozetkaPage.open_cart()

    # Відкрити меню корзини
    rozetkaPage.open_cart_menu()

    time.sleep(1)

    # Видалення товару із корзини
    rozetkaPage.delete_item_from_cart()

    time.sleep(1)

    # Знайти пусту корзину
    rozetkaPage.find_empty_cart()

    # Закриваємо браузер
    rozetkaPage.close()


@pytest.mark.selenium
def test_check_rozetka_search():
    rozetkaPage = RozetkaPage()
    rozetkaPage.go_to("https://rozetka.com.ua/")
    rozetkaPage.search_text("iphone")
    time.sleep(1)
    products = rozetkaPage.find_catalogue_products()
    assert len(products) > 0
    time.sleep(1)
    rozetkaPage.close()


@pytest.mark.selenium
def test_check_rozetka_search_bad():
    rozetkaPage = RozetkaPage()
    rozetkaPage.go_to("https://rozetka.com.ua/")
    rozetkaPage.search_text("iphoneasdfasdfasdfasdfasdfasdfasdf")
    time.sleep(1)
    catalogue = rozetkaPage.find_empty_catalogue()
    assert catalogue != None
    time.sleep(1)
    rozetkaPage.close()
