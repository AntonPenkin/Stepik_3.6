import time


link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_find_the_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket.bnb')
    assert button, "No such item"