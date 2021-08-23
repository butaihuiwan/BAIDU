from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.headless = True

driver = webdriver.Chrome(executable_path='D:\guge\chromedriver_win32\chromedriver.exe', options=opt)
driver.get('http://www.baidu.com')
print('百度 ok')
driver.quit()
