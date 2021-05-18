from selenium import webdriver
import unittest
import random
import string
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Createprojecsync1tmixin:

    def __init__(self):
        print("Create Project")

    def Login_Anuvadak(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.qa_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.qa_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        print("Logged in to Anuvadhak")
        time.sleep(2)

    def Projectcreationreal(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("QA Test",Keys.ENTER)
        self.driver.find_element_by_xpath("//span[contains(@class,'d-flex flex-row')]//button[2]").click()
        self.driver.find_element_by_name("name").send_keys("Projectx1")
        self.driver.find_element_by_name("baseUrl").send_keys("https://anuvadhaqa.wordpress.com/")
        self.driver.find_element_by_id("language").click()
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_xpath("//label[text()='Base URL']").click()
        # self.driver.find_element_by_xpath("(//div[text()='Please select'])[2]").click()
        # self.driver.find_element_by_xpath("//li[text()='RealTime']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        #self.driver.find_element_by_xpath("//textarea[@inputmode='url']").send_keys("https://anuvadhaqa.wordpress.com/")
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[text()='Finish']").click()
        time.sleep(60)
        self.driver.close()

        # try:
        #     self.elem1 = self.driver.find_element_by_xpath("//td[text()='100']")
        #     if self.elem1.is_displayed():
        #         self.elem1.click()
        #         print("Project Created Successfully")
                
        # except NoSuchElementException:
        #         time.sleep(120)
        #         self.driver.refresh()
        #         self.driver.find_element_by_xpath("//td[text()='100']").click()
        #         print("Project Created afte 120 seconds Successfully")
        #         self.driver.close()

    def Add_Content(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("usernameOrEmail").send_keys("chandan.m@reverieinc.com")
        self.driver.find_element_by_xpath("//button[text()='Continue']").click()
        self.driver.find_element_by_id("password").send_keys("imwatim@7")
        self.driver.find_element_by_xpath("//button[text()='Log In']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(//li[@class='section-nav-tab']//a)[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button[@title='Toggle menu'])[1]").click()
        self.driver.find_element_by_xpath("//button[text()='Restore']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Drafts']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button[@title='Toggle menu'])[1]").click()
        self.driver.find_element_by_xpath("//button[text()='Publish']").click()
        time.sleep(5)
        time.sleep(320)
        self.driver.close()
    

    def Flushcache_and_preview_added_Page(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_link_text("Projectx1").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_xpath("(//tbody/tr[4]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_link_text("संपर्क करें").click()
        #self.driver.find_element_by_xpath("//h1[text()='संपर्क करें']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()


    def Delete_Content(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("usernameOrEmail").send_keys("chandan.m@reverieinc.com")
        self.driver.find_element_by_xpath("//button[text()='Continue']").click()
        self.driver.find_element_by_id("password").send_keys("imwatim@7")
        self.driver.find_element_by_xpath("//button[text()='Log In']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(//button[@title='Toggle menu'])[1]").click()
        self.driver.find_element_by_xpath("//button[text()='Bin']").click()
        time.sleep(2)
        time.sleep(320)
        self.driver.close()
    
    def Flushcache_and_preview_Removed_Page(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_link_text("Projectx1").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_xpath("(//tbody/tr[4]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        try:
            self.elem = self.driver.find_element_by_link_text("संपर्क करें")
            if self.elem.is_displayed():
                self.elem.click()
                print("Element Still Present")
                raise Exception

        except NoSuchElementException:
                print("Element Removed successfully")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

    def Deleteproject(self): 
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_xpath("(//tbody/tr[4]/td[5]/span[1]//*[local-name()='svg'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-sm']").click()
        time.sleep(1)
        self.driver.find_element_by_id("projectName").send_keys("Projectx1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='Delete TM']").click()
        time.sleep(3)
        print("Deleted Project Successfully")
        self.driver.close()

    