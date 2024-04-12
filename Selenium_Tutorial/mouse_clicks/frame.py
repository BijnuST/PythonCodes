'''
Created on 08-Apr-2024


'''
#//*[@id="HTML10"]/div[1]/button
from selenium import webdriver
from selenium.webdriver.common.by import By

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 
new_web=driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-0"]')

driver.switch_to.frame("frame-one796456169")
new_web.send_keys("Bijnu")

driver.switch_to.parent_frame()