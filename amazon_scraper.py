import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 15)

# Open Amazon search page
search_url = "https://www.amazon.in/s?k=laptop"
driver.get(search_url)

products = []

try:
    product_cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-component-type='s-search-result']")
        )
    )

    for product in product_cards[:20]:  # limit for safety
        try:
            title = product.find_element(By.XPATH, ".//span[@class='a-size-medium']").text
        except:
            title = "N/A"

        try:
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "N/A"

        try:
            rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        except:
            rating = "N/A"

        products.append({
            "Product Name": title,
            "Price": price,
            "Rating": rating
        })

finally:
    driver.quit()

# Save to Excel
df = pd.DataFrame(products)
df.to_excel("amazon_products.xlsx", index=False)

print("Scraping completed. Data saved to amazon_products.xlsx")
