# Internship Application Automation Script

This project is a Python-based web scraping and automation tool that I built to help my beloved ones automate the process of applying for internships by collecting job listings from specific websites and processing the information for further action.

## Features

- Scrapes internship job listings from websites like Levels.fyi. (IT IS HARDCODED FOR NOW!)

- Extracts relevant information such as job title, company name, location, and job description.
- Saves the scraped data into a CSV file for easy access and further processing.
- Uses **Selenium** to handle dynamic web pages that load content via JavaScript.

## Requirements

To run this script, you need the following:

1. **Python 3.x** installed on your machine.
2. The following Python libraries installed:
   - `selenium`
   - `beautifulsoup4`
   - `requests`
   - `pandas`

   You can install them via pip:

   ```bash
   pip install selenium beautifulsoup4 requests pandas

   
   
## PS: 
   - Consider re-structure your parser if you want to use the script on a different careers website
