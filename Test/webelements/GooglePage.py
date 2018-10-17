from webium import BasePage
from webium.driver import get_driver


class GooglePage(BasePage):

    def __init__(self):
        super(GooglePage, self).__init__(url="https://www.google.pl")

    def openGooglePage(self):
        page = GooglePage()
        page.open()
        get_driver().maximize_window()
        return GooglePage()

    def dupa(self):
        pass




