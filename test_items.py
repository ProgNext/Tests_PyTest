import time
from selenium.webdriver.common.by import By


def test_check_exists_button_add_in_card(browser, request):
    link = 'http://selenium1py.pythonanywhere.com/' + request.config.getoption("language") + '/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button.get_attribute('type') == 'submit', "Error, button 'Add in card' is not exists!!!"