from bs4 import BeautifulSoup
import requests
import csv

html = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
html_request = requests.get(html).text
soup = BeautifulSoup(html_request, 'lxml')
all_jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')
with open("Jobs_list.csv", 'w', newline='') as f:
    thewriter = csv.writer(f)
    header = ['job', 'skills', 'link']
    thewriter.writerow(header)
    for job in all_jobs:
        name_job = job.a.text.strip().replace('/n', '')
        req_skills = job.find('span', class_='srp-skills').text.lower().replace(' ', '').strip().replace('/n', '')
        link_description = job.a['href'].strip()
        info = [name_job, req_skills, link_description]
        thewriter.writerow(info)
