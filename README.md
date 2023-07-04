# ParamProbe

ParamProbe is a Python tool that leverages Selenium to perform parameter discovery for single page applications. It takes a wordlist with arguments and either a single URL or a file containing multiple URLs to check. 🦑

## Installation


1. Clone the ParamProbe repository from GitHub:
   ```bash
   git clone https://github.com/alirezac0/paramprobe.git
   ```

2. Navigate to the ParamProbe directory:
   ```bash
   cd paramprobe
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Use Arguments to run the tool
   ```bash
   python3 ParamProbe.py -l /PATH/TO/URLLIST -w /PATH/TO/WORDLIST -c 50
   ```

## Arguments

```bash
$ python3 ParamProbe.py -h
usage: ParamProbe.py [-h] [-u URL] -w WORDLIST [-l URL_LIST] [-c COUNT] [-H HEADER]

FUZZ reflected parameters with Headless browser

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to test
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist file
  -l URL_LIST, --url-list URL_LIST
                        File containing list of URLs to test
  -c COUNT, --count COUNT
                        Number of queries to send in a single request
  -H HEADER, --header HEADER
                        HTTP headers
```

## To-Do List

- [ ] Double check founded parameters to prevent false positives.
- [ ] Integrate Selenium for web scraping.
- [ ] Parse and analyze the HTML response.
- [ ] Enhance error handling and exception management.

Feel free to contribute to this project by opening issues or submitting pull requests. Happy parameter discovery! 🔥🔥
