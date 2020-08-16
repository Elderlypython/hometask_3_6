import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        return True
    except:
        return False

def test_button_presence(browser):
    browser.get(link)
    #time.sleep(30) #при смене языка на франц. -- раскомментить^^
    assert is_element_present(browser), "Искомая кнопка отсутствует"