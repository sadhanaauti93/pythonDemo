from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_class_name("name").send_keys("Sadhana")
driver.find_elements_by_css_selector("input['name=name']").eend_keys("Sadhana")
driver.find_elements_by_name("email").send_keys("auti")

driver.find_element_by_id("examplecheck1").click()

# select the class provide the metnods to handlethe options in dropdown 
dropdown = select(driver.find_element_by_id("examplefromcontrolSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


driver,fine_element_by_xpath("input[@type='submit']").click()

print(driver.find_elements_by_class_name("alart-success").text)

#//*[contains(@class,'alert-success')]   -xpath
#[class*='alert-success']   -css