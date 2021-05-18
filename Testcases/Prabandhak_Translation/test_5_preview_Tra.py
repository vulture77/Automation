from selenium import webdriver
import unittest
import random
import string
import time
from PrabandhakPages.Pbktranslationfunc import Createpbkprojectmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login(unittest.TestCase,Createpbkprojectmixin):

    qa_username = 'admin@reverieinc.com'
    qa_password = 'admin'
   

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path=cls.Path, options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(cls.Anuvadak_Beta)
        cls.driver.set_window_size(1920 ,1080)

        
    def test_1_Login(self):
        self.Login_To_Anuvadak()
    
    def test_2_Preview(self):
        self.Preview_Loclization_via_Anuvadak()
        self.driver.close()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
        
if __name__ == '__main__':
    unittest.main()
