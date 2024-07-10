# requests needs to be instal through the terminal 'pip install requests'
import requests

def fetch_top_headlines():
    """
    Fetches the top headlines from the NewsAPI for the business category in the US.

    :return: A list of top headlines or None if an error occurs.
    """
    api_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "category": "business",
        "apiKey": "60d937e731f14acb84d596ba3e713d76"
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()  # Parse the JSON response
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
