import time
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from testData.testData import TestData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass, TestData):

    @pytest.fixture()
    def get_loginPage(self):
        self.loginPage = LoginPage(self.driver)
        return self.loginPage

    @pytest.fixture()
    def get_HomePage(self):
        self.homePage = HomePage(self.driver)
        return self.homePage

    def test_validateUpperNavigator(self, get_loginPage, get_HomePage):
        log = self.logScriptDemo()
        actualUpperNavigator = []
        self.loginPage.userNameE().send_keys(TestData.userName)
        self.loginPage.emailE().send_keys(TestData.email)
        self.loginPage.passwordE().send_keys(TestData.password)
        self.loginPage.getLoginCodeBtnE().click()
        time.sleep(3)
        self.loginPage.codeE().send_keys(TestData.loginCode)
        self.loginPage.loginBtnE().click()
        #self.screenShot()
        time.sleep(3)
        for i in self.homePage.upperNavigatorE():
            actualUpperNavigator.append(i.text)
        assert actualUpperNavigator == TestData.expectedUpperNavigator
        log.info("{} {}".format("expected: ", TestData.expectedUpperNavigator))


    def test_validateEntityNavigator(self, get_HomePage):
        actualEntityNavigator = []
        for i in self.homePage.entityNavigatorE():
            actualEntityNavigator.append(i.text)
        assert actualEntityNavigator == TestData.expectedEntityNavigator

    def test_validateUserSubMenu(self, get_HomePage):
        actualSubMenu = []
        for i in self.homePage.userSubMenuE():
            actualSubMenu.append(i.text)
        assert actualSubMenu == TestData.expectedUserSubMenu

    def test_validateGroupSubMenu(self, get_HomePage):
        actualSubMenu = []
        self.homePage.entityNavigatorE()[1].click()
        for i in self.homePage.groupSubMenuE():
            actualSubMenu.append(i.text)
        assert actualSubMenu == TestData.expectedGroupSubMenu

    def test_validateTransactionSubMenu(self, get_HomePage):
        actualSubMenu = []
        self.homePage.entityNavigatorE()[2].click()
        for i in self.homePage.transactionSubMenuE():
            actualSubMenu.append(i.text)
        assert actualSubMenu == TestData.expectedTransactionSubMenu

    def test_validatePofSubMenu(self, get_HomePage):
        actualSubMenu = []
        self.homePage.entityNavigatorE()[3].click()
        for i in self.homePage.pofSubMenuE():
            actualSubMenu.append(i.text)
        assert actualSubMenu == TestData.expectedPofSubMenu

    def test_validateCardSubMenu(self, get_HomePage):
        actualSubMenu = []
        self.homePage.entityNavigatorE()[4].click()
        for i in self.homePage.cardSubMenuE():
            actualSubMenu.append(i.text)
        assert actualSubMenu == TestData.expectedCardSubMenu

    def test_validatePhoneSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[0].click()
        self.homePage.searchInputE().send_keys(TestData.userDetails1[1])
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.userTableDataE()[1].text == TestData.userDetails1[1]

    def test_validateEmailSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[0].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys(TestData.userDetails2[2])
        self.homePage.userSubMenuE()[1].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.userTableDataE()[2].text == TestData.userDetails2[2]


    def test_validateNameSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[0].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys(TestData.userDetails1[0])
        self.homePage.userSubMenuE()[2].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.userTableDataE()[0].text == TestData.userDetails1[0]

    def test_validateUidSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[0].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys(TestData.userDetails2[3])
        self.homePage.userSubMenuE()[3].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.userTableDataE()[3].text == TestData.userDetails2[3]

    def test_validateGroupIDSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[1].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys(TestData.groupDetails1[8])
        self.homePage.groupSubMenuE()[4].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.groupTableDataE()[8].text == TestData.groupDetails1[8]
        '''
        for i in self.homePage.groupTableDataE():
            actualGroupData.append(i.text)
            num = num - 1
            if num == 1:
                break
        assert actualGroupData == TestData.groupDetails1
        '''
    def test_validateGroupNameSearchData(self, get_HomePage):
        num = 10
        actualGroupData = []
        self.homePage.entityNavigatorE()[1].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys(TestData.groupDetails1[0])
        self.homePage.groupSubMenuE()[1].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.groupTableDataE()[0].text == TestData.groupDetails1[0]

    def test_validateParmxSearchData(self, get_HomePage):
        self.homePage.entityNavigatorE()[2].click()
        self.homePage.searchInputE().clear()
        self.homePage.searchInputE().send_keys("00a6c32f7283cc399bb")
        self.homePage.transactionSubMenuE()[4].click()
        self.homePage.searchBtnE().click()
        time.sleep(1)
        assert self.homePage.transactionTableDataE()[14].text == "00a6c32f7283cc399bb"

