'''
Created on 07-Apr-2024


'''
'''
from selenium import webdriver

driver = webdriver.Chrome()   # launches Chrome and closes immediately
driver.get("https://google.com") # launches Chrome and loads the URL mentioned.
title = driver.title
print(title)

'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

print(title)
print(text_box)
print(submit_button)
print(message)
print(text)

driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# Launches Chrome browser
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

# Navigating to practice site

driver.get("https://testautomationpractice.blogspot.com") 

# Interacting with web elements
'''
wiki_txt_box=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_txt_box.send_keys("Wikipedia")

wiki_search_btn=driver.find_element(By.CLASS_NAME,"wikipedia-search-button")
wiki_search_btn.click()

https://demo.opencart.com/
'''
print(driver.current_window_handle)

wiki_search_btn=driver.find_element(By.CSS_SELECTOR,"#HTML4 > div.widget-content > button")
wiki_search_btn.click()

# Switch to new window

print(driver.current_window_handle)
win_list=driver.window_handles   # returns how many windows are present
driver.switch_to.window(win_list[1])

# Clicks on Desktops in navigation bar

open_desktops=driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/a')
open_desktops.click()
