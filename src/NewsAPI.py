import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def fetch_top_headlines():
    """
    Fetches the top headlines from the NewsAPI for the business category in the US.

    :return: A list of top headlines or None if an error occurs.
    """
    api_url = "https://newsapi.org/v2/top-headlines"
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("API key not found. Please set the NEWS_API_KEY environment variable.")
        return None

    params = {
        "country": "ca",
        "category": "business",
        "apiKey": api_key
    }

    try:
        response = requests.get(api_url, params=params)
        # print(response)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()  # Parse the JSON response
        # print(data)
        if data["status"] == "ok":
            return data["articles"]
        else:
            print("Error in API response status:", data["status"])
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return None