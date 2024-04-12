'''
Created on 11-Apr-2024

@author: bijnu
'''

from selenium.webdriver.common.action_chains import ActionChains
ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 

copy_text_button=driver.find_element(By.CSS_SELECTOR,"#HTML10 > div.widget-content > button")
my_actions=ActionChains(driver)
my_actions.double_click(copy_text_button)
my_actions.perform()
