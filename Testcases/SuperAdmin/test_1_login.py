from selenium import webdriver
import unittest
import random
import string
import time
from Pages.Createprojectpage import Createprojectmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login(unittest.TestCase,Createprojectmixin):

    qa_username = 'admin@reverieinc.com'
    qa_username1 = 'admin@reverieincz.com'
    qa_password = 'admin'
    qa_password1 = 'admin1'

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path=cls.Path, options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(cls.Anuvadak_Beta)
        cls.driver.set_window_size(1920 ,1080)

    def test_1_Login_With_Valid_Credentials(self):
        self.Login_With_Valid_Credentials()
    
    def test_2_Login_With_Invalid_Email_Address(self):
        self.Login_With_Invalid_Email_Address()
    
    def test_3_Login_With_Invalid_Password(self):
        self.Login_With_Invalid_Password()
        self.driver.close()
        


    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
        
if __name__ == '__main__':
    unittest.main()