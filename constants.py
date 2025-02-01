BASE_URL = "https://altaivita.ru"
CART_URL = f"{BASE_URL}/engine/cart"

# Полные пути к API-эндпоинтам
ADD_TO_CART_URL = f"{CART_URL}/add_products_to_cart_from_preview.php"
REMOVE_FROM_CART_URL = f"{CART_URL}/delete_products_from_cart_preview.php"

BASE_UI_URL = BASE_URL  # Используется для UI-тестов

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/plain, */*"  # Ожидаем JSON-ответ
}