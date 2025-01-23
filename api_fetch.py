import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def get_stock_data(stock_id):
	""" Fetches stock data from seeking alpha-id """
	url = "https://seeking-alpha.p.rapidapi.com/symbols/get-profile"

	querystring = {"symbols":stock_id}

	headers = {
		"x-rapidapi-key": api_key,
		"x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	return(response.json())