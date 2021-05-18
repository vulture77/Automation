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

class Autoschedulermixin:

    def __init__(self):
        print("Create Project")

    def Login_To_Anuvadak_Auto(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.qa_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.qa_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        print("Logged in to Anuvadhak as Super Admin")
    
    def Create_Prabandhak_Project_Translation_Auto(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("QA Test",Keys.ENTER)
        self.driver.find_element_by_xpath("//span[contains(@class,'d-flex flex-row')]//button[2]").click()
        self.driver.find_element_by_name("name").send_keys("Projectx1")
        self.driver.find_element_by_name("baseUrl").send_keys("https://anuvadaktest2.wordpress.com/")
        self.driver.find_element_by_id("language").click()
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_xpath("//label[text()='Base URL']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//h2[text()='Add URLs manually']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[@class='ant-switch']").click()
        self.driver.find_element_by_xpath("//button[text()='Finish']").click()
        time.sleep(120)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        self.driver.find_element_by_link_text("Projectx1").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@role='switch']").click()
        time. sleep(10)
        self.driver.find_element_by_xpath("//button[@role='switch']").click()
        self.driver.find_element_by_xpath("//input[@type='number']").send_keys(Keys.CONTROL + "a", Keys.BACK_SPACE, Keys.ARROW_UP)
        self.driver.find_element_by_xpath("//button[text()='Sync']").click()
        time.sleep(120)
        self.driver.close()

    def Add_Content_Auto(self):
        
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
        self.driver.close()
    
    def Flushcache_and_preview_new_Content_Auto(self):

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
        self.driver.find_element_by_link_text("https://anuvadaktest2.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//input[@value='Close and accept']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//p[text()='Chandan']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//button[@aria-label='Close']").click()
        time.sleep(5400)
    

    def Login_To_Anuvadak_Lsp_Account_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
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
    
    def Login_To_Associate_perform_Translations_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//span[text()='View']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Start Work']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='Agree']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Segment By Source']").send_keys("Chandan",Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[1]").click()
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[1]").send_keys("चंदन",Keys.CONTROL,Keys.ENTER)
        time.sleep(2)
        print("Translations Completed Successfully")
        self.driver.close()

    def Call_Webhook_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//*[text()='Project Overview']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Webhook']").click()
        time.sleep(2)
        print("Webhook Triggered Successfully")
        self.driver.close()
    
    def Preview_Loclization_via_Anuvadak_Auto(self):

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
        self.driver.find_element_by_link_text("https://anuvadaktest2.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//input[@value='Close and accept']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("//p[text()='चंदन']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

    def Add_New_Page_Auto(self):

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
        self.driver.close()


    def Flushcache_and_preview_added_Page_Auto(self):

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
        self.driver.find_element_by_link_text("https://anuvadaktest2.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//input[@value='Close and accept']").click()
        self.driver.find_element_by_link_text("Manager").click()
        self.driver.find_element_by_xpath("//h1[text()='Manager']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//button[@aria-label='Close']").click()
        time.sleep(5400)
        

    def Login_To_Anuvadak_Lsp_Account_Assign_New_Page_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
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
    
    def Login_To_Associate_perform_New_Page_Translations_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//span[text()='View']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Start Work']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='Agree']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search Segment By Source']").send_keys("Manager",Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[1]").click()
        self.driver.find_element_by_xpath("(//div[@class='target-textarea'])[1]").send_keys("मैनेजर",Keys.CONTROL,Keys.ENTER)
        time.sleep(2)
        print("Translations Completed Successfully")
        self.driver.close()

    def Call_Webhook_for_New_Page_Auto(self):
        
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
        self.driver.find_element_by_xpath("//input[@placeholder='Search Project']").send_keys("Anuvadaktest2",Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='Published'])[1]").click()
        self.driver.find_element_by_xpath("//*[text()='Project Overview']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Webhook']").click()
        time.sleep(2)
        print("Webhook Triggered Successfully")
        self.driver.close()
    
    def Preview_Page_Loclization_via_Anuvadak_Auto(self):

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
        self.driver.find_element_by_link_text("https://anuvadaktest2.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//input[@value='Close and accept']").click()
        self.driver.find_element_by_link_text("मैनेजर").click()
        self.driver.find_element_by_xpath("//h1[text()='मैनेजर']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        
    def Delete_Page_Auto(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("usernameOrEmail").send_keys("chandan.m@reverieinc.com")
        self.driver.find_element_by_xpath("//button[text()='Continue']").click()
        self.driver.find_element_by_id("password").send_keys("imwatim@7")
        self.driver.find_element_by_xpath("//button[text()='Log In']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(//button[@title='Toggle menu'])[1]").click()
        self.driver.find_element_by_xpath("//button[text()='Bin']").click()
        time.sleep(2)
        self.driver.close()
    
    def Delete_Content_Auto(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("usernameOrEmail").send_keys("chandan.m@reverieinc.com")
        self.driver.find_element_by_xpath("//button[text()='Continue']").click()
        self.driver.find_element_by_id("password").send_keys("imwatim@7")
        self.driver.find_element_by_xpath("//button[text()='Log In']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(//button[@title='Toggle menu'])[1]").click()
        self.driver.find_element_by_xpath("//button[text()='Bin']").click()
        time.sleep(2)
        self.driver.close()
    
    def Deleteproject_with_TM_Auto(self): 
        
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