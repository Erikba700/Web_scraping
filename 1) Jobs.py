from bs4 import BeautifulSoup
import requests

my_skills = input('Your skills: ').lower().replace(' ', '').split(',')
html = ('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
html_request = requests.get(html).text
soup = BeautifulSoup(html_request, 'lxml')
all_jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')
for job in all_jobs:
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
        print(f'''\n
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

my_skills: {my_skills}
req_skills: {req_skills.split(',')}
Job name: {name_job}
skills: {req_skills}
more_info: {link_description}
eligible: {eligible}
lack_skills: {lack_skills}

_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
''')
