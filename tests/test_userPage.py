import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from testData.testData import TestData
from utilities.BaseClass import BaseClass


class TestUserPage(BaseClass, TestData):

    @pytest.fixture()
    def get_loginPage(self):
        self.loginPage = LoginPage(self.driver)
        return self.loginPage

    @pytest.fixture()
    def get_HomePage(self):
        self.homePage = HomePage(self.driver)
        return self.homePage

    @pytest.fixture()
    def get_UserPage(self):
        self.userPage = UserPage(self.driver)
        return self.userPage

    def test_validateUserName(self, get_HomePage, get_loginPage, get_UserPage):
        self.loginPage.userNameE().send_keys(TestData.userName)
        self.loginPage.emailE().send_keys(TestData.email)
        self.loginPage.passwordE().send_keys(TestData.password)
        self.loginPage.getLoginCodeBtnE().click()
        time.sleep(3)
        self.loginPage.codeE().send_keys(TestData.loginCode)
        self.loginPage.loginBtnE().click()
        time.sleep(3)
        self.homePage.entityNavigatorE()[0].click()
        self.homePage.searchInputE().send_keys(TestData.userDetails2[1])
        self.homePage.searchBtnE().click()
        time.sleep(1)
        self.homePage.userTableDataE()[5].click()
        self.switchWindow(1)
        time.sleep(3)
        assert self.userPage.userNameE().text == self.userDetails2[0]

    def test_assertBasicActionsList(self, get_UserPage):
        actualBasicActions= []
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        for i in self.userPage.basicActionsListE():
            actualBasicActions.append(i.text)
        assert TestData.expectedBasicActionsMenu == actualBasicActions

    def test_assertMoreActionsList(self, get_UserPage):
        actualMoreActions= []
        self.userPage.moreActionsBtnE().click()
        time.sleep(1)
        for i in self.userPage.moreActionsListE():
            actualMoreActions.append(i.text)
        assert TestData.expectedMoreActionsMenu == actualMoreActions

    def test_changeUserPassword(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[2].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys("1112")
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        assert self.userPage.successMsgE().text == '{"result":true}'
        self.userPage.closeSuccessMsgE().click()

    def test_changeUserSecAnswer(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[4].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys("לוי")
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        assert '{"result":true' in self.userPage.successMsgE().text
        self.userPage.closeSuccessMsgE().click()

    def test_changeUserEmail(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[8].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys("itayzis@walla.co.il")
        self.userPage.actionWinOkBtnE().click()
        time.sleep(2)
        assert self.userPage.successMsgE().text == "Email Changed Successfully"
        assert self.userPage.userDetailsFirstRowE()[1].text == "itayzis@walla.co.il"
        self.userPage.closeSuccessMsgE().click()
        self.logScriptDemo().info("actual message: " + self.userPage.successMsgE().text)
        time.sleep(1)
        self.userPage.closeSuccessMsgE().click()
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[8].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys(TestData.userDetails2[2])
        self.userPage.actionWinOkBtnE().click()
        self.userPage.closeSuccessMsgE().click()

    def test_AsserProfileTypeList(self, get_UserPage):
        actualProfileTypeList = []
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[9].click()
        time.sleep(1)
        self.userPage.actionWinOpenComboE().click()
        for i in self.userPage.actionWinComboE():
            actualProfileTypeList.append(i.text)
        assert TestData.expectedProfileTypeList == actualProfileTypeList
        self.userPage.actionWinOkBtnE().click()

    def test_changeUserProfile(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[9].click()
        time.sleep(1)
        self.userPage.actionWinOpenComboE().click()
        self.userPage.actionWinComboE()[2].click()
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        assert self.userPage.userDetailsSecondRowE()[2].text == 'Profile Type: Business - Exempt'
        self.userPage.closeSuccessMsgE().click()
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[9].click()
        time.sleep(1)
        self.userPage.actionWinOpenComboE().click()
        self.userPage.actionWinComboE()[1].click()
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        self.userPage.closeSuccessMsgE().click()

    def test_changeUserID(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[11].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys("999731334")
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        assert self.userPage.userDetailsFirstRowE()[5].text == "ID Number:999731334"
        self.userPage.closeSuccessMsgE().click()
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[11].click()
        time.sleep(1)
        self.userPage.actionWinUserInputE().send_keys("999525850")
        self.userPage.actionWinOkBtnE().click()
        time.sleep(1)
        self.userPage.closeSuccessMsgE().click()

    def test_exportUserHistory(self, get_UserPage):
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        self.userPage.basicActionsListE()[12].click()
        time.sleep(1)
        self.userPage.actionWinOkBtnE().click()
        time.sleep(2)
        assert self.userPage.successMsgE().text == '{"result":"Success"}'






