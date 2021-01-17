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

class Createpbkprojectmixin:

    def __init__(self):
        print("Create Project")

    def Login_To_Anuvadak(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.qa_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.qa_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        print("Logged in to Anuvadhak as Super Admin")
    
    def Create_Prabandhak_Project_Translation(self):

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
        #self.driver.find_element_by_xpath("//label[text()='Base URL']").click()
        # self.driver.find_element_by_xpath("(//div[text()='Please select'])[2]").click()
        # self.driver.find_element_by_xpath("//li[text()='RealTime']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//h2[text()='Add URLs manually']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//textarea[@inputmode='url']").send_keys("https://anuvadhaqa.wordpress.com/blog")
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[@class='ant-switch']").click()
        self.driver.find_element_by_xpath("//button[text()='Finish']").click()
        time.sleep(60)
        self.driver.close()
        
        # try:
        #     self.elem1 = self.driver.find_element_by_xpath("//td[text()='1']")
        #     if self.elem1.is_displayed():
        #         self.elem1.click()
        #         print("Project Created Successfully")
                
        # except NoSuchElementException:
        #         time.sleep(120)
        #         self.driver.refresh()
        #         self.driver.find_element_by_xpath("(//div[@role='button'])[1]").click()
        #         self.driver.find_element_by_xpath("//td[text()='1']").click()
        #         print("Project Created afte 120 seconds Successfully")
        #         self.driver.close()
          

    def Login_To_Anuvadak_Lsp_Account(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("email").send_keys(self.lsp_username)
        self.driver.find_element_by_name("password").send_keys(self.lsp_password)
        self.driver.find_element_by_xpath("//span[text()='Sign In']").click()
        print("Logged into Prabandhak as Anuvadhak_Lsp")
        time.sleep(10)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//span[text()='My Projects']").click()
        self.driver.find_element_by_xpath("//span[text()='Out-Source Project']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='All']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[@data-value='filesProcessed']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuv",Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='Files processed']").click()
        self.driver.find_element_by_xpath("//*[text()='Project Overview']").click()
        self.driver.find_element_by_xpath("//*[text()='Publish']").click()
        self.driver.find_element_by_xpath("//*[text()='Yes']").click()
        time.sleep(1)
        print("Project Published Successfully")
        self.driver.find_element_by_xpath("//*[text()='Add Team members']").click()
        time.sleep(2)
        self.driver.find_element_by_id("select-targetLanguage").click()
        self.driver.find_element_by_id("select-targetLanguage").click()
        self.driver.find_element_by_css_selector("li[data-value='hindi']").click()
        self.driver.find_element_by_id("select-service").click()
        self.driver.find_element_by_css_selector("li[data-value='translation']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search User']").send_keys("qatran",Keys.ENTER)
        self.driver.find_element_by_id("754a2819-c3f8-4a74-8669-d6e07b896cc2").click()
        self.driver.find_element_by_id("wordCount").send_keys("999")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='Allocate']").click() 
        time.sleep(2)
        print("Project allocated to Associate Successfully")
        self.driver.close()
    
    def Login_To_Associate_perform_Translations(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("email").send_keys(self.lsp_username)
        self.driver.find_element_by_name("password").send_keys(self.lsp_password)
        self.driver.find_element_by_xpath("//span[text()='Sign In']").click()
        print("Logged into Prabandhak as a Translator")
        time.sleep(5)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//span[text()='My Projects']").click()
        self.driver.find_element_by_xpath("//span[text()='Invited Project']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuv",Keys.ENTER)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//span[text()='View']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Start Work']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='Agree']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Segment By Source']").send_keys("Cricket",Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[2]").click()
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[2]").send_keys("क्रिकेट",Keys.CONTROL,Keys.ENTER)
        time.sleep(2)
        print("Translations Completed Successfully")
        self.driver.close()

    def Call_Webhook(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("email").send_keys(self.lsp_username)
        self.driver.find_element_by_name("password").send_keys(self.lsp_password)
        self.driver.find_element_by_xpath("//span[text()='Sign In']").click()
        print("Logged in as Anuvadhak_Lsp")
        time.sleep(5)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//span[text()='My Projects']").click()
        self.driver.find_element_by_xpath("//span[text()='Out-Source Project']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuv",Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//*[text()='Project Overview']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Webhook']").click()
        time.sleep(2)
        print("Webhook Triggered Successfully")
        self.driver.close()
    
    def Preview_Loclization_via_Anuvadak(self):

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
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='क्रिकेट']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
    
    def Deleteproject_with_TM(self): 
        
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