from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
#driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
#action = ActionChains(driver)
#menu = driver.find_element_by_id("mousehover")
#action.move_to_element(menu).perform()
#childMenu = driver.find_element_by_link_text("Top")
#action.move_to_element(childMenu).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double click me!!!,You got to be kidding me" == alert.text
alert.accept()




