'''
Created on 12-Apr-2024

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)   

driver.get("https://testautomationpractice.blogspot.com") 

mouse_value=driver.find_element(By.XPATH,'//*[@id="name"]')
mouse_value.send_keys("Bijnu S Thomas")
time.sleep(1)

mouse_value=driver.find_element(By.XPATH,'//*[@id="email"]')
mouse_value.send_keys("bijnu@gmail.com")
time.sleep(1)

mouse_value=driver.find_element(By.XPATH,'//*[@id="phone"]')
mouse_value.send_keys("9876543210")
time.sleep(1)

mouse_value=driver.find_element(By.XPATH,'//*[@id="textarea"]')
mouse_value.send_keys("House no .1, Mysore, Karnataka")
time.sleep(1)

mouse_value=driver.find_element(By.XPATH,'//*[@id="female"]')
mouse_value.click()
time.sleep(1)

mouse_value=driver.find_element(By.XPATH,'//*[@id="sunday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="monday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="tuesday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="wednesday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="thursday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="friday"]')
mouse_value.click()
time.sleep(1)
mouse_value=driver.find_element(By.XPATH,'//*[@id="saturday"]')
mouse_value.click()
time.sleep(1)


#element = driver.find_element(By.ID,"country")
#actions = ActionChains(driver)
#actions.move_to_element(element).perform()

drop_down=driver.find_element(By.XPATH,'//*[@id="country"]')
drop_down.click()
time.sleep(1)
drop_down=driver.find_element(By.XPATH, '//*[@id="country"]/option[10]')
drop_down.click()

select_colour=driver.find_element(By.XPATH,'//*[@id="colors"]/option[2]')
select_colour.click()
time.sleep(1)

select_date=driver.find_element(By.XPATH, '//*[@id="datepicker"]')
select_date.click()
time.sleep(1)
select_date=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]')
select_date.click()
time.sleep(1)
select_date=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]/a')
select_date.click()
time.sleep(1)



