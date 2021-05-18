from selenium import webdriver
import unittest
import time
import random
import string
from Pages.Createprojectsyncpage import Createprojecsynctmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")


class login(unittest.TestCase,Createprojecsynctmixin):

    translator_username = 'qatranslator@gmail.com'
    translator_password = 'Rev@123'

    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
   

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe", options=chrome_options)
        #cls.driver = webdriver.Chrome(executable_path="C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://wordpress.com/posts/anuvadhaqa.wordpress.com")
        cls.driver.set_window_size(1920, 1080)
        
    def test_1_Remove_Content(self):
        self.Delete_Content()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
if __name__ == '__main__':
    unittest.main()