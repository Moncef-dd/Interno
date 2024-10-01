from selenium import webdriver
from bs4 import BeautifulSoup 

import pandas as pd 


driver = webdriver.Chrome(executable_path = "C:\Users\DELL\Downloads\chrome-win64\chrome-win64")

JobMarketUrl = "https://www.levels.fyi/jobs/level/internship?jobFamilySlugs=software-engineer%2Cdata-scientist"
driver.get(JobMarketUrl)


soup = BeautifulSoup(driver.page_source, 'html.parser')


 