'''
###############################################################################
      _____ __    ___   ________ __    _____ _______   ______  __________
     / ___// /   /   | / ____/ //_/   / ___// ____/ | / / __ \/ ____/ __ \
     \__ \/ /   / /| |/ /   / ,<      \__ \/ __/ /  |/ / / / / __/ / /_/ /
    ___/ / /___/ ___ / /___/ /| |    ___/ / /___/ /|  / /_/ / /___/ _, _/
   /____/_____/_/  |_\____/_/ |_|   /____/_____/_/ |_/_____/_____/_/ |_|

###############################################################################

slack_sender.py performs login on slack webapp using Firefox to send messages
without notifying the channel owner of the presence of a new bot or automation

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirements ###############
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[1] Python 3
[2] Firefox
[3] Selenium Python Module (pip3 install selenium)
[4] Geckodriver (https://github.com/mozilla/geckodriver/releases)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Instructions ###############
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Line 55     :  input the file path of geckodriver.exe between the quotes
               EXAMPLE - Firefox(executable_path=r'FILE PATH')
Line 59     :  input the name of your workspace between quotations
               EXAMPLE - .send_keys('slack workspace domain')
Line 61     :  input your email between quotations
               EXAMPLE - .send_keys('email@gmail.com')
Line 62     :  input your password between quotations
               EXAMPLE - .send_keys('password')
Line 72     :  you will need to do some digging for the element id of your
               channel. Easiest way to find this is by looking at the last
               character-string in your URL ONLY AFTER clicking on the channel.
               Should be 9 characters.
               EXAMPLE - https://www.slack.com/sdfshjsdj/<this is what you want>
Line 75     :  input text of your message (supports slack emojis - :sunglasses:)
               EXAMPLE - .send_keys('This is my message')

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Notes ######################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!!IMPORTANT!!:  If you have slow internet, you may need to increase the sleep
timers placed throughout the script to allow for pages to load before continuing
executiong of the rest of the script.

'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'')

def site_login():
    driver.get('https://slack.com/signin')
    driver.find_element_by_id('domain').send_keys('')
    driver.find_element_by_id('submit_team_domain').click()
    driver.find_element_by_id('email').send_keys('')
    driver.find_element_by_id('password').send_keys('')

    time.sleep(1)

    submit = driver.find_element_by_id("signin_btn").click()

    time.sleep(1)

def channel_navigation():
    time.sleep(5)
    driver.find_element_by_id('').click()

def prep_send_msg():
    driver.find_element_by_class_name('ql-editor').send_keys('')
    time.sleep(1)
    driver.find_element_by_id('undefined').send_keys(Keys.RETURN)
    time.sleep(10)

def cleanup():
    driver.quit()

site_login()
channel_navigation()
prep_send_msg()
cleanup()
