import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.naukri.com/top-jobs-by-designations# desigtop600"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome()
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id': 'nameSearch'})
job_profiles = all_divs.find_all('a')

for job_profile in job_profiles:
	print(job_profile.text)

# driver.close() # closing the webdriver
