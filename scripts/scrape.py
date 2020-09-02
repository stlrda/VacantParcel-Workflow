# Functions for Scraping the Parcel API and Storing in The RedB Database

# Get Connection Information from Airflow Connections
import requests
import psycopg2
from psycopg2.extras import Json, DictCursor

DB_HOST = ''
DB_NAME = ''
DB_PORT = 5432
DB_PASS = ''
DB_USER = ''

# Connection to DB
conn = psycopg2.connect(host = DB_HOST, port = DB_PORT, user = DB_USER, password = DB_PASS, database = DB_NAME)

def api_get_parcel(url, key, handle):
    query = url + '?key=' + key + '&handle=' + handle
    resp = requests.get(query)
    return resp.json()

def scrape_parcel_api(url, key, list_handles):
    for handle in list_handles:
        # Get Parcel Info from API
        parcel_info = api_get_parcel(url, key, handle)

        # Put this Info in the Database
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("INSERT INTO city_api.parcel_data (handle, parcel_data) VALUES(%s, %s) ON CONFLICT (handle) DO UPDATE SET parcel_data = %s", (handle, Json(parcel_info), Json(parcel_info)))
        conn.commit()
        cursor.close()

# Get List of Handles
cursor = conn.cursor()
#handles = cursor.execute("SELECT county_parcel_id FROM core.county_id_mapping;") Those are parcel 11
# Still need list of parcels
handle_list = ['12075000090', '00010000050']

scrape_parcel_api('https://portalcw.stlouis-mo.gov/a/property', api_key, handle_list) 

