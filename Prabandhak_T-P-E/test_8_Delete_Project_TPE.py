from selenium import webdriver
import unittest
import time
import random
import string
from PrabandhakPages.PbkTPEfunction import Createpbktpeprojectmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")


class login(unittest.TestCase,Createpbktpeprojectmixin):

    qa_username = 'nandha.kumar@reverieinc.com'
    qa_password = 'admin'

    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
   
   
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Reverie-PC\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe", options=chrome_options)
        #cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Reverie-PC\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://52.172.136.96:3000/")
        cls.driver.set_window_size(1366, 768)
        
    
    def test_1_Delete_Project(self):
        self.Deleteproject_with_TM()  

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
if __name__ == '__main__':
    unittest.main()





