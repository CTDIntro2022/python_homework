from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import re
from time import sleep
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://en.wikipedia.org/wiki/Web_scraping")
baseURL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart&page="

# Will put date-format, title and author in a dictionary. Each dictionary will be put into results list
results  = []

pageCount = 1
dupeEntry = False

# Find number of results at cp-pagination-label. Pulled out total, divide by 20, add 1 and that is number of pages
driver.get (baseURL)
body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

# Get pagination label
pageLabel = body.find_element(By.CLASS_NAME, "cp-pagination-label")

# Format is 1 to 20 of 256 results
resultPages = re.findall(r'\b\d+\b', pageLabel.text)
result = resultPages[2]
nbrOfPages = int(int(result)/20) + 1

while (pageCount <= nbrOfPages):
    # driver.get ("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    url = baseURL + str(pageCount)
    driver.get (url)

    sleep(2) # wait 2 seconds
    body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

    # List Items with classs 
    listItems = body.find_elements(By.CSS_SELECTOR, "ul.results li.cp-search-result-item")
    for item in listItems:
        bookInfo = item.find_element(By.CLASS_NAME, "display-info")

        # Now find the div with format and year
        # primaryInfo = bookInfo.find_element(By.CLASS_NAME,"display-info-primary")
        # formatYear = primaryInfo.text
        formatYear = bookInfo.find_element(By.CLASS_NAME,"display-info-primary").text

        # Find title of the book - this is the div. Href is child of this?
        titleText = item.find_element(By.CLASS_NAME, "title-content").text

        # Find div the author
        # If not authors then authors will be blank
        authorInfo =  item.find_elements(By.CLASS_NAME,"author-link")
        # Need to check for multiple authors. Seperate by semil colon
        authors = ""
        for author in authorInfo:
            if (authors):
                authors = authors + ";" + author.text
            else:
                authors = author.text

        bookDict = {"Format-Year" : formatYear, "Author" : authors, "Title" : titleText, "Page" : pageCount }
        # Every once in a while get a dupe in the search results
        if bookDict in results:
            print ("Dupe entry: ", bookDict, pageCount)
            dupeEntry = True
            break
        else:    
            results.append (bookDict)
    pageCount += 1
    
driver.quit()
    
# Put results into a data frame
df = pd.DataFrame(results)
print (df)

csvFile = "get_books.csv"
df.to_csv (csvFile)
print ("DF written to ", csvFile)

jsonFile = "get_books.json"
df.to_json (jsonFile, indent=4, orient='records')
print ("DF written to:", jsonFile)