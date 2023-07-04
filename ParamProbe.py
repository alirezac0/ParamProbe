from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse

parser = argparse.ArgumentParser(description='FUZZ reflected parameters with Headless browser')
parser.add_argument('-u', '--url', type=str, required=False, help='URL to test')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='Wordlist file')
parser.add_argument('-l', '--url-list', type=str, help='File containing list of URLs to test')
parser.add_argument('-c', '--count', type=int, default=1, help='Number of queries to send in a single request')
parser.add_argument('-H', '--header', type=str, action='append', help='HTTP headers')
args = parser.parse_args()

if not args.url and not args.url_list:
    print("Error: Either -u or -l must be specified")
    exit()

if args.url and args.url_list:
    print("Error: -u and -l cannot be used together")
    exit()

if args.url:
    urls = [args.url]
else:
    with open(args.url_list, 'r') as f:
        urls = f.read().splitlines()

chrome_options = Options()
chrome_options.add_argument('--headless')
if args.header:
    for header in args.header:
        chrome_options.add_argument(f"--header={header}")
driver = webdriver.Chrome(options=chrome_options)

with open(args.wordlist, 'r') as f:
    words = f.read().splitlines()

for url in urls:
    if '?' in url:
        query_separator = '&'
    else:
        query_separator = '?'

    for i in range(0, len(words), args.count):
        query_words = words[i:i+args.count]
        query = query_separator + "&".join([f"{word}=zxc{i}" for i, word in enumerate(query_words)])
        full_url = url + query
        driver.get(full_url)
        if 'zxc' in driver.page_source:
            for i, query_word in enumerate(query_words):
                if f'zxc{i}' in driver.page_source:
                    print(f"{query_word} reflected in {url}")

driver.quit()