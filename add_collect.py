import requests
#
# Replace with your actual API token and shop name
API_TOKEN = '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'
SHOP_NAME = '761d3f-f5'
API_VERSION = '2024-07'

# Headers for authentication
headers = {
    "X-Shopify-Access-Token": API_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Data for the new collection
collection_data = {
    "custom_collection": {
        "title": "Paint Protection Film Kits",
        "body_html": "<strong>Protect your vehicle's paint with our high-quality film kits.</strong>",
        "published": True
    }
}

# URL for creating a custom collection
url = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/custom_collections.json"

# Make the request to create the collection
response = requests.post(url, headers=headers, json=collection_data)

# Check if the request was successful
if response.status_code == 201:
    print("Collection created successfully.")
    print(response.json())
else:
    print(f"Failed to create collection. Status code: {response.status_code}")
    print(response.text)