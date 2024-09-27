from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome()

driver.get("https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin")

user_id_input = driver.find_element(By.XPATH, "//input[@name='sid']")
user_id_input.send_keys(str(username))

user_passwd_input = driver.find_element(By.XPATH, "//input[@name='PIN']")
user_passwd_input.send_keys(str(password))

user_button_input = driver.find_element(By.XPATH, "//input[@type='submit']")
user_button_input.click()

input("Please press enter to close the browser...")

driver.quit()
