# selenium = automation tool to control google chrome (automated tests)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://google.com/"
driver = webdriver.Chrome()
driver.get(url)
# after 5 sec, if program DNE, crash program
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
# specify class_name of input field you want to access
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# won't override, will append data
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
# click and re-direct to another page
# if tech with tim exists in link or anchor tag, click youtube channel
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# keep active for 10 seconds
time.sleep(10)
driver.quit