import dotenv
from selenium import webdriver
import time
# Imports for the try block
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Imports for .env
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Get the base directory
basepath = Path()
basedir = str(basepath.cwd())
# Load the environment variables
envars = basepath.cwd() / '.env'
load_dotenv(envars)
# Read an environment variable.
KEY = os.getenv('KEY')

# Check
print(f'The client id is: {KEY}.')

# Change path name, env var doesn't work when the name is PATH
PATH = os.getenv('CHROME_PATH')

link = "https://mylearningspace.wlu.ca/d2l/home"
driver = webdriver.Chrome(PATH)
driver.get(link)
time.sleep(5)
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
try:
    # Change either driver or time
    main = WebDriverWait(driver, 10).until(
        # Change by. to match
        EC.presence_of_element_located((By.ID, 'userName'))
    )
    main.click()
    main.clear()

    # Enters the users username
    main.send_keys(USERNAME)

    main = WebDriverWait(driver, 10).until(
        # Change by. to match
        EC.presence_of_element_located((By.ID, 'password'))
    )
    main.click()
    main.clear()
    # Enters the users password
    main.send_keys(PASSWORD)

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
            (By.XPATH, "//*[@title='CP-386-C - Operating Systems - 853.202105']"))
    )
    main.click()


except:
    driver.quit()

# Complete actions within the classroom
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, 'Discussions'))
    )
    main.click()
except:
    driver.quit()
