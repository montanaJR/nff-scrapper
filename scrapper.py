import re

import requests
from bs4 import BeautifulSoup
from offer import Offer

# todo make it parametrized
from strategy.FileExportContext import FileExportContext
from strategy.CSVConcreteStrategy import CSVConcreteStrategy
from strategy.JSONConcreteStrategy import JSONConcreteStrategy


def scrap():
    html_text = requests.get(
        'https://nofluffjobs.com/jobs/krakow/backend?criteria=city%3Dkrakow%20category%3Dbackend,fullstack%20seniority%3Dmid%20java').text
    initial_soup = BeautifulSoup(html_text, features='xml')
    link_len = len(initial_soup.find_all('a', class_='page-link')) - 2
    index = 0
    offersList = []
    for i in range(link_len):
        http = 'https://nofluffjobs.com'
        page = i + 1
        html_offers = requests.get(
            f'{http}/jobs/krakow/backend?criteria=city%3Dkrakow%20category%3Dbackend,fullstack%20seniority%3Dmid%20java&page={page}').text
        soup = BeautifulSoup(html_offers, 'lxml')
        offers = soup.find_all('a', class_=re.compile("posting-list-item posting-list-item"), href=True)

        for job in offers:

            wrapper_pos_comp = job.find('div', class_='posting-title__wrapper')
            position = wrapper_pos_comp.find('h4', class_='posting-title__position').text
            company = wrapper_pos_comp.find('span', class_='posting-title__company').text.replace(" w ", "")

            wrapper_fork_loc = job.find('div', class_='posting-info position-relative d-none d-lg-flex flex-grow-1')
            fork = wrapper_fork_loc.find('span',
                                         class_='text-truncate badgy salary btn btn-outline-secondary btn-sm').text
            if wrapper_fork_loc.find('a', class_='btn text-truncate btn-outline-secondary btn-sm') is not None:
                tech = wrapper_fork_loc.find('a', class_='btn text-truncate btn-outline-secondary btn-sm').text
            loc = wrapper_fork_loc.find('nfj-posting-item-city', class_='mr-1 flex-shrink-0').text
            loc = loc.partition('+')[0]
            link = http + job['href']

            index += 1
            offersList.append(Offer(index, position, company, fork, tech, loc, link))

    return offersList


for obj in scrap():
    print('===============================')
    print(
        f'{obj.index}. {obj.position} in {obj.company} with salary {obj.fork} '
        f'and main technology {obj.tech} based in {obj.loc} \n Link: {obj.link}')
strategy = CSVConcreteStrategy()
context = FileExportContext(strategy)
context.export(scrap())

strategy2 = JSONConcreteStrategy()
context2 = FileExportContext(strategy2)
context2.export(scrap())
