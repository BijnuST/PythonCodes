'''
Interactions--Drag and Drop -- Statis , Dynamic
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

'''1. Launch Chrome'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

'''2. Navigate to practice site'''
driver.get("https://demo.automationtesting.in/Resizable.html") 
#driver.get("https://testautomationpractice.blogspot.com") 

'''3. Mouse hover over Switch To drop down - click on Interactions--Drag and Drop -- Static'''
# Finding Interactions
switch_to_dropdown=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[6]/a')
my_actions=ActionChains(driver)
my_actions.move_to_element(switch_to_dropdown).perform()
time.sleep(2)
# Finding Interactions -- Drag and Drop
drag_and_drop=driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
my_actions.move_to_element(drag_and_drop).perform()
time.sleep(2)
# Finding Interactions -- Drag and Drop -- Static
static=driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a')
time.sleep(2)
static.click()

'''4. Mouse hover over Switch To drop down - click on Interactions--Drag and Drop -- Dynamic'''
# Finding Interactions
switch_to_dropdown=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[6]/a')
my_actions=ActionChains(driver)
my_actions.move_to_element(switch_to_dropdown).perform()
time.sleep(2)
# Finding Interactions -- Drag and Drop
drag_and_drop=driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
my_actions.move_to_element(drag_and_drop).perform()
time.sleep(2)
# Finding Interactions -- Drag and Drop -- Dynamic
dynamic=driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[2]/a')
time.sleep(2)
dynamic.click()
