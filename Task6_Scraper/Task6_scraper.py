# Task 6: Create a program for interactive web scraping
# Objective: Fetch data from a website and present it in a user-friendly way.

import requests
from bs4 import BeautifulSoup


def scrape_quotes():

    url = "http://quotes.toscrape.com/"

    print(f"🌐 Fetching data from: {url}\n")

    try:

        response = requests.get(url)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, 'html.parser')


        quotes_data = soup.find_all('div', class_='quote')

        print("==========================================")
        print("          INSPIRATIONAL QUOTES            ")
        print("==========================================\n")


        count = 1
        for block in quotes_data[:5]:
            text = block.find('span', class_='text').text
            author = block.find('small', class_='author').text

            print(f"Quote {count}: {text}")
            print(f"Author: - {author}")
            print("-" * 40)
            count += 1

        print("\n✅ Data scraped successfully!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")


if __name__ == "__main__":
    scrape_quotes()