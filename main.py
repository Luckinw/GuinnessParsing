import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    link_div = soup.find('div',class_='block block-12-12'  )
    links = link_div.find_all('a')
    link_list = []
    for link in links:
        href = link.get( 'href' )
        link_list.append(href)
    return link_list


def extract_each_guinness(url):
    response = requests.get( url )
    soup = BeautifulSoup( response.text, 'html.parser' )
    div_records = soup.find( 'div', class_='explore-list-wrap' )
    links = div_records.find_all('a')
    link_list = []
    for link in links:
        href = link.get('href')
        link_list.append(href)
    return link_list

def exract_title_who(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    who = soup.find('div', class_='equal-one block block-4-12')
    title = soup.find( 'div', class_='page-header block block-11-12' )
    def nothing_to_return():
        who, title = 'Unknow', 'Unknow'
        return who, title
    if who != None:
        who = who.find('dd').text.strip()
    else:
        return nothing_to_return()
    if title != None:
        title  = title.find('h1').text.strip()
    else:
        return nothing_to_return()
    return who , title


file = open('guinness.csv','w',newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Who', 'Link'])
url = 'https://www.guinnessworldrecords.com/records/showcase'
links = extract_links(url)

for url in links:
    url = 'https://www.guinnessworldrecords.com'+url
    new_url = extract_each_guinness(url)
    for url in new_url:
        for_title_who = 'https://www.guinnessworldrecords.com'+ url
        who, title = exract_title_who(for_title_who)
        data = [[title,who,for_title_who]]
        writer.writerows(data)
        sleep(randint(3,15))