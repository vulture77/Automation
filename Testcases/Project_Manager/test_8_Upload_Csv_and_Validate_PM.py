from selenium import webdriver
import unittest
import random
import string
import time
from PagesPM.CreateprojectpagePM import Createprojectpmmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login(unittest.TestCase,Createprojectpmmixin):

    qa_username = 'qaowner@gmail.com'
    qa_password = 'admin'

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path=cls.Path, options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(cls.Anuvadak_Beta)
        cls.driver.set_window_size(1920 ,1080)
    
    def test_1_Login_Anuvadak(self):
        self.Login_Anuvadak_PM()

    def test_2_Upload_CSV_File(self):
        self.Upload_Csv_file_PM()

    def test_3_Flushcache_and_Validate_Uploded_translation(self):
        self.Flushcache_and_Validate_Uploded_translation_PM()
        self.driver.close()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
        
if __name__ == '__main__':
    unittest.main()