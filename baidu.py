from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.headless = True

driver = webdriver.Chrome(options=opt)
driver.get('http://www.baidu.com')
print('百度 ok')
driver.quit()
