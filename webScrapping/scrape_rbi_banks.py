from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening browser
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# RBI Website URL - List of Banks
url = "https://www.rbi.org.in/Scripts/AboutUsDisplay.aspx?pg=BankingInstitutions"
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Extract bank categories (Public, Private, Foreign, etc.)
categories = driver.find_elements(By.XPATH, '//div[@id="content"]/ul/li')

# Store bank data
bank_data = []
for category in categories:
    bank_type = category.find_element(By.TAG_NAME, 'strong').text.strip()
    banks = category.find_elements(By.TAG_NAME, 'a')
    
    for bank in banks:
        bank_name = bank.text.strip()
        bank_data.append({
            "Bank Name": bank_name,
            "Type": bank_type
        })

# Convert to DataFrame
df = pd.DataFrame(bank_data)
print(bank_data)  # Add this line before saving the CSV
df.to_csv("banks_in_india.csv", index=False)
print("Data saved to banks_in_india.csv")


# Close driver
driver.quit()