'''
###############################################################################
             _       ____          __       ___
            | |     / / /_  ____ _/ /______/   |  ____  ____
            | | /| / / __ \/ __ `/ __/ ___/ /| | / __ \/ __ \
            | |/ |/ / / / / /_/ / /_(__  ) ___ |/ /_/ / /_/ /
            |__/|__/_/ /_/\__,_/\__/____/_/  |_/ .___/ .___/
               _____                __        /_/   /_/
              / ___/___  ____  ____/ /__  _____
              \__ \/ _ \/ __ \/ __  / _ \/ ___/
             ___/ /  __/ / / / /_/ /  __/ /
            /____/\___/_/ /_/\__,_/\___/_/

###############################################################################

groupme_sender.py performs login on groupme webapp using Firefox to automate
sending messages to a groupme group discretely

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirements ###############
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[1] Python 3
[2] WhatsApp Desktop
[3] PyAutoGUI Python Module (pip3 install pyautogui)

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
!!IMPORTANT!!:  WhatsApp (Desktop) must be open and authenticated on the screen
for this script to work
'''
import pyautogui as pag

def gather_display_info():
    screenWidth, screenHeight = pag.size()
    currentMouseX, currentMouseY = pag.position()

def prep_send_msg():
    search = pag.locateOnScreen('Search or start new chat')
    search.click()
    search.typewrite('J')




prep_send_msg():
