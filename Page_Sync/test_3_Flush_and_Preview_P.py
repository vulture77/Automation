from selenium import webdriver
import unittest
import time
import random
import string
from Pages.Createprojectsyncpage1 import Createprojecsync1tmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")


class login(unittest.TestCase,Createprojecsync1tmixin):

    qa_username = 'admin@reverieinc.com'
    #qa_username = 'qa@reverieinc.com'
    qa_password = 'admin'
    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe", options=chrome_options)
        #cls.driver = webdriver.Chrome("C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://qa-dashboard.reverieinc.com/")
        cls.driver.set_window_size(1920, 1080)
        
    def test_1_Login_to_Anuvadak(self):
        self.Login_Anuvadak()

    def test_2_Cache_flush_and_Preview(self):
        self.Flushcache_and_preview_added_Page()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
if __name__ == '__main__':
    unittest.main()