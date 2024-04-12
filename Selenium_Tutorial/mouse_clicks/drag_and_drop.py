'''
Created on 11-Apr-2024

View port. Python scrolls down the screen to take us to the point in a webpage where change is being done.
Mouse XY - gives X and Y offsets of an element
'''
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 

source=driver.find_element(By.ID,"draggable")
target=driver.find_element(By.ID,"droppable")
my_actions=ActionChains(driver)

# Drag and drop by source and target
#my_actions.drag_and_drop(source, target).perform()

#Drag and drop by offset
#my_actions.drag_and_drop_by_offset(source,50,50).perform()
my_actions.scroll_by_amount(0,400).perform()
time.sleep(2)
my_actions.drag_and_drop(source, target).perform()
