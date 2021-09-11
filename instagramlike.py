from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            'D:\FRIENDS\PYTHON\Projects\pyprojects\chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/accounts/login')
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(
            self.password + Keys.RETURN)
        time.sleep(3)

    def searchByHashtag(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

    def searchByProfile(self, profileName):
        bot = self.bot
        bot.get('https://instagram.com/' + profileName + '/?hl=en')

    def likePosts(self, amount):
        bot = self.bot
        time.sleep(3)
        bot.find_element_by_class_name('v1Nh3').click()
        i = 1
        while(i <= amount):
            time.sleep(3)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name(
                'coreSpriteRightPaginationArrow').click()
            i += 1


entered_username = input('Enter the username')
entered_password = input('Enter the passsword')
insta = Instabot(entered_username, entered_password)
insta.login()

print('1. Search By Hashtag')
print('2. Search By Profile Name')
choice = int(input('Enter The choice'))

if(choice == 1):
    entered_hashtag = input('Enter the hashtag')
    insta.searchByHashtag(entered_hashtag)
if(choice == 2):
    profileName = input('Enter the Profile Name')
    insta.searchByProfile(profileName)

amount = int(input('Enter the amount of posts to be liked'))
insta.likePosts(amount)
