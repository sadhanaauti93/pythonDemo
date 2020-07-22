from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver,find_element_by_css_selector("#name").send_key(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
assert validateText in alertText
alert.accept()