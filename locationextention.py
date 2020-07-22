from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_elements_by_css_selector("#username").send_key("sadhana")
driver.find_elements_by_css_selector(".password").send_key("Auti")
driver.find_elements_by_css_selector(".password").clear()
driver.find_elements_by_link_text("Forgot Your password?").click()
#//tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='cancel']").clicl()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_elements_by_css_selector("from[name='login'] lable:nth-child(3)").text)

