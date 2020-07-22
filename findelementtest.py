import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.fine_element_by_css_selector("li[class='ui-menu-item']a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").grt_attribute('value') =="India"






driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromcity").clicl()

countries = driver.fine_element_by_css_selector("input[placeholder='from']").send_key("del")
time.sleep(2)
cites = dribver.fine_element_by_css_selector("p[class*=blackText']")
print(len(cities))
for country in cities:
    if city.text == "Del Rio,United States":
        city.click()
        break
driver.find_element_by_xpath("//p[text()='Delhi,India']").click()




