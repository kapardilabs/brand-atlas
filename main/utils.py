import requests
from bs4 import BeautifulSoup


def crawl_link(url, brand_name_selector, country_selector, description_selector, ua):
    response = requests.get(url, headers={"User-Agent": ua})
    print("______CRAWLER_____")
    soup = BeautifulSoup(response.content, "html.parser")
    print(response.content)
    brand_tags = soup.select(brand_name_selector)
    print(brand_tags)
    country_tags = []
    description_tags = []
    if country_selector is not None:
        country_tags = soup.select(country_selector)

    if description_selector is not None:
        description_tags = soup.select(description_selector)

    brand_list = []

    country_list = []

    description_list = []

    for brand_tag in brand_tags:
        brand_list.append(brand_tag.text)

    for country_tag in country_tags:
        country_list.append(country_tag.text)

    for description_tag in description_tags:
        description_list.append(description_tag.text)

    return brand_list, country_list, description_list
