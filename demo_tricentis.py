from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver= webdriver.Chrome()
driver.get("https://www.velo.com/gb/en")
driver.maximize_window()
sleep(2)

# REGISTOR PAGE
# driver.find_element(By.LINK_TEXT,'Register').click()
# sleep(2)
# driver.find_element(By.ID,'gender-male').click()
# sleep(2)
# driver.find_element(By.ID,'FirstName').send_keys("Venkatesh")
# sleep(2)
# driver.find_element(By.ID,'LastName').send_keys('j')
# sleep(2)
# driver.find_element(By.ID,'Email').send_keys('venkychowdary08@gmail.com')
# sleep(2)
# driver.find_element(By.ID,'Password').send_keys('venkat@123')
# sleep(2)
# driver.find_element(By.ID,'ConfirmPassword').send_keys('venkat@123')
# sleep(2)
# driver.find_element(By.ID,'register-button').click()
# sleep(2)

#LOGIN PAGE
# driver.find_element(By.LINK_TEXT,'Log in').click()
# sleep(2)
# driver.find_element(By.ID,'Email').send_keys('venkychowdary08@gmail.com')
# sleep(2)
# driver.find_element(By.ID,'Password').send_keys('venkat@123')
# sleep(2)
# driver.find_element(By.ID,'RememberMe').click()
# sleep(2)
# driver.find_element(By.XPATH,"//input[@class='button-1 login-button']").click()
# sleep(2)
#
# #CONFIRMATION MESSAGE OF LOGIN
# success_element = driver.find_element(By.LINK_TEXT,'venkychowdary08@gmail.com')
#
# if success_element.is_displayed():
#     print("Login successful!")
# else:
#     print("Login failed.")
#
driver.find_element(By.XPATH,"(//a[contains(text(),'Books')][1])").click()
sleep(5)
driver.find_element(By.XPATH,"//a[text()='Computing and Internet']").click()
sleep(5)
driver.find_element(By.ID,"add-to-cart-button-13").click()
sleep(5)

driver.find_element(By.XPATH,"//span[text()='Shopping cart']").click()
sleep(5)
# driver.find_element(By.XPATH,"//input[@value='Go to cart']").click()
# sleep(2)
