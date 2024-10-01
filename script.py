from selenium import webdriver
from bs4 import BeautifulSoup 

import pandas as pd 


driver = webdriver.Chrome(executable_path = "C:\Users\DELL\Downloads\chrome-win64\chrome-win64")

JobMarketUrl = "https://www.levels.fyi/jobs/level/internship?jobFamilySlugs=software-engineer%2Cdata-scientist"
driver.get(JobMarketUrl)


soup = BeautifulSoup(driver.page_source, 'html.parser')


jobItemsParent = soup.find_all('div', class_ = 'company-jobs-preview-card_container__T3XI1')
jobItems = []

# Parent className =  company-jobs-preview-card_container__T3XI1
for child in jobItemsParent.find_all(recursive = False):
    jobItems.append(child) 


