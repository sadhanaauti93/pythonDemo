from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_element_by_xpath("//input[@type='checkbox']")
#print(type(checkboxes))
#print(len(checkboxes))
checkboxes.click()
'''
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()

    '''    

radiobuttons = driver.find_element_by_class_name("radiobutton")    
radiobuttons[2].click()
assert radiobuttons[2].is_selected()    

assert 2==2        
assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed()

