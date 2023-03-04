from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewHealthRecordsClass:

    def __init__(self,driver):
         self.driver = driver

         #creating the element locators

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

    def click_clinicaldocuments_link(self):
        clinicalDocuments = self.driver.find_element(By.XPATH, self.clinicalDocsElement)
        clinicalDocuments.click()

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

    def text_error_msg(self):
        errorMsg = self.driver.find_element(By.XPATH, self.errorMsgElement).text
        return errorMsg









