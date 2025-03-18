import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all headings (h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])

        # Print out each heading found on the page
        for heading in headings:
            print(heading.text.strip())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to scrape: ")
    scrape_webpage(url)