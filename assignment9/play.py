from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Web_scraping")  # this much you've seen before

see_also_h2 = driver.find_element(By.CSS_SELECTOR,'[id="See_also"]') # our starting point
if (see_also_h2):
    parent_div = see_also_h2.find_element(By.XPATH, '..') # up to the parent div
    if parent_div:
        see_also_div = parent_div.find_element(By.XPATH,'following-sibling::div' ) # over to the div with all the links
        links = see_also_div.find_elements(By.CSS_SELECTOR, 'a')
        for link in links:
            print(f"{link.text}: {link.get_attribute('href')}")

if body:
    links = body.find_elements(By.CSS_SELECTOR,'a') # Find all the links in the body.
    if len(links) > 0:
        print("href: ", links[0].get_attribute('href'))  # getting the value of an attribute

# Save extracted data to a file
fileName = "get_books.csv"
with open(fileName, 'w', newline='') as file:
    for elem in links:
        href = elem.get_attribute("href")
        if (href != None):
            file.write(elem.get_attribute("href"))
        else: 
            file.write ("None")
print ("Links written to:", fileName)
 