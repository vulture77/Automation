from selenium import webdriver
import unittest
import time
import random
import string
from PrabandhakPages.Pbktranslationfunc import Createpbkprojectmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login(unittest.TestCase,Createpbkprojectmixin):

    lsp_username = 'qatranslator@gmail.com'
    lsp_password = 'Rev@123'
   

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path=cls.Path, options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(cls.Prabandhak_Beta)
        cls.driver.set_window_size(1920 ,1080)
        
    
    def test_1_Associate_Translate(self):
        self.Login_To_Associate_perform_Translations()  
        self.driver.close()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
if __name__ == '__main__':
    unittest.main()





