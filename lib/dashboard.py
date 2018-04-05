from lib.core import BaseElement
from selenium.webdriver.support.ui import WebDriverWait

DASHBOARD_SELECTOR = "h1.h2"

title = BaseElement(DASHBOARD_SELECTOR)

TABLE_SELECTOR = ".table.table-sm > tbody > tr"


class Table(BaseElement):
    def wait_to_load(self, driver):
        WebDriverWait(driver, timeout=10).until(self.nth_row(2).is_visible)

    def nth_row(self, n):
        return BaseElement(self.selector + ":nth-of-type({})".format(n))


table = Table(TABLE_SELECTOR)
