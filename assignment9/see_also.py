from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Web_scraping")

# Will put date-format, title and author in a dictionary. Each dictionary will be put into results list
results  = []

pageCount = 1
dupeEntry = False

# Find number of results at cp-pagination-label. Pulled out total, divide by 20, add 1 and that is number of pages

body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

# Get pagination label
# rootClass = "cp-pagination-label"
rootClass = "div-col"
# rootID = "See_also"
element = body.find_element(By.CLASS_NAME, rootClass)
# element = body.find_element(By.ID, rootID)
print ("Element text:", element.text)


# Get the HTML source of the WebElement
element_html = element.get_attribute('innerHTML')

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(element_html, 'html.parser')

# Prettify the HTML
pretty_html = soup.prettify()

# Print the prettified HTML
print("Pretty HTML: \n", pretty_html)

# Close the WebDriver
driver.quit()