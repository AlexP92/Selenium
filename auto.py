from selenium import webdriver

chrome_br = webdriver.Chrome('./chromedriver.exe')

chrome_br.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

button=chrome_br.find_element_by_class_name('btn-default')

b=button.get_attribute('innerHTML')

m=chrome_br.find_element_by_id('user-message')
m.clear()

m.send_keys('blba bala')
button.click()