import pytest
import requests
from selenium import webdriver


# Фикстура для API-тестов
@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    yield session
    session.close()

# Фикстура для UI-тестов
@pytest.fixture(scope="function")
def browser():
    """Запускает Chrome без указания пути к chromedriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # Автоматически находит chromedriver
    driver.implicitly_wait(10)

    yield driver
    driver.quit()