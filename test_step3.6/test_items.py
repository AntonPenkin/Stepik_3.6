import time


link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_search_add_to_cart_button(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_elements_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket'), "Add to cart button not found"