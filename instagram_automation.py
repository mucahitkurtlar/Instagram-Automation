from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

def isInclude(var, list):
    for list_var in list:
        if (list_var == var):
            return True
    return False

def alphaToIntList(str):
    intList = []
    num = 0
    for char in str:
        try:
            if (char == " "):
                num = num / 10
                intList.append(num)
                num = 0
            else:
                num = num + int(char)
                num = num * 10

        except:
            pass
    intList.append(num / 10)
    return intList
class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        #time.sleep(2)
        username_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        username_xpath.clear()
        username_xpath.send_keys(self.username)
        password_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password_xpath.clear()
        password_xpath.send_keys(self.password)
        login_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
        login_xpath.click()

        # username: /html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input
        # password: /html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input
        # login :/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div

    def getFollowingOf(self, username):
        driver = self.driver
        driver.get("https://www.instagram.com/" + username + "/")
        time.sleep(0.25)
        following_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_xpath.click()
        time.sleep(0.25)
        following_list = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        number_of_following_in_list = len(following_list.find_elements_by_css_selector('li'))
        following_list.click()
        action_chain = webdriver.ActionChains(driver)
        while (number_of_following_in_list < 169):
            action_chain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            number_of_following_in_list = len(following_list.find_elements_by_css_selector('li'))
            print(number_of_following_in_list)

        following = []
        for user in following_list.find_elements_by_css_selector('li'):
            user_link = user.find_element_by_css_selector('a').get_attribute('href')
            print(user_link)
            following.append(user_link)
            if (len(following) == max):
                break

        close_xpath = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")
        close_xpath.click()

        return following

    def getFollowing(self):
        driver = self.driver
        following_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_xpath.click()
        time.sleep(0.25)
        following_list = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        number_of_following_in_list = len(following_list.find_elements_by_css_selector('li'))
        following_list.click()
        action_chain = webdriver.ActionChains(driver)
        while (number_of_following_in_list < 169):
            action_chain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            number_of_following_in_list = len(following_list.find_elements_by_css_selector('li'))
            print(number_of_following_in_list)

        following = []
        for user in following_list.find_elements_by_css_selector('li'):
            user_link = user.find_element_by_css_selector('a').get_attribute('href')
            print(user_link)
            following.append(user_link)
            if (len(following) == max):
                break

        close_xpath = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")
        close_xpath.click()

        return following

    def getFollowersOf(self, username):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ username + "/")
        time.sleep(0.25)
        follower_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        follower_xpath.click()
        time.sleep(0.25)
        follower_list = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        number_of_follower_in_list = len(follower_list.find_elements_by_css_selector('li'))
        follower_list.click()
        action_chain = webdriver.ActionChains(driver)
        while (number_of_follower_in_list < 118):
            action_chain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            number_of_follower_in_list = len(follower_list.find_elements_by_css_selector('li'))
            print(number_of_follower_in_list)

        followers = []
        for user in follower_list.find_elements_by_css_selector('li'):
            user_link = user.find_element_by_css_selector('a').get_attribute('href')
            print(user_link)
            followers.append(user_link)
            if (len(followers) == max):
                break

        close_xpath = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")
        close_xpath.click()

        return followers

    def getFollowers(self):
        driver = self.driver
        follower_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        follower_xpath.click()
        time.sleep(0.25)
        follower_list = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        number_of_follower_in_list = len(follower_list.find_elements_by_css_selector('li'))
        follower_list.click()
        action_chain = webdriver.ActionChains(driver)
        while (number_of_follower_in_list < 118):
            action_chain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            number_of_follower_in_list = len(follower_list.find_elements_by_css_selector('li'))
            print(number_of_follower_in_list)

        followers = []
        for user in follower_list.find_elements_by_css_selector('li'):
            user_link = user.find_element_by_css_selector('a').get_attribute('href')
            print(user_link)
            followers.append(user_link)
            if (len(followers) == max):
                break

        close_xpath = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")
        close_xpath.click()

        return followers

    def unfollowUser(self, user_link):
        driver = self.driver
        driver.get(user_link)
        time.sleep(0.25)
        try:
            follow_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/button")
        except:
            follow_xpath = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
        #/html/body/div[1]/section/main/div/header/section/div[1]/button
        #/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button
        follow_xpath.click()
        unfollow_xpath = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]")
        unfollow_xpath.click()

    def detectBetrayers(self):
        followers = self.getFollowersOf(self.username)
        following = self.getFollowing()
        betrayers = []
        print("___BETRAYERS___")
        for user in following:
            if not(isInclude(user, followers)):
                betrayers.append(user)
                print(user)
        return betrayers

    def  unfollowBetrayers(self):
        betrayers = self.detectBetrayers()
        isUserSure = input("You are gonna unfollow all the betrayers. Are you sure? y/n")
        if (isUserSure == "y"):
            for betrayer in betrayers:
                self.unfollowUser(betrayer)
        else:
            print("Abort")

    def manuelUnfollowBetrayers(self):
        betrayers = self.detectBetrayers()
        print("\n\nBetrayers List")
        for i in range(len(betrayers)):
            print(i, betrayers[i])
        selected_betrayers = raw_input("\nEnter number of the user who you want to unfollow(use space for multiple choices):")
        selected_betrayers_list = alphaToIntList(selected_betrayers)
        for betrayer_number in selected_betrayers_list:
            self.unfollowUser(betrayers[betrayer_number])

    def add_comment_to(self, post, comment):
        driver = self.driver
        driver.get(post)
        self.add_comment_to_current_post(comment)

    def add_comment_to_current_post(self, comment):
        driver = self.driver
        comment_area = driver.find_element_by_class_name("Ypffh")
        comment_area.click()
        comment_area = driver.find_element_by_class_name("Ypffh")
        comment_area.send_keys(comment)
        action_chain = webdriver.ActionChains(driver)
        action_chain.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def tag_user_to(self, post, user):
        driver = self.driver
        driver.get(post)
        self.tag_user_to_current_post(user)

    def tag_user_to_current_post(self, user):
        driver = self.driver
        comment_area = driver.find_element_by_class_name("Ypffh")
        comment_area.click()
        comment_area = driver.find_element_by_class_name("Ypffh")
        comment_area.send_keys("@" + user)
        time.sleep(2)
        action_chain = webdriver.ActionChains(driver)
        action_chain.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action_chain.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action_chain.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def tag_random_user_to_current_post(self):
        driver = self.driver
        comment_area = driver.find_element_by_class_name("Ypffh")
        comment_area.click()
        comment_area = driver.find_element_by_class_name("Ypffh")
        rand_str_length = random.randrange(1, 4)
        rand_str = ""
        for i in range(rand_str_length):
            rand_str += random.choice(string.ascii_letters)
        comment_area.send_keys("@" + rand_str)
        time.sleep(2)
        action_chain = webdriver.ActionChains(driver)
        user_list_number = random.randrange(1, 6)
        action_chain.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        for i in range(user_list_number):
            action_chain.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        for i in range(4):
            action_chain.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def tag_random_user_to(self, post):
        driver = self.driver
        driver.get(post)
        self.tag_random_user_to_current_post()


if (__name__ == "__main__"):
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    myBot = Bot(username, password)
    myBot.login()
    time.sleep(5)
    myBot.tag_random_user_to("")
    time.sleep(3)
    for i in range(20):
        for j in range(3):
            myBot.tag_random_user_to_current_post()
            time.sleep(5)
        time.sleep(180)
    time.sleep(6)
    myBot.closeBrowser()
