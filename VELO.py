from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.get("https://www.velo.com/gb/en")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//a[@id='over-18']").click()
sleep(5)
driver.find_element(By.XPATH,"//button[@id='onetrust-accept-btn-handler']").click()
sleep(5)
driver.find_element(By.XPATH,"//a[text()='SHOP NOW']").click()
sleep(5)