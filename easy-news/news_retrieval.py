import os

import requests
from data_classes import Article
from dotenv import load_dotenv


def get_headlines(country_code: str, api_key: str) -> dict:
    url = "https://newsapi.org/v2/top-headlines"
    params = {"country": country_code, "apiKey": api_key}
    response = requests.get(url, params=params)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
        return {}


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")

    headlines = get_headlines(country_code="us", api_key=api_key)
    articles = [Article.from_dict(x) for x in headlines["articles"]]
    for art in articles:
        print(str(art))
        print("====")
