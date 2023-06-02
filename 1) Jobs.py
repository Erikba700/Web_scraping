from bs4 import BeautifulSoup
import requests
import csv

"""
Jobs filter:

It is a manual job filter for a freelance market where the jobs filter 
by skills is missing. So, this script is collecting your skills,
scrapping jobs (published a few days ago), and presenting jobs that fit 
your skills. It also provides additional skills that the job requires
from you and links to that job description for more info.

P.S. It also returns results in a newly created .csv format file.

Author: Erik Badalyan
Date: May 2023

"""


my_skills = input('Your skills: ').lower().replace(' ', '').split(',')
html = ('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
        '=python&txtLocation=')
html_request = requests.get(html).text
soup = BeautifulSoup(html_request, 'lxml')
all_jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')
# The csv Createing code

with open("Jobs_list.csv", 'w', newline='') as f:
    thewriter = csv.writer(f)
    header = ['job', 'skills', 'eligible', 'lack of skills' 'link']
    thewriter.writerow(header)
    idx = 0
    for job in all_jobs:
        idx += 1
        is_up_to_date = job.find('span', class_='sim-posted').span.text
        eligible = False
        if 'few' in is_up_to_date:
            name_job = job.a.text.strip()
            req_skills = job.find('span', class_='srp-skills').text.lower().replace(' ', '').strip()
            # python, web technologies, linux, mobile, mysql, angularjs, javascript
            link_description = job.a['href'].strip()
            lack_skills = ','.join(list(filter(lambda skill: skill not in my_skills, req_skills.split(','))))
            if len(lack_skills) == 0:
                eligible = True

            name_job = job.a.text.strip().replace('/n', '')
            req_skills = job.find('span', class_='srp-skills').text.lower().replace(' ', '').strip().replace('/n', '')
            link_description = job.a['href'].strip()
            info = [name_job, req_skills, eligible, lack_skills, link_description]
            thewriter.writerow(info)

            print(f'''\n
    ({idx})-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    

    my_skills: {my_skills}
    req_skills: {req_skills.split(',')}
    Job name: {name_job}
    more_info: {link_description}
    eligible: {eligible}
    lack_skills: {lack_skills}

    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    ''')
