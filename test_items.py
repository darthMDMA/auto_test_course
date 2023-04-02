from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_trash_can_button(browser):
    try:
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        assert button

    finally:
        time.sleep(5)
        print("\nquit browser..")
        browser.quit()