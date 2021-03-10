from selenium.webdriver.common.by import By

class LoginPage:

    #constructor
    def __init__(self, driver):
        self.driver = driver

    #locators
    userName = (By.ID, "username")
    email = (By.ID, "email")
    password = (By.ID, "password")
    getLoginCodeBtn = (By.XPATH, "//div[@class='form-actions']/button[1]")
    code = (By.ID, "code")
    loginBtn = (By.XPATH, "//button[normalize-space()='Login']")
    errorMsg = (By.XPATH, "//div[@class='alert alert-danger ng-binding']")

    #elements
    def userNameE(self):
        return self.driver.find_element(*LoginPage.userName)

    def emailE(self):
        return self.driver.find_element(*LoginPage.email)

    def passwordE(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginCodeBtnE(self):
        return self.driver.find_element(*LoginPage.getLoginCodeBtn)

    def codeE(self):
        return self.driver.find_element(*LoginPage.code)

    def loginBtnE(self):
        return self.driver.find_element(*LoginPage.loginBtn)

    def errorMsgE(self):
        return self.driver.find_element(*LoginPage.errorMsg)
