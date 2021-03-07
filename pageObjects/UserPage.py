from selenium.webdriver.common.by import By


class UserPage:

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    # locators:
    successMsg = (By.XPATH, "//div[@type='success']/div")
    closeSuccessMsg = (By.XPATH, "//button[@ng-click='close({$event: $event})']")
    userName = (By.XPATH, "//div[@class='col-md-7 text-center']/h3")
    basicActionsBtn = (By.XPATH, "//button[text()='Basic Actions']")
    basicActionsList = (By.XPATH, "//li[@ng-repeat='obj in basicActions']")
    moreActionsBtn = (By.XPATH, "//button[text()='More Actions']")
    moreActionsList = (By.XPATH, "//li[@ng-repeat='obj in moreActions']")

        # action window locators
    actionWinUserInput = (By.XPATH, "//div[@ng-show = 'action.form.f1']/input")
    actionWinMes = (By.XPATH, "//h3[@class ='text-center ng-binding']")
    actionWinOkBtn = (By.XPATH, "//button[@class='btn btn-success']")
    actionWinCancelBtn = (By.XPATH, "//button[@class='btn btn-success']")

    # elements:
    def successMsgE(self):
        return self.driver.find_element(*UserPage.successMsg)

    def closeSuccessMsgE(self):
        return self.driver.find_element(*UserPage.closeSuccessMsg)

    def userNameE(self):
        return self.driver.find_element(*UserPage.userName)

    def basicActionsBtnE(self):
        return self.driver.find_element(*UserPage.basicActionsBtn)

    def basicActionsListE(self):
        return self.driver.find_elements(*UserPage.basicActionsList)

    def moreActionsBtnE(self):
        return self.driver.find_element(*UserPage.moreActionsBtn)

    def moreActionsListE(self):
        return self.driver.find_elements(*UserPage.moreActionsList)

    def actionWinUserInputE(self):
        return self.driver.find_element(*UserPage.actionWinUserInput)

    def actionWinMesE(self):
        return self.driver.find_element(*UserPage.actionWinMes)

    def actionWinOkBtnE(self):
        return self.driver.find_element(*UserPage.actionWinOkBtn)

    def actionWinCancelBtnE(self):
        return self.driver.find_element(*UserPage.actionWinCancelBtn)



