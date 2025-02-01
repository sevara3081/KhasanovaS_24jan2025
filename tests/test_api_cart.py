import requests
import pytest
import allure
import json
from constants import ADD_TO_CART_URL, REMOVE_FROM_CART_URL, HEADERS


@allure.feature("API: Корзина")
@allure.story("Добавление товара в корзину")
def test_add_product_to_cart():
    """Проверяем, что товар успешно добавляется в корзину"""
    payload = {
        "product_id": "727",
        "LANG_key": "ru",
        "S_wh": "1",
        "S_CID": "12c8e19b7187888c11f84c5b8388a864",
        "S_cur_code": "usd",
        "S_koef": "0.01262",
        "quantity": "1"
    }

    response = requests.post(ADD_TO_CART_URL, data=payload, headers=HEADERS)

    assert response.status_code == 200, f"Ошибка: неверный статус-код {response.status_code}"

    try:
        json_data = response.json()
    except json.JSONDecodeError:
        print("Ошибка: сервер вернул некорректный JSON!")
        print("Ответ сервера:", response.text[:500])
        pytest.fail("Ошибка: не удалось декодировать JSON!")

    assert json_data.get("status") == "ok", f"Ошибка: неверный статус ответа {json_data}"


@allure.feature("API: Корзина")
@allure.story("Удаление товара из корзины")
def test_remove_product_from_cart():
    """Проверяем, что товар успешно удаляется из корзины"""
    payload = {
        "product_id": "727",
        "LANG_key": "ru",
        "S_wh": "1",
        "S_CID": "12c8e19b7187888c11f84c5b8388a864",
        "S_cur_code": "usd",
        "S_koef": "0.01262"
    }

    response = requests.post(REMOVE_FROM_CART_URL, data=payload, headers=HEADERS)

    assert response.status_code == 200, f"Ошибка: неверный статус-код {response.status_code}"

    try:
        json_data = response.json()
    except json.JSONDecodeError:
        print("Ошибка: сервер вернул некорректный JSON!")
        print("🔍 Ответ сервера:", response.text[:500])
        pytest.fail("Ошибка: не удалось декодировать JSON!")

    assert json_data.get("status") == "ok", f"Ошибка: неверный статус ответа {json_data}"