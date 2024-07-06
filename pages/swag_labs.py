from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
class SwagLabs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = None

    def exist_icon(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def exist_field(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True