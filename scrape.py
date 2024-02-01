import requests

url = 'https://www.99acres.com/flats-in-mumbai-ffid-page-11'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    # Now, you can use BeautifulSoup to parse the HTML content
    # ...
else:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")


response