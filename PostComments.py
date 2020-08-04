import Config           # Own module imports
from Utils import *

from time import time       # Other imports
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

if Config.post_url:
    pass
else:
    print('Please enter required post_url in Config.py file!')
    exit()

##### Writer csv
writer = csv.writer(open(Config.file_name, 'w'))
writer.writerow(['Name','Comment'])

linkedin_username, linkedin_password = login_details()

start = time()       # Starting time

##### Selenium Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')

username = driver.find_element_by_name('session_key')
username.send_keys(linkedin_username)
sleep(0.5)

password = driver.find_element_by_name('session_password')
password.send_keys(linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(0.5)

driver.get(Config.post_url)
sleep(3)

print('Loading comments :', end=' ', flush=True)
load_more_comments(Config.load_comments_class, driver)

#comments = driver.find_elements_by_xpath('//span[@class="ember-view"]')
# this is bad because in case of comments with mentions or tags, it doesnt work
comments = driver.find_elements_by_class_name(Config.comment_class)
comments = [comment.text.strip() for comment in comments]

names = driver.find_elements_by_class_name(Config.name_class)
names = [name.text.split('\n')[0] for name in names]

# print(comments[:10])
# print(names[:10])

write_data2csv(names, comments, writer)

end = time()       # Finishing Time
time_spent = end-start # Time taken by script

print('Linkedin post comments scraping done in: %.2f minutes (%d seconds)' % (((time_spent)/60),(time_spent)))

driver.quit()
