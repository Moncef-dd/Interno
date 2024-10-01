from selenium import webdriver
from bs4 import BeautifulSoup 

import pandas as pd 





driver = webdriver.Chrome(executable_path="C:/Users/DELL/Downloads/chrome-win64/chrome.exe")

JobMarketUrl = "https://www.levels.fyi/jobs/location/canada/level/internship?jobFamilySlugs=software-engineer%2Cdata-scientist"
driver.get(JobMarketUrl)


soup = BeautifulSoup(driver.page_source, 'html.parser')


jobItemsParent = soup.find_all('div', class_ = 'company-jobs-preview-card_container__T3XI1')
jobItems = []

try: 
# Parent className =  company-jobs-preview-card_container__T3XI1
# Company h2 className : company-jobs-preview-card_companyName__cQKav
# Position Title className : company-jobs-preview-card_companyJobTitle__HhXIR
 for child in jobItemsParent.find_all(recursive = False):
    companyName = child.find('h2', class_='company-jobs-preview-card_companyName__cQKav').text.strip()
    positionTitle = child.find_all('div', class_='company-jobs-preview-card_companyJobTitle__HhXIR').text.strip()
    applicationLinks = child.find_all('a').text.strip()

except: 
  print("an error has occured while ")

