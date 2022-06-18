import random

import requests
from bs4 import BeautifulSoup


def scrapeWikiArticle(url):
    try:
        response = requests.get(url, timeout=5)

    except ConnectionError:
        print(f"[!] Got {response.status_code}, skipping {url}")
        return

    except:
        print(f"[!] That's it, Wikipedia won't allow us to crawl any further... Bye")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    print(f"[+] {url} -> {title.text}")

    # Get all the link
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)

    for link in allLinks:
        link_url = link['href']
        try:
            if 'wiki' in link_url:
                scrapeWikiArticle("https://en.wikipedia.org" + link_url)
                crawled += 1
        except:
            return

scrapeWikiArticle("https://en.wikipedia.org/wiki/Battle_of_Waterloo")
