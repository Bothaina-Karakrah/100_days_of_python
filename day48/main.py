from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms")

# Accept cookie consent if present
try:
    cookie_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_btn.click()
except:
    pass

# Wait for the price div using CSS_SELECTOR
try:
    price = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".base-price-text-module--price-part---xQlz.ud-clp-discount-price.ud-heading-xl")
        )
    )
    print("Course price:", price.text)
except:
    print("❌ Could not find the price.")