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

chrome_options = Options()  
chrome_options.add_argument("--headless")


class Createprojectpmmixin:

    chrome_options = Options()  
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    Path = "chrome/chromedriver.exe"
    Anuvadak_Beta = "https://qa-dashboard.reverieinc.com/"
    Prabandhak_Beta = "http://beta.prabandhak.in/"


    def __init__(self):
        print("Create Project PM")

    
    def Login_Anuvadak_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("normal_login_email").send_keys(self.qa_username)
        self.driver.find_element_by_id("normal_login_password").send_keys(self.qa_password)
        self.driver.find_element_by_xpath("//text()[.='Log in']/ancestor::button[1]").click()
        print("Logged into Anuvadhak Successfully")
        time.sleep(2)
    
    
    def Create_Admin_User_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Add new user']").click()
        self.driver.find_element_by_name("firstName").send_keys("QA")
        self.driver.find_element_by_name("lastName").send_keys("Tester")
        self.driver.find_element_by_name("email").send_keys("tester123@gmail.com")
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-dropdown-trigger']").click()
        self.driver.find_element_by_xpath("//li[text()='Automation_Owner']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[text()='save & exit']").click()
        print("Organziation Created Successfully")
        time.sleep(2)
  


    def Edit_Admin_Users_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("QA Tester",Keys.ENTER)
        self.driver.find_element_by_xpath("//span[contains(@class,'d-flex flex-row')]//button[1]").click()
        self.driver.find_element_by_id("edit_user_fname").send_keys("1")
        self.driver.find_element_by_id("edit_user_lname").send_keys("2")
        self.driver.find_element_by_id("edit_user_email").send_keys("m")
        self.driver.find_element_by_id("admin-finish-button").click()
        time.sleep(2)
        print("Admin User Modified Successfully")
        

   

    def Delete_Admin_User_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("QA1 Tester2",Keys.ENTER)
        self.driver.find_element_by_xpath("//span[contains(@class,'d-flex flex-row')]//button[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ant-popover ant-popover-placement-top']//button[2]").click()
        time.sleep(2)
        print("Admin User Deleted Successfully")


    def Create_NonJS_Project_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Users']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("Test Owner",Keys.ENTER)
        self.driver.find_element_by_xpath("//span[contains(@class,'d-flex flex-row')]//button[2]").click()
        self.driver.find_element_by_name("name").send_keys("Owner_Project")
        self.driver.find_element_by_name("baseUrl").send_keys("https://anuvadhaqa.wordpress.com/")
        self.driver.find_element_by_id("language").click()
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//textarea[@inputmode='url']").send_keys("https://anuvadhaqa.wordpress.com/blog")
        self.driver.find_element_by_xpath("//button[text()='Next']").click()
        self.driver.find_element_by_xpath("//button[text()='Finish']").click()
        time.sleep(60)

        
        # try:
        #     self.elem1 = self.driver.find_element_by_xpath("(//div[text()='100%'])[4]")
        #     if self.elem1.is_displayed():
        #         self.elem1.click()
        #         print("Project Created Successfully")
                
        # except NoSuchElementException:
        #         time.sleep(60)
        #         self.driver.refresh()
        #         self.driver.find_element_by_xpath("(//div[text()='100%'])[4]").click()
        #         print("Project Created afte 120 seconds Successfully")
        #         self.driver.close()

    def Preview_Localization_PM(self):        
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        #self.driver.find_element_by_link_text("क्रिकेट").click()
        time.sleep(20)
        self.driver.find_element_by_xpath("//h1[text()='क्रिकेट']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def Add_Exclusion_PM(self):   
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='Add field'])[2]").click()
        self.driver.find_element_by_id("AddNoTrans_url").send_keys("https://anuvadhaqa.wordpress.com/blog")
        self.driver.find_element_by_id("AddNoTrans_element").send_keys(".entry-header.responsive-max-width", Keys.ENTER)
        self.driver.find_element_by_xpath("//button[text()='Add customization']").click()
        print("Added Exclusion Section Successfully")
        time.sleep(2)

    def Flushcache_and_Validate_added_Exclusion_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='Cricket']").click()
        print("Previewed Excluded Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def Remove_Exclusion_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='View all entries'])[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//i[@class='fa fa-ellipsis-v c-pointer']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//p[text()='Delete']").click()
    
    def Flushcache_and_Validate_Removed_Exclusion_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//i[contains(@class,'fa fa-arrow-left')]").click()
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='क्रिकेट']").click()
        print("Previewed Excluded Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    
    def Upload_Csv_file_PM(self):   
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='Upload']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='ant-btn']/following-sibling::button[1]").click()
        self.driver.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\taan\\Desktop\\Auto\\Fileformats\\File.csv")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='ant-btn']/following-sibling::button[1]").click()
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn w-25')]").click()
        self.driver.find_element_by_xpath("//button[@class='ant-modal-close']//span[1]").click()
        print("Uploaded Translations via CSV-file Successfully")
        time.sleep(2)
    
    def Flushcache_and_Validate_Uploded_translation_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_link_text("चंदन").click()
        print("Previewed Excluded Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    
    
    def Add_Custom_Fontsize_PM(self):   
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='Add field'])[1]").click()
        self.driver.find_element_by_name("url").send_keys("https://anuvadhaqa.wordpress.com/blog")
        self.driver.find_element_by_name("element").send_keys(".has-text-align-center.has-small-font-size")
        self.driver.find_element_by_name("fontsize").send_keys("3rem")
        self.driver.find_element_by_xpath("//div[text()='please Select']").click()
        self.driver.find_element_by_xpath("//li[text()='Windows']").click()
        self.driver.find_element_by_xpath("(//div[text()='please Select'])[2]").click()
        self.driver.find_element_by_xpath("//li[text()='load']").click()
        self.driver.find_element_by_id("language").click()
        self.driver.find_element_by_xpath("//li[text()='hindi']").click()
        self.driver.find_element_by_xpath("//button[text()='Add customization']").click()
        print("Added FontSize Section Successfully")
    
    def Flushcache_and_Validate_Added_Size_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//input[@value='Close and accept']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("[style='font-size: 3rem;']").click()
        print("Previewed Custom Fontsize successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
    
    def Remove_Custom_Fontsize_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Translation']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//span[text()='View all entries'])[1]").click()
        self.driver.find_element_by_xpath("//i[@class='fa fa-ellipsis-v c-pointer']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//p[text()='Delete']").click()
        print("Removed FontSize Section Successfully")

    def Flushcache_and_Validate_Removed_Size_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//i[contains(@class,'fa fa-arrow-left')]").click()
        self.driver.find_element_by_xpath("//div[text()='Settings']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Flush Cache now']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='Select all']").click()
        self.driver.find_element_by_id("all-lang-cache").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='क्रिकेट']").click()
        time.sleep(10)

        try:
            self.elem = self.driver.find_element_by_css_selector("[style='font-size: 3rem;']")
            if self.elem.is_displayed():
                self.elem.click()
                print("Element Still Present")
        except NoSuchElementException:
                print("Element Removed successfully")

        print("Verified Deleted Fontsize on Preview successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        

    def Deleteproject_PM(self): 
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-sm']").click()
        time.sleep(1)
        self.driver.find_element_by_id("projectName").send_keys("Owner_Project")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='Delete TM']").click()
        time.sleep(3)
        print("Deleted Project Successfully")
        

    def Add_New_URL_and_validate_Preview_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_link_text("Owner_Project").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Scope']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter your URL']").send_keys("https://anuvadhaqa.wordpress.com/contact/")
        self.driver.find_element_by_xpath("//button[text()='Add to scope']").click()
        time.sleep(60)
        print("Added New URL to an Existing Project Successfully")

    def Preview_Newly_Added_URL_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//li[text()=' Projects']").click()
        time.sleep(5)
        self.driver.find_element_by_name("search").send_keys("Owner_Project", Keys.ENTER)
        self.driver.find_element_by_xpath("(//tbody/tr[1]/td[5]/span[1]//*[local-name()='svg'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/contact").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='संपर्क करें']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        

    def Create_Complete_website_Project_PM(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[@title='Filter menu']").click()
        self.driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("QA Test",Keys.ENTER)
        self.driver.find_element_by_xpath("//td[@class='ant-table-selection-column']//label[1]").click()
        self.driver.find_element_by_css_selector("button[id='create-user']").click()
        self.driver.find_element_by_id("AddPrject_name").send_keys("Owner_Project")
        self.driver.find_element_by_name("baseUrl").send_keys("https://anuvadhaqa.wordpress.com/")
        self.driver.find_element_by_id("AddPrject_language").click()
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_xpath("//label[text()='Base URL']").click()
        self.driver.find_element_by_xpath("(//input[@class='c-pointer'])[2]").click()
        time.sleep(30)
        self.driver.find_element_by_xpath("//i[@class='fas fa-external-link-alt']").click()
        self.driver.refresh()
        #self.driver.find_element_by_xpath("//td[text()='100']").click()
        print("Project Created Successfully")
        
    
    def Validate_Complete_Website_Localization_PM(self):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("(//div[@role='button'])[1]").click()
        #self.driver.find_element_by_xpath("//td[text()='2']").click()
        self.driver.find_element_by_xpath("//button[@class='c-pointer loc-preview-btn']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-dropdown-trigger')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='hindi']").click()
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com/blog").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//h1[text()='क्रिकेट']").click()
        print("Previewed Section successfully")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_link_text("https://anuvadhaqa.wordpress.com").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_link_text("अनुवाधाक").click()