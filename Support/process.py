from selenium import webdriver
from configparser import ConfigParser
import time
import os


class WebAutomation():

    def __init__(self):

        #config file read
        print('Read the config')
        file = "Support/config.ini"
        self.config = ConfigParser()
        self.config.read(file)


        #web driver
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C:\\Users\\Tharusha\\AppData\\Local\\Google\\Chrome\\User Data')  # Path to your chrome profile
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\Tharusha\\Downloads\\New folder (11)\\chromedriver.exe' , chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def Create_directory(self):
        config = self.config

        try:
            if not os.path.exists('Output_files\\testfile'):
                os.mkdir('Output_files\\testfile')



            return'pass'

        except:



            return'fail'



    def Wfm_login(self):
        driver= self.driver
        config = self.config

        try:

            #login
            driver.get("https://www.workflowmax.com")
            login = driver.find_element_by_xpath("//header/div[1]/div[1]/a[1]")
            login.click()
            print("click login btn")

            E_type =driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[2]")
            time.sleep(5)
            E_type.clear()
            E_type.send_keys(config['account']['mail'])
            print("type email")

            p_type = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]")
            time.sleep(2)
            p_type.clear()
            p_type.send_keys(config['account']['password'])

            L_click = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
            time.sleep(2)
            L_click.click()

            #Authentication
            Authentication_btn = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
            time.sleep(2)
            Authentication_btn.click()

            #security_qestions
            security_qestions_btn = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
            security_qestions_btn.click()

            time.sleep(7)
            print("stat Q1")

            #Q1
            if str(driver.find_element_by_xpath('//*[@id="auth-splashpage"]/div/div/form/div[1]/label').text) == str(config['Questions']['1']):
                Q1 = str(['Answers']['1'])
            elif str(driver.find_element_by_xpath('//*[@id="auth-splashpage"]/div/div/form/div[1]/label').text) == str(config['Questions']['2']):
                Q1 = str(config['Answers']['2'])
            else:
                Q1 = str(config['Answers']['3'])

            if str(driver.find_element_by_xpath('//*[@id="auth-splashpage"]/div/div/form/div[2]/label').text) == str(config['Questions']['1']):
                Q2 = str(config['Answers']['1'])
            elif str(driver.find_element_by_xpath('//*[@id="auth-splashpage"]/div/div/form/div[2]/label').text) == str(config['Questions']['2']):
                Q2 = str(config['Answers']['2'])
            else:
                Q2 = str(config['Answers']['3'])


            print (Q1)
            A_type1 = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
            A_type1.send_keys(Q1)

            print (Q2)
            A_type2 = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]')
            A_type2.send_keys(Q2)

            time.sleep(2)

            confrim_btn =driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]')
            confrim_btn.click()

            time.sleep(5)






            return 'Pass'
        except:
            return 'Fail'
            print("fail")

    def NavigateTo_neoSuper(self):
        driver = self.driver

        try:
            print("naviagte to neoSuper")
            driver.get("https://my.workflowmax.com/portal")
            time.sleep(3)

            connect_btn = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/button[1]")
            connect_btn.click()
            time.sleep(5)

            Report_btn = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/div[1]/ol[1]/li[5]/button[1]")
            Report_btn.click()
            time.sleep(3)

            ReportBuilder_btn = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/div[1]/ol[1]/li[5]/div[1]/div[2]/div[1]/ol[1]/li[2]/a[1]")
            ReportBuilder_btn.click()
            time.sleep(3)

            custom_btn = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[2]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]")
            custom_btn.click()
            time.sleep(3)

            system_download_btn = driver.find_element_by_partial_link_text("Downtime report")
            system_download_btn.click()














            return'pass'
        except:

            return 'Fail'

    def File_download(self):

        try:



            return 'pass'
        except:
            return 'Fail'


