import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

"""
Git topics

This script is getting all the top topics of the github and creating
a new csv where you can find those topics with links/stars/authors etc.

Author: Erik Badalyan
Date: Nov 2022

"""
def getting_topics(site_url: str) -> tuple:     # Creating the csv of the topics
    # Requesting and parsering with Beautifulsoup:
    req = requests.get(site_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    topics_all = soup.find_all('div', class_='py-4 border-bottom d-flex flex-justify-between')
    titles = []
    descs = []
    links = []

    # making dataframe of topics with titles, desc, links:
    for topic in topics_all:
        try:
            titles.append(topic.find('p', class_='f3 lh-condensed mb-0 mt-1 Link--primary').text.strip())
            descs.append(topic.find('p', 'f5 color-fg-muted mb-0 mt-1').text.strip())
            links.append(f'https://github.com{topic.a["href"]}')
        except UnicodeEncodeError:
            continue
    data = {'Titles': titles, 'Descriptions': descs, "Links": links}
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('git_tops.csv', index=False)
    print("Topics_dataframe was created")
    return titles, links


def topics_thems(name_links: tuple) -> None:    # Making csvs with top topics reposotories
    # making other folder
    os.makedirs("topics_repositories")
    os.chdir(f'{os.getcwd()}\\topics_repositories')
    names_of_tops = name_links[0]
    links_repos = name_links[1]
    i = 0
    # loop throgh each topic and get repos
    for link in links_repos:
        names = []
        surnames = []
        stars = []
        links = []
        req_them = requests.get(link)
        soap = BeautifulSoup(req_them.text, 'html.parser')
        repositories = soap.find_all('article', class_='border rounded color-shadow-small color-bg-subtle my-4')
        # Get all data for each repo and creat csv
        for repo in repositories:
            name_surname = repo.find('h3', class_='f3 color-fg-muted text-normal lh-condensed')
            name = name_surname.text.strip().split()[0]
            surname = name_surname.text.strip().split()[2]
            names.append(name_surname.text.strip().split()[0])
            surnames.append(name_surname.text.strip().split()[2])
            stars.append(repo.find('span', id='repo-stars-counter-star').text)
            links.append(f'https://github.com/{name}/{surname}')
        data = {"Names": names, 'Surnames': surnames, 'Stars': stars, "Repo_link": links}
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(f'{names_of_tops[i]}.csv', index=False)
        print(f'csv file of {names_of_tops[i]} has created')
        i += 1


if __name__ == "__main__":
    url = 'https://github.com/topics'
    thems_links = getting_topics(url)
    topics_thems(thems_links)
