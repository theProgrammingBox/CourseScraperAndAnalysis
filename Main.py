from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

firefox_profile = os.getenv('firefox_profile')
service = os.getenv('service')
url = os.getenv('url')
username = os.getenv('username')
password = os.getenv('password')
major = os.getenv('major')
college = os.getenv('college')
specialization = os.getenv('specialization')

options = webdriver.FirefoxOptions()
options.profile = FirefoxProfile(firefox_profile)
driver = webdriver.Firefox(service=Service(service), options=options)
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_username"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_password"))).send_keys(password, Keys.ENTER)

time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "what-if"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "major_label_value"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{major}']]"))).click()
WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{major}']]")))

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "college_label_value"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{college}']]"))).click()
WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{college}']]")))

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "specialization_label_value"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{specialization}']]"))).click()
WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{specialization}']]")))

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "WhatIfProcess"))).find_elements(By.TAG_NAME, "button")[1].click()

while True:
    pass