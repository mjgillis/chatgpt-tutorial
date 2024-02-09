import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional, for headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Instantiate undetected Chromedriver
driver = uc.Chrome(options=chrome_options)

# Your script logic
driver.get('https://app.sensortower.com/users/sign_in')
time.sleep(10)  # Adjust as needed

html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())
