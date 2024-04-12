'''
Created on 07-Apr-2024

In the form, click on Alert, Confirm Box and Prompt.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 
print("-----Clicking on Alert-----")
js_alert=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[1]')
js_alert.click()

al=driver.switch_to.alert
time.sleep(2)
al.accept()
#print("Clicked on OK")

print("-----Clicking on Confirm Box-----")

js_confirm=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[2]')
js_confirm.click()
conf=driver.switch_to.alert
time.sleep(2)
conf.accept()
print("Pressed on OK in Confirm Box")
js_confirm=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[2]')
js_confirm.click()
conf=driver.switch_to.alert
time.sleep(2)       #hard wait
conf.dismiss()
print("Pressed on Cancel in Confirm Box")

print("-----Clicking on Prompt-----")
js_prompt=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[3]')
js_prompt.click()
pr=driver.switch_to.alert
time.sleep(2)
pr.send_keys("Bijnu")
pr.accept()
print("Pressed on Ok in Prompt Box")

time.sleep(5)

js_prompt=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[3]')
js_prompt.click()
pr=driver.switch_to.alert
pr.dismiss()
print("Pressed on Cancel in Prompt Box")