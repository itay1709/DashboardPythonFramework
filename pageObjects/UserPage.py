from selenium.webdriver.common.by import By


class UserPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    basicActionsBtn = (By.XPATH, "//button[text()='Basic Actions']")
    userName = (By.XPATH, "//div[@class='col-md-7 text-center']/h3")

        #set new pin
    passwordInput = (By.XPATH, "//label[text()='pin']/following-sibling::input")

    #elements:
    def basicActionsBtnE(self):
        return self.driver.find_element(*UserPage.basicActionsBtn)

    def userNameE(self):
        return self.driver.find_element(*UserPage.userName)