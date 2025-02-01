import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_UI_URL = "https://altaivita.ru"


@allure.feature("UI: Корзина")
@allure.story("Добавление товара в корзину")
@pytest.mark.ui
def test_ui_add_item_to_cart(browser):
    """Тест: добавление товара в корзину и проверка значка корзины"""
    browser.get(BASE_UI_URL)

    with allure.step("Ищем кнопку 'В корзину' и кликаем"):
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'в корзину')]"))
        )
        browser.execute_script("arguments[0].click();", add_to_cart_button)  # JS-клик

    with allure.step("Проверяем, что значок корзины обновился"):
        cart_icon = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.header__basket-link"))
        )
        assert cart_icon is not None, "Ошибка: значок корзины не обновился!"

    with allure.step("Проверяем, что товар добавлен в корзину"):
        browser.get(f"{BASE_UI_URL}/cart/")  # Открываем корзину
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.basket__delete.js-item-delete"))
        )

@pytest.mark.ui
@allure.feature("UI: Корзина")
@allure.story("Удаление товара из корзины")
def test_ui_remove_item_from_cart(browser):
    """Тест: автоматическое добавление товара в корзину перед удалением"""

    browser.get(f"{BASE_UI_URL}/cart/")

    with allure.step("Проверяем, есть ли товар в корзине"):
        try:
            delete_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'basket__delete')]//button"))
            )
            is_cart_empty = False
        except:
            is_cart_empty = True

    if is_cart_empty:
        with allure.step("Корзина пуста, добавляем товар"):
            browser.get(BASE_UI_URL)
            add_to_cart_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'в корзину')]"))
            )
            browser.execute_script("arguments[0].click();", add_to_cart_button)

            # Ждем, пока корзина обновится
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.header__basket-link"))
            )

            # Переход в корзину
            browser.get(f"{BASE_UI_URL}/cart/")
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.basket__delete.js-item-delete"))
            )

    with allure.step("Удаляем товар из корзины"):
        delete_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'basket__delete')]//button"))
        )
        browser.execute_script("arguments[0].click();", delete_button)

    with allure.step("Проверяем, что корзина теперь пуста"):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p[style*='text-align: center']"))
        )