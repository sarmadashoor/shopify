#api token: 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
#api key: 2104778a160703a76278c203aa639424
#api secret key: 1a271f9cc93286b43e79e1ba4ed3458f

import requests
import requests
#
# Replace these with your actual API token and shop name
API_TOKEN = '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'
SHOP_NAME = '761d3f-f5'
API_VERSION = '2024-07'



# Collection ID (you'll need to get this from the response of the collection creation or manually if known)
COLLECTION_ID = '284345729107'

# Headers for authentication
headers = {
    "X-Shopify-Access-Token": API_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# List of products to add with tags for filtering
products = [
    {
        "title": "PPF Product 1",
        "body_html": "<strong>High-quality PPF for your car.</strong>",
        "vendor": "PPF Vendor",
        "product_type": "PPF",
        "tags": "Year:2000, Make:Honda, Model:Civic, Submodel:DX, Series:Coupe",
        "variants": [
            {
                "option1": "Default Title",
                "price": "199.99",
                "sku": "ppf1"
            }
        ]
    },
    {
        "title": "PPF Product 2",
        "body_html": "<strong>Durable PPF for your car.</strong>",
        "vendor": "PPF Vendor",
        "product_type": "PPF",
        "tags": "Year:2001, Make:Toyota, Model:Camry, Submodel:LE, Series:Sedan",
        "variants": [
            {
                "option1": "Default Title",
                "price": "249.99",
                "sku": "ppf2"
            }
        ]
    }
    # Add more products as needed
]

# Function to add a product and assign it to a collection
def add_product_and_assign_to_collection(product):
    product_url = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/products.json"
    response = requests.post(product_url, headers=headers, json={"product": product})
    if response.status_code == 201:
        product_id = response.json()['product']['id']
        collect_url = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/collects.json"
        collect_data = {
            "collect": {
                "product_id": product_id,
                "collection_id": COLLECTION_ID
            }
        }
        collect_response = requests.post(collect_url, headers=headers, json=collect_data)
        if collect_response.status_code == 201:
            print(f"Product {product['title']} added and assigned to collection successfully.")
        else:
            print(f"Failed to assign product {product['title']} to collection.")
    else:
        print(f"Failed to add product {product['title']}.")

# Add each product and assign it to the collection
for product in products:
    add_product_and_assign_to_collection(product)

# Function to create a custom collection for Paint Protection Films
def create_collection():
    collection_url = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/custom_collections.json"
    collection_data = {
        "custom_collection": {
            "title": "Paint Protection Films",
            "body_html": "<strong>Protect your vehicle's paint with our high-quality films.</strong>",
            "published": True
        }
    }
    collection_response = requests.post(collection_url, headers=headers, json=collection_data)
    if collection_response.status_code == 201:
        collection_id = collection_response.json()['custom_collection']['id']
        print("Collection created successfully.")
        print("Collection details:", collection_response.json())
        return collection_id
    else:
        print("Failed to create the collection.")
        print(f"Response Status Code: {collection_response.status_code}")
        print(f"Response Text: {collection_response.text}")
        return None

# Create the collection and get the collection ID
COLLECTION_ID = create_collection()

# If collection creation was successful, add products to the collection
if COLLECTION_ID:
    for product in products:
        add_product_and_assign_to_collection(product)