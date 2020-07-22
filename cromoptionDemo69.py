from selenium import webdriver
from selenium.webdriver.support.select import Select

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--start-maximized")
Chrome_options.add_argument("headless")
Chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe",options=Chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
