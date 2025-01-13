from bs4 import BeautifulSoup
import requests
import lxml
import urllib.request
import urllib.parse

url = "https://www.linkedin.com/jobs/collections/recommended/"
urls = [url]

html_text = requests.get('https://www.linkedin.com/jobs/collections/recommended')
soup = BeautifulSoup(html_text.text, "lxml")  # Use .text to get the page content
#print(html_text.text)  # Print the raw HTML content to confirm it's being fetched correctly

jobs = soup.find_all('li', class_='ember-view   mdijrNyBqsqmTYWxqdFZpkGSrQFzkUHozJRxiWgg occludable-update p0 relative scaffold-layout__list-item')
print(jobs)
