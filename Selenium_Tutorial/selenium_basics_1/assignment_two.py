'''
Created on 07-Apr-2024

'''
from selenium import webdriver
from selenium.webdriver.common.by import By

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 
new_web=driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button')
new_web.click()

win_list=driver.window_handles   
driver.switch_to.window(win_list[1])

open_desktops=driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/a')
open_desktops.click()

open_opt=driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li[2]/a')
open_opt.click()

driver.implicitly_wait(10.0)
driver.switch_to.window(win_list[1])

ckbox=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/label/span[2]')
ckbox.click()   
