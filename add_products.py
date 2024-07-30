import requests

# Replace these with your actual API token and shop name
API_TOKEN = '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'
SHOP_NAME = '761d3f-f5'
API_VERSION = '2024-07'
COLLECTION_ID = '284382560339'  # Replace with the actual collection ID

# Headers for authentication
headers = {
    "X-Shopify-Access-Token": API_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# List of products to add
products = [
    {
        "title": "2000 Honda Civic Ex - Front Bumper Kit",
        "body_html": "<strong>Front bumper kit for 2000 Honda Civic Ex.</strong>",
        "vendor": "Your Vendor",
        "product_type": "Paint Protection Kit",
        "tags": "Year:2000, Make:Honda, Model:Civic, Submodel:Ex",
        "variants": [
            {
                "option1": "Default Title",
                "price": "199.99",
                "sku": "2000-honda-civic-ex-front-bumper"
            }
        ]
    },
    {
        "title": "2000 Honda Civic Ex - Rear Bumper Kit",
        "body_html": "<strong>Rear bumper kit for 2000 Honda Civic Ex.</strong>",
        "vendor": "Your Vendor",
        "product_type": "Paint Protection Kit",
        "tags": "Year:2000, Make:Honda, Model:Civic, Submodel:Ex",
        "variants": [
            {
                "option1": "Default Title",
                "price": "179.99",
                "sku": "2000-honda-civic-ex-rear-bumper"
            }
        ]
    },
    {
        "title": "2017 Toyota Corolla LE - Rear Fenders",
        "body_html": "<strong>Rear fenders for 2017 Toyota Corolla LE.</strong>",
        "vendor": "Your Vendor",
        "product_type": "Paint Protection Kit",
        "tags": "Year:2017, Make:Toyota, Model:Corolla, Submodel:LE",
        "variants": [
            {
                "option1": "Default Title",
                "price": "149.99",
                "sku": "2017-toyota-corolla-le-rear-fenders"
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
        print(f"Failed to add product {product['title']}. Status code: {response.status_code}")

# Add each product and assign it to the collection
for product in products:
    add_product_and_assign_to_collection(product)
