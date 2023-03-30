# LinkedIn Comments Scraper <img src="assets/linkedin_logo.png" width="50" height="50"></img>

## Updates 🚀

- [x] Fix utf-8 encoding error
- [x] Shift configuration from Config.py to config.json
- [x] Add support for profile pictures of commentors
- [ ] Add support for pulling images in comment section
- [x] Add headless support 
- [ ] Chrome extension
- [x] Show all replies support

## Brief Overview
If you have used LinkedIn, you must have encountered many posts regarding helpful resources, and they would ask email address,to which replies in comments are usually like
```bash
Interested!
<email-address>
 ``` 
I don't like this thing, like you can already share link in the post itself :angry:. **Nevertheless**, I thought to automate this work of collecting all emails.  
All the comments, with columns of 
- Name of the person commented
- Designation of the person
- Profile Picture URL
- Email address (if present in comment)
- Comment (UTF-8 encoded)

are stored in a csv.

## Requirements
- [python](https://www.python.org/) (recommended : >= 3.7)
- [selenium](https://pypi.org/project/selenium/) 
<!-- <img src="assets/selenium_logo.png" width="20" height="20"></img> -->
- [web-driver](https://pypi.org/project/webdriver-manager/)

Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

- In `config.json`, enter the required url of LinkedIn Post in **post_url** variable:
```python
post_url = ""
```
> *__NOTE__*: If you forget to enter here, it will be asked during execution of script itself.

- You can also change csv file name (in which scraped data will be stored) and dir name (in which profile pics will be downloaded) in `config.json` .
- Help:
```
usage: main.py [-h] [--headless] [--show-replies] [--download-pfp]

Linkedin Scraping.

options:
  -h, --help      show this help message and exit
  --headless      Go headless browsing
  --show-replies  Load all replies to comments
  --download-pfp  Download profile pictures of commentors
```
> *__NOTE__*: Even if the flag `--download-pfp` isn't provided, URLs of image would get stored in the output csv.

- Run the script:
```bash
python main.py
```

Login email and password for your LinkedIn account will be asked and process would start.

### Configuration

`config.json` contains various fields, containing information about scraping the HTML elements by name or xpath, and other metadata

Suggestions and contributio ns are alwasy welcome!:smile:
