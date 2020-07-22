
#Chorme
#from selenium import webdriver
from selenium import webdriver
#browser exposes and executable file 
#Througt selenium test we need to invoke the executable file which will then invoke actual browers 
driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
#driver.maximize_windows()

driver.get("https://www.google.com/")   #get method to hit urlon browser

print(driver.title)
print(driver.current_url)
'''
driver.close()

driver.get("https://www.google.com/")
#driver.minimize_windows()
driver.back()
driver.close()
'''

'''
#Firefox
from selenium import webdriver
#browser exposes and executable file 
#Througt selenium test we need to invoke the executable file which will then invoke actual browers 
driver = webdriver.Firefox(executable_path="C:\\grckodriver.exe")
#driver.maximize_windows()

driver.get("https://rahulshettyacademy.com/")   #get method to hit urlon browser

print(driver.title)
print(driver.current_url)
driver.close()
driver.get("https://rahulshettyacademy.com/Automationpractice/")
#driver.minimize_windows()
driver.back()
diver,refresh()
driver.close()

#IE
from selenium import webdriver
#browser exposes and executable file 
#Througt selenium test we need to invoke the executable file which will then invoke actual browers 
driver = webdriver.Ie(executable_path="C:\\IEdriverservice.exe")
#driver.maximize_windows()

driver.get("https://rahulshettyacademy.com/")   #get method to hit urlon browser

print(driver.title)
print(driver.current_url)
driver.close()
driver.get("https://rahulshettyacademy.com/Automationpractice/")
#driver.minimize_windows()
driver.back()
diver,refresh()
driver.close()
'''