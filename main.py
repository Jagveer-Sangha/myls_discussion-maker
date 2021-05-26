from selenium import webdriver
import time
# Imports for the try block
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/jagveer/Library/Python/3.8/drivers/chromedriver"

link = "https://mylearningspace.wlu.ca/d2l/home"

driver = webdriver.Chrome(PATH)
driver.get(link)
time.sleep(5)


try:
    # Change either driver or time
    main = WebDriverWait(driver, 10).until(
        # Change by. to match
        EC.presence_of_element_located((By.ID, "userName"))
    )
    main.click()
    main.clear()

    # enter the students username
    main.send_keys('')

    main = WebDriverWait(driver, 10).until(
        # Change by. to match
        EC.presence_of_element_located((By.ID, "password"))
    )
    main.click()
    main.clear()
    # enter the students password
    main.send_keys("www")

    driver.find_element_by_class_name("d2l-button").click()
    time.sleep(3)
except:
    driver.quit()

# To click the navigation and enter a specific classroom
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "d2l-navigation-s-course-menu"))
    )

    main.click()

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@title='CP-213-OC1 - Object-Oriented Programming - 494.202009']"))
    )
    main.click()


except:
    driver.quit()

# Complete actions within the classroom
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@slot='main']"))
    )


except:
    driver.quit()
