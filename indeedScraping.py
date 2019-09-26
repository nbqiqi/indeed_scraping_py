import requests
import datetime
from bs4 import BeautifulSoup
from csv import writer

# https://www.indeed.ca/jobs?q=electrical+engineer&l=alberta&sort=date&limit=50&radius=0&ts=1564344380517&pts=1563941443553&rq=1&fromage=last

searchArea = input("Enter Area of Interest: ")
response = requests.get('https://www.indeed.ca/jobs?q=electrical+engineer&l=' + searchArea + '&radius=0&sort=date&limit=50')

now = datetime.datetime.now()
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all(class_='jobsearch-SerpJobCard unifiedRow row result')

with open('jobs_' + searchArea + now.strftime("_%Y-%m-%d") + '.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Position','Company','Location','Date']
    csv_writer.writerow(headers)

    for post in posts:
        if not post.findAll(class_='sponsoredGray'):
            position = post.find(class_='title').get_text().strip()
            company = post.find(class_='company').get_text().strip()
            location = post.find(class_='location').get_text().strip()
            date = post.find(class_='date').get_text().strip()
            csv_writer.writerow([position,company,location,date])
