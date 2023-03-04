from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class healthrecordspageClass:
    def __init__(self, driver):
         self.driver = driver

    # creating the element locators

         self.LaterbuttonElement = "//*[@id='wzrk-cancel']"
         self.loginButtonElement = "//div[@class='Header_userCircle__3RGRA ']/span"
         self.MobileNumberTextBoxElement = "mobileNumber"
         self.NextButtonElement = "//span[@class='MuiFab-label']/span"
         self.LoginNextButtonElement = "//span[@class='icon-ic_arrow_forward']"
         self.mobnumTextBoxElement = "mobileNumber"
         self.MobTextElement = "//div[@class='jss93']/p"
         self.textofotpelement = "//*[text()='Now type in the OTP sent to you for authentication']"
         self.HomepageElement = "//*[@id='mainContainerCT']/div/div/div[1]/div[1]/div/div/div/div"

         self.vhrLinkElement = "//a[@title='View Health Records']/div[2]/h3"
         self.heightButtonElement = "//div[@id='__next']/div/div[2]/div/div/div/div[2]/ul/li[1]/h6"
         self.clinicalDocsElement = "//div[@id='__next']/div/div[2]/div/div[2]/div/div/div/a/span[2]"
         self.updateHightElement  = "//*[text()='Update Height']"
         self.healthCatElement = "//div[@id='__next']/div/div[2]/div/div[2]/div/div/div[2]/div/h1[1]"
         self.heightElement = "//input[@placeholder='Height' and @type='text']"
         self.updateButtonElement = "//div[@role='presentation']/div[3]/div//div[3]/button/span[1]"
         self.errorMsgElement = "//*[text()='Invalid Input']"
         self.updateTextElement = "//*[@id='__next']/div/div[2]/div/div[1]/div/div[2]/ul/li[1]/span"

   # creating the methods

    def click_Later_button(self):
         Later_button = self.driver.find_element(By.XPATH, self.LaterbuttonElement)
         Later_button.click()
    def click_login_icon(self):
         loginButton = self.driver.find_element(By.XPATH, self.loginButtonElement)
         loginButton.click()
    def enter_mobilenumber_placeholder(self, number):
         MobileNumberTextBox = self.driver.find_element(By.NAME, self.MobileNumberTextBoxElement)
         MobileNumberTextBox.send_keys(number)
    def click_next_button(self):
        NextButton = self.driver.find_element(By.XPATH, self.NextButtonElement)
        NextButton.click()
    def click_login_next_button(self):
        nextButton = self.driver.find_element(By.XPATH, self.LoginNextButtonElement)
        nextButton.click()
    def enter_mobnum_tb(self, MobileNumber):
        MobNumBox = self.driver.find_element(By.NAME, self.MobileNumberTextBoxElement)
        MobNumBox.send_keys(MobileNumber)
    def check_MobileWindow_Text(self):
       MobWindow= self.driver.find_element(By.XPATH, self.MobTextElement).text
       return MobWindow

    def check_otpWindow_Text(self):
       otpWindowText = self.driver.find_element(By.XPATH, self.textofotpelement).text
       return otpWindowText

    def check_User_Name(self):
        usernametext = self.driver.find_element(By.XPATH, self.HomepageElement).text
        return usernametext

    def click_vhr_link(self):
         vhrLink = self.driver.find_element(By.XPATH, self.vhrLinkElement)
         vhrLink.click()

    def healthcat_text(self):
         Health = self.driver.find_element(By.XPATH, self.healthCatElement).text
         return Health

    def click_height_button(self):
         heightButton = self.driver.find_element(By.XPATH, self.heightButtonElement)
         heightButton.click()

    def update_text(self):
         updateheight = self.driver.find_element(By.XPATH, self.updateHightElement).text
         return updateheight

    def enter_height_placeholder(self,height):
        heightnum = self.driver.find_element(By.XPATH, self.heightElement)
        heightnum.send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        heightnum.send_keys(height)

    def click_update_button(self):
        update = self.driver.find_element(By.XPATH, self.updateButtonElement)
        update.click()

    def text_update_data(self):
        update = self.driver.find_element(By.XPATH, self.updateTextElement).text
        return update