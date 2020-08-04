from time import sleep
from getpass import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

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
            sleep(3.5)
            # 3.5 second sleep works great...you can increase if this time seems too less and program finishes before loading all comments....dont decrease though
            try:
                load_more_button = driver.find_element_by_class_name(load_comments_class)
            except:
                print('>')
                print("All comments have been displayed!")
                break
            print('=',end='',flush=True)
    except:
        print("All comments are displaying already!")

def write_data2csv(names, comments, writer):
    for name,comment in zip(names,comments):
        writer.writerow([name.encode('utf-8'),
                        comment.encode('utf-8')])
        # utf-8 encoding helps to deal with emojis
