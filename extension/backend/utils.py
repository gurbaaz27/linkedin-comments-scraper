import re
from time import sleep
import urllib.request
import os


def load_more_comments(load_comments_class, driver):
    try:
        load_more_button = driver.find_element_by_class_name(load_comments_class)
        print("[", end="", flush=True)
        while True:
            load_more_button.click()
            sleep(5)
            # 5 second sleep works great for medium-speed net...you can increase if this time seems too less and program finishes before loading all comments....you may decrease till 3 if you have fast internet speed
            try:
                load_more_button = driver.find_element_by_class_name(
                    load_comments_class
                )
            except:
                print("]")
                print("All comments have been displayed!")
                break
            print("#", end="", flush=True)
    except:
        print("All comments are displaying already!")


def extract_emails(comments):
    emails = []
    for comment in comments:
        email_match = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", comment)
        if email_match:
            emails.append(email_match)
        else:
            emails.append("-")
    return emails


def write_data2csv(names, avatars, headlines, emails, comments, writer):
    for name, avatar, headline, email, comment in zip(
        names, avatars, headlines, emails, comments
    ):
        writer.writerow([name, avatar, headline, email, comment.encode("utf-8")])
        # utf-8 encoding helps to deal with emojis


def download_avatars(urls, filenames, dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass

    filenames = [
        filename.lower().replace(".", "").replace(" ", "-") for filename in filenames
    ]

    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
            "User-Agent",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
        )
    ]
    urllib.request.install_opener(opener)

    for url, filename in zip(urls, filenames):
        urllib.request.urlretrieve(url, f"{dir_name}/{filename}.jpg")

    print("Profile pictures have been downloaded!")
