import re
from time import sleep
from getpass import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

def check_post_url(post_url):
    if post_url:
        return post_url
    else:
        print('You haven\'t entered required post_url in Config.py file!')
        choice = input('Do you want to enter url now? (y/N) : ')
        if choice.lower() == 'y':
            post_url = input('Enter url of post: ')
            return post_url
        elif choice.lower() == 'n':
            exit()
        else:
            print('Invalid choice!')
            exit()

def login_details():
    username = input('Enter your email registered in LinkedIn : ')
    password = getpass('Enter your password : ')

    return username, password

def load_more_comments(load_comments_class, driver):
    try:
        load_more_button = driver.find_element_by_class_name(load_comments_class)
        print('<',end='',flush=True)
        while True:
            load_more_button.click()
            sleep(5)
            # 5 second sleep works great for medium-speed net...you can increase if this time seems too less and program finishes before loading all comments....you may decrease till 3 if you have fast internet speed
            try:
                load_more_button = driver.find_element_by_class_name(load_comments_class)
            except:
                print('>')
                print("All comments have been displayed!")
                break
            print('=',end='',flush=True)
    except:
        print("All comments are displaying already!")

def extract_emails(comments):
    emails = []
    for comment in comments:
        email_match = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', comment)
        if email_match:
            emails.append(email_match)
        else:
            emails.append('-')
    return emails

def write_data2csv(names, emails, comments, writer):
    for name,email,comment in zip(names,emails,comments):
        writer.writerow([name,
                        email,
                        comment.encode('utf-8')])
        # utf-8 encoding helps to deal with emojis
