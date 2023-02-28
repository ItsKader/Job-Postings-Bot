from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime



#Block of code to go to job search website (Download the Google Chrome Driver and change the path to the one in your computer)
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=&locationstring=&sort=M')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="filterList2"]/h3')))


#Date posted: Choose an index of the date_posted_options list as date_posted_option
date_posted_toggle = driver.find_element_by_xpath('//*[@id="filterList2"]/h3').click()
time.sleep(2)
date_posted_options = ['blank','Last 48 hours', 'Last 30 days', "More than 30 days"]
date_posted_option = '2'
date_posted = driver.find_element_by_xpath('//*[@id="dateposted-type"]/div[' + date_posted_option + ']/label').click()
time.sleep(2)

#Type of job: Write the indexes of the desired options of the type_job_options in the type_job_options_indexes list. Leave blank if not a desired option.
type_job_toggle = driver.find_element_by_xpath('//*[@id="filterList3"]/h3').click()
time.sleep(2)
type_job_options = ['blank', 'non_student', 'student', 'non_apprentice', 'apprentice', 'internship', 'green']
type_job_options_indexes = ['1', '', '', '', '', '6']
for i in range (6):
    if type_job_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="job-types"]/ul/li[' + type_job_options_indexes[i] + ']/div/div/label').click()
        time.sleep(3)

#Hours: Write the indexes of the desired options of the hours_options list in the hours_options_indexes list. Leave blank if not a desired option. 
hours_toggle = driver.find_element_by_xpath('//*[@id="filterList4"]/h3').click()
time.sleep(3)
hours_options = ['blank', 'full-time', 'part-time']
hours_options_indexes = ['1', '']
for i in range (2):
    if hours_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="hours-type"]/div[' + hours_options_indexes[i] + ']/label').click()
        time.sleep(3)

#Language: Choose an index of the language_options list as language_option
language_toggle = driver.find_element_by_xpath('//*[@id="filterList5"]/h3').click()
time.sleep(2)
language_options = ['blank', 'english', 'french', 'english and french']
language_option = '1'
language = driver.find_element_by_xpath('//*[@id="language-type"]/div[' + language_option + ']/label').click()
time.sleep(2)

#Salary: Write the indexes of the desired options of the salary_options list in the salary_options_indexes list. Leave blank if not a desired option.
salary_toggle = driver.find_element_by_xpath('//*[@id="filterList6"]/h3').click()
time.sleep(2)
salary_options = ['blank', '20k-39k', '40k-59k', '60k-79k','80k-99k', '100+k']
salary_options_indexes = ['1', '', '', '', '']
for i in range (5):
    if salary_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="wage-level"]/div[' + salary_options_indexes[i] + ']/label').click()
        time.sleep(3)

#Period: Write the indexes of the desired options of the periods_options list in the period_options_indexes list. Leave blank if not a desired option.
period_toggle = driver.find_element_by_xpath('//*[@id="filterList7"]/h3').click()
time.sleep(2)
periods_options = ['blank', 'permanent', 'term/contract', 'seasonal', 'casual']
period_options_indexes = ['1', '', '', '']
for i in range(4):
    if period_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="periodemployment-type"]/div[' + period_options_indexes[i] + ']/label').click()
        time.sleep(3)

#Employment group: Write the indexes of the desired options of the group_options list in the group_options_indexes list. Leave blank if not a desired option.
group_toggle = driver.find_element_by_xpath('//*[@id="filterList8"]/h3').click()
time.sleep(2)
group_option = '1'
group_options = ['blank', 'indigenous', 'disabilities', 'newcomers', 'older', 'veteran', 'youth', 'visible minority', 'temporary foreign']
group_options_indexes = ['1', '', '', '', '', '', '', '8']
for i in range (8):
    if group_options_indexes[i] != '':
        group = driver.find_element_by_xpath('//*[@id="employmentgroups-type"]/div[' + group_options_indexes[i] + ']/label').click()
        time.sleep(3)

#Job source: Write the indexes of the desired options of the source_options list in the source_options_indexes list. Leave blank if not a desired option.
source_toggle = driver.find_element_by_xpath('//*[@id="filterList9"]/h3').click()
time.sleep(2)
source_options = ['blank', 'verified', 'exlude placement agencies', 'municipal governments', 'federal government', 'provincial and territorial governments']
source_options_indexes = ['1', '', '', '', '']
for i in range (5):
    if source_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="jobsource-type"]/div[' + source_options_indexes[i] + ']/label').click()
        time.sleep(3)

#Intended applicants: Write the indexes of the desired options of the applicant_options list in the applicant_options_indexes list. Leave blank if not a desired option.
applicants_toggle = driver.find_element_by_xpath('//*[@id="filterList10"]/h3').click()
time.sleep(2)
applicant_options = ['blank', 'Canadian and authorized workers', 'Canadian and international candidates']
applicant_options_indexes = ['1', '']
for i in range(2):
    if applicant_options_indexes[i] != '':
        driver.find_element_by_xpath('//*[@id="applicantgroup-type"]/div[' + applicant_options_indexes[i] + ']/label').click()
        time.sleep(3)



#Type the postion you are looking for
job = 'Cook'
job_field = driver.find_element_by_xpath('//*[@id="searchString"]')
job_field.send_keys(job)

#Type your location
location = 'Montreal'
location_field = driver.find_element_by_xpath('//*[@id="locationstring"]')
location_field.send_keys(location)
location_field.send_keys(Keys.ENTER)

#Job Listings Scrapping and DataFrame creation


time.sleep(3) 
while len(driver.find_elements_by_xpath('//*[@id="moreresultbutton"]')) > 0:
    more_jobs = driver.find_element_by_xpath('//*[@id="moreresultbutton"]').click()
    time.sleep(4)

time.sleep(3)  
df = pd.DataFrame({'Job Title':[''],'Company':[''], 'Posting Date':[''], 'Salary':[''], 'Application Link' :['']})
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('article')    

for posting in postings:
    job_title = ' '.join(posting.find('span', {'class':'noctitle'}).text.split())
    company = posting.find('li', {'class':'business'}).text
    date = posting.find('li', {'class':'date'}).text
    salary = posting.find('li', {'class':'salary'}).text.strip()[0:6] + ':'  + ' '+ posting.find('li', {'class':'salary'}).text.strip()[7:].lstrip()
    posting_link = 'https://www.jobbank.gc.ca' + posting.find('a', class_='resultJobItem').get('href')
    df = df.append({'Job Title': job_title, 'Company': company, 'Posting Date': date, 'Salary': salary, 'Application Link':posting_link}, ignore_index = True)

#Modify path to save CSV file of job postings to your computer
df.to_csv(f'/Users/admin/Desktop/coding_projects/Web_Scraping/{datetime.now()}_Job_Postings')


    









