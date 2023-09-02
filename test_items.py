from selenium.webdriver.common.by import By
import time 
import unittest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_select_language_and_find_button(browser):
    browser.get(link)
    time.sleep(3)
    
    Element = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert Element > 0, 'The desired element is missing'




if __name__ == "__main__":
    pytest.main()

