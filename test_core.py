from lib.login import log_in, log_out, username_field
from lib.dashboard import title, table


def test_basic(driver):
    log_in(driver)
    assert title.is_visible(driver)
    log_out(driver)
    assert username_field.is_visible(driver)

AUD = "AUD"
BGN = "BGN"
BRL = "BRL"
CAD = "CAD"
CHF = "CHF"
CNY = "CNY"
CZK = "CZK"
DKK = "DKK"
EUR = "EUR"
HKD = "HKD"
CURRENCIES = AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, HKD




def test_dashboard(driver):
    log_in(driver)
    assert title.is_visible(driver)
    table.wait_to_load(driver)
    for i, currency in enumerate(CURRENCIES):
        row = i + 1
        assert currency in table.nth_row(row).get_text(driver), "Currency {} not found in row {}".format(currency, row)