from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import sys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten/")

body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

# Need to get to list of 10 security risks. No Id or Class names on UL or LIs.
#  Start with section that has ID and is at root of tree that contains what we want
rootID = "sec-main"
section_element = body.find_element(By.ID, rootID)

# Store results as dictionary items in this list
results = []

if (section_element):
    try:
        top_10_list = section_element.find_elements(By.XPATH, "./ul[2]/li") 

        if top_10_list:
            # Let's make sure we got 10
            if len(top_10_list) != 10:
                print (f'Warning: Top ten list has {len(top_10_list)} items in it!)')
            for item in top_10_list:
                # Get the href  
                li_link = item.find_element(By.TAG_NAME, "a")
                # print("get attribute: ", li_link.get_attribute("href"))
                # print ("<a> text: ", li_link.text)
                # Put in dictionary then append that to the results list
                sec_dict = {"Title" : li_link.text, "Link" : li_link.get_attribute("href") }
                results.append (sec_dict)
        else:
            print ("Did not find top 10 list.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        sys.exit(1)

# Close the WebDriver
driver.quit()

# Put results into a data frame
df = pd.DataFrame(results)
fileName = "owasp_top_10.csv"
df.to_csv (fileName)
print ("Results written to:", fileName)

