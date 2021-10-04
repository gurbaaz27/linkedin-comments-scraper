# LinkedIn Comments Scraper <img src="assets/linkedin_logo.png" width="50" height="50"></img>

## Updates 🚀

- [x] Fix utf-8 encoding error
- [x] Shift configuration from Config.py to config.json
- [x] Add support for profile pictures of commentors
- [ ] Add support for pulling images in comment section
- [x] Add headless support 
- [ ] Chrome extension

## Brief Overview
If you have used LinkedIn, you must have encountered many posts regarding helpful resources, and they would ask email address,to which replies in comments are usually like
```bash
Interested!
<email-address>
 ``` 
I don't like this thing, like you can already share link in the post itself :angry:. **Nevertheless**, I thought to automate this work of collecting all emails.  
All the comments, with columns of 
* Name of the person commented
* Designation of the person
* Email address (if present in comment)
* Comment (UTF-8 encoded)

are stored in a csv.

## Requirements
* [python](https://www.python.org/) (recommended : 3.7.3)
* [selenium](https://pypi.org/project/selenium/) <img src="assets/selenium_logo.png" width="20" height="20"></img>
* [web-driver](https://pypi.org/project/webdriver-manager/)

Install the dependencies in Windows using command:
```bash
pip install -r requirements.txt
```
For Mac/Linux, use:
```bash
pip3 install -r requirements.txt
```

## Usage

- In `config.json`, enter the required url of LinkedIn Post in **post_url** variable:
```python
post_url = ""
```
> *__NOTE__*: If you forget to enter here, it will be asked during run-time of script itself.

- You can also change csv file name (in which scraped data will be stored) and dir name (in which profile pics will be downloaded) in `config.json` .
- Help:
```
usage: main.py [-h] [--headless] [--download-pfp]

Linkedin Scraping.

optional arguments:
  -h, --help      show this help message and exit
  --headless      Go headless browsing
  --download-pfp  Download profile pictures of commentors
```

- Run the script for Windows:
```bash
python main.py
```
For Linux/Linux, use:
```bash
python3 main.py
```
Login email and password for your LinkedIn account will be asked and process would start.

### Configuration

`config.json` contains various fields, containing information about scraping the HTML elements by name or xpath, and other metadata


## Scope of Improvement
* Main problem is that for scraping all comments, they need to be loaded first. This involves: find the "Load more comments" button, clicks, sleeps for 5 seconds and continues this until all comments are loaded. Usually the **sleep strategy** of 5 seconds works well, but may fail on slow internet connection and needs to be increased. There are certain commands in Selenium to avoid this but I was unsuccessful. 

If you can do it or have any suggestions, contribute!:smile: