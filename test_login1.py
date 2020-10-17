from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")


class login(unittest.TestCase):

    fre_username = 'tushar.jawa@reverieinc.com'
    fre1_username = 'tushar.jawa@3reverieinc.com'
    fre_password = 'admin'
    fre1_password = 'admin2'

    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
   

    @classmethod
    def setUpClass(cls):

        #cls.driver = webdriver.Chrome(executable_path="Path\\chrome\\chromedriver.exe", options=chrome_options)
        #cls.driver = webdriver.Chrome(executable_path="C:\\Users\\taan\\Desktop\\pp\\Drivers\\chrome\\chromedriver")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://52.172.136.96:3000/")
        cls.driver.set_window_size(1920, 1080)
        
    def test_1__________Login_Valid_Credentials(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.fre_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.fre_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='Projects']").click()
        self.driver.back()
        print("Logged in to Anuvadhak")
        
    
    def test_2__________Login_Invalid_Email(self):

        time.sleep(2)
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.fre1_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.fre_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        self.driver.find_element_by_xpath("//*[text()='Email or password is incorrect']").click()
        print("Invalid Email")
    
    def test_3__________Login_Invalid_Password(self):

        time.sleep(2)
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.fre_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.fre1_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        # try:
        self.driver.find_element_by_xpath("//*[text()='Email or password is incorrect']").click()
        print("Invalid Password")
        self.driver.close()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
if __name__ == '__main__':
    unittest.main()
