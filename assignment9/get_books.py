from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://en.wikipedia.org/wiki/Web_scraping")
driver.get ("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

title = driver.title # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
print(title)

links = []

body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

# Will put date-format, title and author in a dictionary
results  = []

# List Items with classs 
listItems = body.find_elements(By.CSS_SELECTOR, "ul.results li.cp-search-result-item")
count = 0
for item in listItems:
    bookInfo = item.find_element(By.CLASS_NAME, "display-info")

    # Now find the div with format and year
    primaryInfo = bookInfo.find_element(By.CLASS_NAME,"display-info-primary")
    formatYear = primaryInfo.text

    # Find div the author
    authorInfo =  item.find_elements(By.CLASS_NAME,"author-link")
    # Need to check for multiple authors
    authors = ""
    for author in authorInfo:
        if (authors):
            authors = authors + ";" + author.text
        else:
            authors = author.text
 
    # Find title of the book - this is the div. Href is child of this?
    title = item.find_element(By.CLASS_NAME, "cp-title")
    titleText = title.text

    bookDict = {"Format-Year" : formatYear, "Author" : authors, "Title" : titleText }
    results.append (bookDict)

# Put results into a data frame
df = pd.DataFrame(results)
df.sort_values ("Title")
print (df)