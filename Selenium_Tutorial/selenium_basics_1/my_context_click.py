'''
Created on 19-Apr-2024

@author: bijnu
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains

'''1. Launch Chrome'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

'''2. Navigate to practice site'''
driver.get("https://demo.guru99.com/test/simple_context_menu.html") 
#driver.get("https://testautomationpractice.blogspot.com") 

'''3. Right Click on (right click me) button'''
right_click_me=driver.find_element(By.XPATH,'//*[@id="authentication"]/span')
my_actions=ActionChains(driver)
my_actions.context_click(right_click_me).perform()