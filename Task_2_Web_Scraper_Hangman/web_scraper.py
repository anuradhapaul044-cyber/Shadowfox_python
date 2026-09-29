import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    data = []

    for quote, author in zip(quotes, authors):
        data.append({
            "Quote": quote.get_text(strip=True),
            "Author": author.get_text(strip=True)
        })

    print("Scraped Data:\n")

    for item in data:
        print("Quote:", item["Quote"])
        print("Author:", item["Author"])
        print()

    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Quote", "Author"])
        writer.writeheader()
        writer.writerows(data)

    print("Data saved successfully to scraped_data.csv")

except requests.exceptions.RequestException as error:
    print("Error while accessing the website:", error)

except Exception as error:
    print("An unexpected error occurred:", error)