'''
###############################################################################
   ______                       __  ___        _____                __
  / ____/________  __  ______  /  |/  /__     / ___/___  ____  ____/ /__  _____
 / / __/ ___/ __ \/ / / / __ \/ /|_/ / _ \    \__ \/ _ \/ __ \/ __  / _ \/ ___/
/ /_/ / /  / /_/ / /_/ / /_/ / /  / /  __/   ___/ /  __/ / / / /_/ /  __/ /
\____/_/   \____/\__,_/ .___/_/  /_/\___/   /____/\___/_/ /_/\__,_/\___/_/
                     /_/
###############################################################################

groupme_sender.py performs login on groupme webapp using Firefox to automate
sending messages to a groupme group discretely

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
Line 57     :  input the file path of geckodriver.exe between the quotes
               EXAMPLE - Firefox(executable_path=r'FILE PATH')
Line 61     :  input your email or phone number between quotations
               EXAMPLE - .send_keys('email@gmail.com')
               EXAMPLE - .send_keys('1234567890')
Line 62     :  input your password between quotations
               EXAMPLE - .send_keys('password')
Line 71     :  input the name of your groupme group between quotations
               EXAMPLE - .find_element_by_xpath("//*[contains(text(), 'GROUP')]").click()
Line 75     :  input text of your message between quotations
               EXAMPLE - .send_keys('This is my message')

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Notes ######################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!!IMPORTANT!!:  If you have slow internet, you may need to increase the sleep
timers placed throughout the script to allow for pages to load before continuing
executiong of the rest of the script.

!!IMPORTANT!!:  In order for flawless login, disable two-step verification
        [1]  Tap the menu button.
        [2]  Tap your profile picture.
        [3]  Toggle Use two-step verification on or off.
'''


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as popup

driver = webdriver.Firefox(executable_path=r'C:\python38\geckodriver.exe')

def site_login():
    driver.get('https://web.groupme.com/signin')
    driver.find_element_by_id('signinUserNameInput').send_keys('')
    driver.find_element_by_id('signinPasswordInput').send_keys('')

    time.sleep(1)

    driver.find_element_by_class_name('btn-success').click()


def channel_navigation():
    time.sleep(5)
    driver.find_element_by_xpath("//*[contains(text(), '')]").click()

def prep_send_msg():
    time.sleep(5)
    driver.find_element_by_class_name('emoji-wysiwyg-editor').send_keys('')
    time.sleep(1)
    driver.find_element_by_class_name('emoji-wysiwyg-editor').send_keys(Keys.RETURN)


def cleanup():
    time.sleep(5)
    driver.quit()


site_login()
channel_navigation()
prep_send_msg()
cleanup()
