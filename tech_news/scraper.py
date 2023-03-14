import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    news_urls = sel.css('.cs-overlay > a::attr(href)').getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    next_link = sel.css("a.next").get()
    if next_link:
        return sel.css("a.next::attr(href)").get()
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    select = Selector(text=html_content)
    news = {
        'url': select.css("link[rel='canonical']::attr(href)").get(),
        'title': select.css("h1.entry-title::text").get().strip(),
        'timestamp': select.css("li.meta-date::text").get(),
        'writer': select.css("span.author a::text").get(),
        'reading_time': int(
            select.css("li.meta-reading-time::text").get()[:2]),
        'summary': ''.join(
            select.css(
                ".entry-content > p:first-of-type *::text").getall()).strip(),
        'category': select.css(".label::text").get()
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
