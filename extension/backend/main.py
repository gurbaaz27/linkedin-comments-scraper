import shutil
import json
import csv
from utils import *
from datetime import datetime
import zipfile
from io import BytesIO
from flask import Flask, request, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return "<h1>Linkedin Comments Scraper</h1><br>Make post request at /api endpoint"


@app.route("/api", methods=["POST"])
def collect_data():
    req = request.get_json()
    email = req["email"]
    password = req["password"]
    post_url = req["posturl"]
    download_pfp = req["downloadpfp"]
    # email = request.form["email"]
    # password = request.form["password"]
    # post_url = request.form["posturl"]
    # download_pfp = request.form["downloadpfp"]

    with open(
        "config.json",
    ) as f:
        Config = json.load(f)

    unique_suffix = datetime.now().strftime("-%m-%d-%Y--%H-%M")

    csvfilename = Config["filename"] + unique_suffix + ".csv"
    csvfile = open(
        csvfilename,
        "w",
        encoding="utf-8",
    )

    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Profile Picture", "Designation", "Email", "Comment"])

    options = Options()
    options.headless = False
    driver = webdriver.Chrome(
        options=options, executable_path=ChromeDriverManager().install()
    )
    driver.get("https://www.linkedin.com")

    username_element = driver.find_element_by_name(Config["username_name"])
    username_element.send_keys(email)

    password_element = driver.find_element_by_name(Config["password_name"])
    password_element.send_keys(password)

    sign_in_button = driver.find_element_by_xpath(Config["sign_in_button_xpath"])
    sign_in_button.click()

    driver.get(post_url)

    load_more_comments(Config["load_comments_class"], driver)

    comments = driver.find_elements_by_class_name(Config["comment_class"])
    comments = [comment.text.strip() for comment in comments]

    headlines = driver.find_elements_by_class_name(Config["headline_class"])
    headlines = [headline.text.strip() for headline in headlines]

    emails = extract_emails(comments)

    names = driver.find_elements_by_class_name(Config["name_class"])
    names = [name.text.split("\n")[0] for name in names]

    avatars = driver.find_elements_by_class_name(Config["avatar_class"])
    avatars = [
        avatar.find_element_by_tag_name("img").get_attribute("src")
        for avatar in avatars
    ]

    dirname = Config["dirname"] + unique_suffix
    if download_pfp:
        download_avatars(avatars, names, dirname)

    driver.quit()

    write_data2csv(names, avatars, headlines, emails, comments, writer)
    csvfile.close()

    memory_file = BytesIO()

    zipfilename = f"data{unique_suffix}.zip"
    # zipfolder = zipfile.ZipFile(zipfilename, "w", compression=zipfile.ZIP_STORED)

    with zipfile.ZipFile(memory_file, "w") as zf:
        zf.write(csvfilename)
        zf.write(dirname)
        for imgs in os.listdir(dirname):
            zf.write(f"{dirname}/{imgs}")
        zf.close()

    memory_file.seek(0)

    shutil.rmtree(dirname)
    os.remove(csvfilename)

    return send_file(
        memory_file,
        mimetype="application/zip",
        as_attachment=True,
        download_name=zipfilename,
    )


if __name__ == "__main__":
    app.run()
