from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print('百度 ok')
