import Config           # Own module imports
from Utils import *

from time import time       # Other imports
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

post_url = check_post_url(Config.post_url)

##### Writer csv
writer = csv.writer(open(Config.file_name, 'w'))
writer.writerow(['Name','Email','Comment'])

linkedin_username, linkedin_password = login_details()

start = time()       # Starting time
print('Initiating the process....')
##### Selenium Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')

username = driver.find_element_by_name(Config.username_name)
username.send_keys(linkedin_username)
sleep(0.5)

password = driver.find_element_by_name(Config.password_name)
password.send_keys(linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(0.5)

driver.get(post_url)
sleep(3)

print('Loading comments :', end=' ', flush=True)
load_more_comments(Config.load_comments_class, driver)

#comments = driver.find_elements_by_xpath('//span[@class="ember-view"]')
# this is bad because in case of comments with mentions or tags, it doesnt work
comments = driver.find_elements_by_class_name(Config.comment_class)
comments = [comment.text.strip() for comment in comments]

emails = extract_emails(comments)

names = driver.find_elements_by_class_name(Config.name_class)
names = [name.text.split('\n')[0] for name in names]

# print(comments[:10])
# print(names[:10])
# print(emails[:10])

write_data2csv(names, emails, comments, writer)

end = time()       # Finishing Time
time_spent = end-start # Time taken by script

print('Linkedin post comments scraped in: %.2f minutes (%d seconds)' % (((time_spent)/60),(time_spent)))

driver.quit()
