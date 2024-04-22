'''
Created on 19-Apr-2024

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

'''1. Launch Chrome'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

'''2. Navigate to practice site'''
driver.get("https://demo.automationtesting.in/Resizable.html") 
#driver.get("https://testautomationpractice.blogspot.com") 

'''3. Mouse hover over Switch To drop down'''
switch_to_dropdown=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
my_actions=ActionChains(driver)
my_actions.move_to_element(switch_to_dropdown).perform()

