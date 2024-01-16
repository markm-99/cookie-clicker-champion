from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# https://orteil.dashnet.org/cookieclicker/
# cookie has specific attributes that script is looking for to perform clicks
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# find the element with the text 'English' using the XPath expression "//*[contains(text(), 'English')]"
# XPATH gives us a way to locate elements in HTML and navigate through it based on attributes/content
# great for clicking buttons and filling out forms
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

# keep infinitely clicking cookie and print the cookie count to console
while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    # will print the cookie count until the next upgrade, then resets the cookie counter
    print(cookies_count)
        
    # 4 products to iterate over
    for i in range(4):
        # Iterate over the 4 products to get their prices
        # Get text content with ID 'productPrice'
        
        # with enough cookies for price, find product
        # then click on the product button to redeem upgrade  
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        # if product price is not a valid number, continue to next iteration
        # there are commas in the product price numbers, so removed and added check for digit-only values for peace of mind
        # we only consider valid product numbers for upgrades
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        # anytime we have enough cookies to upgrade, automatically upgrade
        # click product button to upgrade
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
