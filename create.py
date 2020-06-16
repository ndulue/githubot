import sys
import os
from selenium import webdriver
from selenium.webdriver.common.key import keys


path = "xampp/python/git/"

class Gitbot:
    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def createRepo(self):
        bot = self.bot
        bot.get('https://www.github.com/login')
        folderName = str(sys.argv[1])
        os.makedirs(path + str(sys.argv[1]))
        username = bot.find_element_by_xpath("//input[@name='login']")[0]
        password = bot.find_element_by_xpath("//input[@name='password']")[0]
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        bot.find_element_by_xpath("//input[@name='commit']").click()
        bot.get('https://www.github.com/new')
        repo = bot.find_element_by_xpath("//input[@name='repository[name]']")
        repo.send_keys(folderName)
        bot.find_element_by_css_selector("button.first-in-line").submit()

gb = Gitbot('ndulue','')
gb.createRepo()
