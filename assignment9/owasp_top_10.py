from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten/")


body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one

# Need to get to list of 10 security risks. No Id or Class names on UL or LIs.
#  Start with section that has ID and is at root of tree that contains what we want
rootID = "sec-main"
section_element = body.find_element(By.ID, rootID)

results = []

if (section_element):
    # section_children = section_element.find_element(By.XPATH, "./*") 
    top10_ul = section_element.find_element(By.XPATH, "./ul[2]") 
    if top10_ul:

        top_10_lis = top10_ul.find_elements (By.XPATH, "./li")
        if (top_10_lis):

            for item in top_10_lis:
                # Get the href  
                li_link = item.find_element(By.TAG_NAME, "a")
                # print("get attribute: ", li_link.get_attribute("href"))
                # print ("<a> text: ", li_link.text)

                # Put in dictionary then append that to the results list
                sec_dict = {"Title" : li_link.text, "Link" : li_link.get_attribute("href") }
                results.append (sec_dict)

# Close the WebDriver
driver.quit()

# Put results into a data frame
df = pd.DataFrame(results)
fileName = "owasp_top_10.csv"
df.to_csv (fileName)
print ("Results written to:", fileName)

