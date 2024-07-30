import requests
#
# Replace with your actual API token and shop name
API_TOKEN = ''
SHOP_NAME = '761d3f-f5'
API_VERSION = '2024-07'

# Headers for authentication
headers = {
    "X-Shopify-Access-Token": API_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# URL to get the list of collections
collections_url = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/custom_collections.json"

# Make the request
response = requests.get(collections_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    collections = response.json()['custom_collections']
    for collection in collections:
        print(f"Collection ID: {collection['id']}, Title: {collection['title']}")
else:
    print(f"Failed to retrieve collections. Status code: {response.status_code}, Response: {response.text}")
