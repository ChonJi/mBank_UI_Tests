import unittest

from webium.driver import get_driver

from Test.set_up.tests_setup import SetUpTests
from Test.webelements.GooglePage import GooglePage


class MainPageTest(unittest.TestCase):

    def test_open_main_page(self):

        pass

    if __name__ == "__main__":
        page = GooglePage().openGooglePage()
        get_driver().quit()
        chrome_page = SetUpTests().open_main_page()

    def test_dupa(self):
        # self.chrome_page. -- GÓWNO TAK NIE ZADZIAŁA :D
        pass

