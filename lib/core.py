from selenium.common.exceptions import NoSuchElementException


class BaseElement:
    def __init__(self, selector):
        self.selector = selector

    def element(self, driver):
        return driver.find_element_by_css_selector(self.selector)

    def click(self, driver):
        self.element(driver).click()

    def enter_text(self, driver, text):
        self.element(driver).send_keys(text)

    def get_text(self, driver):
        return self.element(driver).text

    def is_visible(self, driver):
        try:
            return self.element(driver).is_displayed()
        except NoSuchElementException:
            return False
