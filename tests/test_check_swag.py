# в файле test_check_swag.py реализуйте следующий тест кейс:
# i. перейти на страницу https://www.saucedemo.com/
# ii. проверить наличие иконки

from pages.swag_labs import SwagLabs
import time
def test_check_icon(browser):

    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    time.sleep(3)
    assert swag_labs_page.exist_icon(locator='#root > div > div.login_logo') # проверяем наличие иконки
    assert swag_labs_page.exist_field(locator='#user-name') # проверяем наличие поля Имя
    assert swag_labs_page.exist_field(locator='#password')  # проверяем наличие поля Пароль