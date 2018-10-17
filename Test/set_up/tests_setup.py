from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class SetUpTests(object):

    seconds = 20

    def __init__(self):
        self.browser = webdriver.Chrome(r'K:\!Programowanie\PyCharm\PyWorkspace\mBank_UI_Tests\chromedriver.exe')
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, self.seconds)

    def open_main_page(self):
        browser = self.browser
        browser.get('https://www.google.com')
        return self.Main_Page()

    def tearDown(self):
        browser = self.browser
        browser.quit()
