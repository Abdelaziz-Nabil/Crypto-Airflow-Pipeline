import os
import sqlite3
import logging



def create_table(path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    conn = sqlite3.connect(path)  # Use the absolute path here
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id INTEGER PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            rank INTEGER,
            slug TEXT,
            is_active INTEGER,
            first_historical_data TEXT,
            last_historical_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_crypto_data(transformed_data , path):
    conn = sqlite3.connect(path)  # Use the absolute path here
    cursor = conn.cursor()

    for crypto in transformed_data:
        cursor.execute('''
            INSERT OR REPLACE INTO cryptocurrencies
            (id, name, symbol, rank, slug, is_active, first_historical_data, last_historical_data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (crypto['id'], crypto['name'], crypto['symbol'], crypto['rank'], crypto['slug'],
              crypto['is_active'], crypto['first_historical_data'], crypto['last_historical_data']))

    conn.commit()
    conn.close()


def store_task(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids="TransformCrypto" , dag_id = 'crypto_pipeline')

    logging.info("Storing cryptocurrency data in the database...")
    # Get the directory of the current script or specify a known directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate to the project root directory
    project_root = os.path.dirname(os.path.dirname(script_dir))

    db_path = os.path.join(project_root ,"data", 'crypto_data.db')
    create_table(path = db_path)
    store_crypto_data(transformed_data=transformed_data , path = db_path)