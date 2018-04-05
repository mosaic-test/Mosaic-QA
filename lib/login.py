from .core import BaseElement


DUMMY_USER = "username"
DUMMY_PW = "password"


LOGIN_SELECTOR_BASE = '[action="dashboard.html"] > input[type={}]'
USERNAME_SELECTOR = LOGIN_SELECTOR_BASE.format("text")
PASSWORD_SELECTOR = LOGIN_SELECTOR_BASE.format("password")
SUBMIT_SELECTOR = LOGIN_SELECTOR_BASE.format("submit")

LOGOUT_SELECTOR = "ul a.nav-link"


username_field = BaseElement(USERNAME_SELECTOR)
password_field = BaseElement(PASSWORD_SELECTOR)
submit_btn = BaseElement(SUBMIT_SELECTOR)
sign_out_btn = BaseElement(LOGOUT_SELECTOR)


def log_in(driver):
    username_field.enter_text(driver, DUMMY_USER)
    password_field.enter_text(driver, DUMMY_USER)
    submit_btn.click(driver)


def log_out(driver):
    sign_out_btn.click(driver)
