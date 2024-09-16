
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract all the links from the webpage
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

if __name__ == '__main__':
    url = 'https://example.com'
    scrape_website(url)
