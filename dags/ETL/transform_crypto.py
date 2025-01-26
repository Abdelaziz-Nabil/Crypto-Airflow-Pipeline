
import logging


def filter_top_cryptos(crypto_data, top_n=10):
    # Sort the cryptocurrencies by rank and return the top N
    return sorted(crypto_data, key=lambda x: x['rank'])[:top_n]

def transform_data(crypto_data):
    # Example transformation: extract useful fields
    transformed_data = []
    for crypto in crypto_data:
        transformed_data.append({
            'id': crypto['id'],
            'name': crypto['name'],
            'symbol': crypto['symbol'],
            'rank': crypto['rank'],
            'slug': crypto['slug'],
            'is_active': crypto['is_active'],
            'first_historical_data': crypto['first_historical_data'],
            'last_historical_data': crypto['last_historical_data']
        })
    return transformed_data


def transform_task(**kwargs):
        ti = kwargs['ti']
        crypto_data = ti.xcom_pull(task_ids="ExtractCrypto" , dag_id = 'crypto_pipeline')
        if not crypto_data:
            raise ValueError("No data received from ExtractCrypto task.")
        logging.info("Transforming cryptocurrency data...")
        top_cryptos = filter_top_cryptos(crypto_data, top_n=10)
        return transform_data(top_cryptos)