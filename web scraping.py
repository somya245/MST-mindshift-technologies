import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for Oxylabs Sandbox Products
BASE_URL = "https://sandbox.oxylabs.io/products"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# List to store extracted products
products_data = []

# Function to scrape products
def scrape_products():
    print("Scraping products from Oxylabs Sandbox...")
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('div', class_='product-card css-e8at8d eag3qlw10')
    
    for product in products:
        name_tag = product.find('h4', class_='title css-7u5e79 eag3qlw7')
        description_tag = product.find('p', class_='description css-cput12 eag3qlw5')
        price_tag = product.find('div', class_='price-wrapper css-li4v8k eag3qlw4')
        availability_tag = product.find('p', class_='in-stock css-1w904rj eag3qlw1')
        
        product_data = {
            "Name": name_tag.text.strip() if name_tag else "N/A",
            "Description": description_tag.text.strip() if description_tag else "N/A",
            "Price": price_tag.text.strip() if price_tag else "N/A",
            "Availability": availability_tag.text.strip() if availability_tag else "N/A"
        }
        
        products_data.append(product_data)
        print(f"Scraped: {product_data['Name']}-->{price_tag.string}\n")

# Scrape the data
scrape_products()

# Save data to CSV
if products_data:
    df = pd.DataFrame(products_data)
    df.to_csv('oxylabs_products.csv', index=False)
    print("Products saved to 'oxylabs_products.csv'")
else:
    print("No data scraped.")
