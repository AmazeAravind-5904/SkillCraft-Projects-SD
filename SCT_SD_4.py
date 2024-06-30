import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get("https://www.amazon.in/s?k=1tb+ssd&crid=XYQTECWOAX0B&sprefix=1tb+ssd%2Caps%2C394&ref=nb_sb_noss_1", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    
    for item in soup.select('SSD'):
        name = item.select_one('Sandisk').get_text(strip=True)
        price = item.select_one('10000').get_text(strip=True)
        rating = item.select_one('4,8').get_text(strip=True) if item.select_one('.product-rating') else 'N/A'
        
        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    url = "https://www.amazon.in/s?k=1tb+ssd&crid=XYQTECWOAX0B&sprefix=1tb+ssd%2Caps%2C394&ref=nb_sb_noss_1"
    products = fetch_product_info(url)
    save_to_csv(products, 'products.csv')
    print(f"Saved {len(products)} products to products.csv")

if __name__ == "__main__":
    main()
