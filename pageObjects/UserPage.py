from selenium.webdriver.common.by import By


class UserPage:

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    # locators:
    successMsg = (By.XPATH, "//div[@type='success']/div")
    closeSuccessMsg = (By.XPATH, "//button[@ng-click='close({$event: $event})']")
    userName = (By.XPATH, "//div[@class='col-md-7 text-center']/h3")
    userDetailsFirstRow = (By.XPATH, "//div[@class='panel-body']/div[1]/div/p")
    userDetailsSecondRow = (By.XPATH, "//div[@class='panel-body']/div[2]/div/p")
    basicActionsBtn = (By.XPATH, "//button[text()='Basic Actions']")
    basicActionsList = (By.XPATH, "//li[@ng-repeat='obj in basicActions']")
    moreActionsBtn = (By.XPATH, "//button[text()='More Actions']")
    moreActionsList = (By.XPATH, "//li[@ng-repeat='obj in moreActions']")

        # action window locators
    actionWinUserInput = (By.XPATH, "//div[@ng-show = 'action.form.f1']/input")
    actionWinMes = (By.XPATH, "//h3[@class ='text-center ng-binding']")
    actionWinOkBtn = (By.XPATH, "//button[@class='btn btn-success']")
    actionWinCancelBtn = (By.XPATH, "//button[@class='btn btn-success']")
    actionWinOpenLeftCombo = (By.XPATH, "//select[@ng-model='formData[action.form.f20.key]']")
    actionWinLeftCombo = (By.XPATH, "//select[@ng-model='formData[action.form.f20.key]']/option")
    actionWinOpenRightCombo = (By.XPATH, "//select[@ng-model='formData[action.form.f18.key]']")
    actionWinRightCombo = (By.XPATH, "//select[@ng-model='formData[action.form.f18.key]']/option")

    # elements:
    def successMsgE(self):
        return self.driver.find_element(*UserPage.successMsg)

    def closeSuccessMsgE(self):
        return self.driver.find_element(*UserPage.closeSuccessMsg)

    def userNameE(self):
        return self.driver.find_element(*UserPage.userName)

    def userDetailsFirstRowE(self):
        return self.driver.find_elements(*UserPage.userDetailsFirstRow)

    def userDetailsSecondRowE(self):
        return self.driver.find_elements(*UserPage.userDetailsSecondRow)

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

    def actionWinOpenComboE(self):
        return self.driver.find_element(*UserPage.actionWinOpenLeftCombo)

    def actionWinComboE(self):
        return self.driver.find_elements(*UserPage.actionWinLeftCombo)

    def actionWinOpenRightComboE(self):
        return self.driver.find_element(*UserPage.actionWinOpenRightCombo)

    def actionWinRightComboE(self):
        return self.driver.find_elements(*UserPage.actionWinRightCombo)





