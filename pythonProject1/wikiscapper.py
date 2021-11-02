import requests
from bs4 import BeautifulSoup
import random
import webbrowser


# while True:
#     response = requests.get(url="https://en.wikipedia.org/wiki/")
#     soup = BeautifulSoup(response.content, "html.parser")
#     title = soup.find(class_="firstHeading").text
#     print(f"{title}do you want to read it\n")
#     ans = input(">>>").lower()
#
#     if ans == 'y':
#         response = "https://en.wikipedia.org/wiki/%s" % title
#         webbrowser.open(response)
#     elif ans == 'n':
#         print("try again")
#         continue
#     else:
#         print("wrong input")
#         break

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])


scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
