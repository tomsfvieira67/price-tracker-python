import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_book(url):
    print(f"[*] Fetching page: {url}")
    
    # Spoofing User-Agent to mimic a real web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # Send the HTTP GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product details using HTML tags and classes
        title = soup.find('h1').text
        price = soup.find('p', class_='price_color').text
        stock = soup.find('p', class_='instock availability').text.strip()
        
        # Display the formatted report
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n" + "="*45)
        print("📦 PRODUCT REPORT")
        print("="*45)
        print(f"Title : {title}")
        print(f"Price : {price}")
        print(f"Stock : {stock}")
        print(f"Date  : {now}")
        print("="*45 + "\n")
        
    except Exception as e:
        print(f"\n[CRITICAL ERROR] Failed to scrape the page: {e}")

if __name__ == "__main__":
    # Sandbox URL for web scraping practice
    target_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    
    scrape_book(target_url)