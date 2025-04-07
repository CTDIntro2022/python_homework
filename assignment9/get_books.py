from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://en.wikipedia.org/wiki/Web_scraping")
baseURL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart&page="

# Will put date-format, title and author in a dictionary. Each dictionary will be put into results list
results  = []

pageCount = 1
dupeEntry = False

# Will keep moving throuh pages by incrementin page cont.  IF you browswe to site with page count > what is availabhle then
# the last page will be shown. We will know that by checking to see if the first item found on that page has alread been inserted
# in the results list. dupeEntry will be set to true which will exit the while loop.
# Alernatively could have found number of results at cp-pagination-label. Pulled out total, divide by 19 and that is number of pages

# This is alternate code
# body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one                                            
# pageText = body.find_element(By.CLASS_NAME, "cp-screen-reader-shortcuts")
# print (pageText)

while (not dupeEntry):
    # driver.get ("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    url = baseURL + str(pageCount)
    driver.get (url)

    print ("URL: ", driver.current_url)
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

        bookDict = {"Format-Year" : formatYear, "Author" : authors, "Title" : titleText }
        if bookDict in results:
            print ("Dupe entry: ", bookDict)
            dupeEntry = True
            break
        else:    
            results.append (bookDict)
    pageCount += 1
    
driver.quit()
    
# Put results into a data frame
df = pd.DataFrame(results)
df.sort_values ("Title")
print (df)

csvFile = "get_books.csv"
df.to_csv (csvFile)
print ("DF written to ", csvFile)