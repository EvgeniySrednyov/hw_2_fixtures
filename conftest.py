import pytest
from selene import browser


@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 1080  # задаем высоту окна браузера
    browser.config.window_width = 1920  # задаем ширину окна браузера
    yield
    browser.quit()  # закрываем браузер
