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
        self.homePage.searchInputE().send_keys(TestData.userDetails1[1])
        self.homePage.searchBtnE().click()
        time.sleep(1)
        self.homePage.userTableDataE()[5].click()
        self.switchWindow(1)
        time.sleep(3)
        assert self.userPage.userNameE().text == self.userDetails1[0]

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

    def test_assertBasicActionsList(self, get_UserPage):
        actualBasicActions= []
        self.userPage.basicActionsBtnE().click()
        time.sleep(1)
        for i in self.userPage.basicActionsListE():
            actualBasicActions.append(i.text)
        assert TestData.expectedBasicActionsMenu == actualBasicActions

