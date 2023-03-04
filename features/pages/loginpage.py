from selenium.webdriver.common.by import By

class LoginPageClass:
    def __init__(self, driver):
         self.driver = driver

    # creating the element locators

         self.Laterbutton = "//*[@id='wzrk-cancel']"
         self.loginButtonElement = "//div[@class='Header_userCircle__3RGRA ']/span"
         self.MobileNumberTextBoxElement = "mobileNumber"
         self.NextButtonElement = "//span[@class='MuiFab-label']/span"
         self.LoginNextButtonElement = "//span[@class='icon-ic_arrow_forward']"
         self.mobnumTextBox = "mobileNumber"
         self.MobText = "//div[@class='jss93']/p"
         self.textofotpelement = "//*[text()='Now type in the OTP sent to you for authentication']"
         self.HomepageElement = "//*[@id='mainContainerCT']/div/div/div[1]/div[1]/div/div/div/div"

   # creating the methods

    def click_Later_button(self):
         Later_button = self.driver.find_element(By.XPATH, self.Laterbutton)
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
        LoginNextButton = self.driver.find_element(By.XPATH, self.LoginNextButtonElement)
        LoginNextButton.click()
    def enter_mobnum_tb(self, MobileNumber):
        MobNumTextBox = self.driver.find_element(By.NAME, self.MobileNumberTextBoxElement)
        MobNumTextBox.send_keys(MobileNumber)
    def check_MobileWindow_Text(self):
       MobWindowText = self.driver.find_element(By.XPATH, self.MobText).text
       return MobWindowText

    def check_otpWindow_Text(self):
       otpWindowText = self.driver.find_element(By.XPATH, self.textofotpelement).text
       return otpWindowText

    def check_User_Name(self):
        usernametext = self.driver.find_element(By.XPATH, self.HomepageElement).text
        return usernametext

