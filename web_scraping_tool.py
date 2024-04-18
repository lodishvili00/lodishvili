import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_articles = []

    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")
    for headline in headlines:
        title = headline.get_text().strip()
        link = headline.find("a")["href"]
        news_articles.append({"title": title, "link": link})

    return news_articles

if __name__ == "__main__":
    news = scrape_bbc_news()
    print("BBC News Headlines:")
    for idx, article in enumerate(news, start=1):
        print(f"{idx}. {article['title']}")
        print(f"   Link: {article['link']}")
        print()
