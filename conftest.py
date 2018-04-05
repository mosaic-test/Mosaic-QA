from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

HOME_PAGE = "http://mosaic-test-app.s3-website.eu-west-2.amazonaws.com/"
@pytest.yield_fixture
def driver():
    opts = Options()
    opts.add_argument('app={}'.format(HOME_PAGE))
    opts.add_argument('disable-infobars')
    _driver = webdriver.Chrome('chromedriver', chrome_options=opts)
    yield _driver
    _driver.quit()