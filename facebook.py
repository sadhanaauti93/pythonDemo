from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("hii")

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("mailid")
password = browser.find_element_by_id("password")
submit   = browser.find_element_by_id("login")
username.send_keys("mailid")
password.send_keys("password")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"
