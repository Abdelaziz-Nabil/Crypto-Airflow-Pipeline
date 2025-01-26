import json
import os
from requests import Session, ConnectionError, Timeout, TooManyRedirects
import logging


def load_config():
    # Get the directory of the current script (plugins/operations.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate to the project root directory
    project_root =  os.path.dirname(os.path.dirname(script_dir))
    
    # Construct the full path to the config.json file
    config_path = os.path.join(project_root, 'config', 'config.json')
    
    # Load the config.json file
    with open(config_path) as config_file:
        return json.load(config_file)


# Function to scrape cryptocurrency data
def scrape_crypto_data():
    config = load_config()
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config["X-CMC_PRO_API_KEY"],
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        # Return the list of cryptocurrencies
        return data["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Error while fetching data: {e}")
        return None
    
def scrape_task():
    logging.info("Starting to scrape cryptocurrency data...")
    crypto_data = scrape_crypto_data()
    if crypto_data is None:
        raise ValueError("Failed to fetch cryptocurrency data.")
    return crypto_data
