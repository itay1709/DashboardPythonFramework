import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):

    @pytest.fixture()
    def get_loginPage(self):
        self.loginPage = LoginPage(self.driver)
        return self.loginPage

    def test_validateLoginDataDriven(self, get_loginPage, getLoginDrivenData):
        self.loginPage.userNameE().send_keys(getLoginDrivenData[0])
        self.loginPage.emailE().send_keys(getLoginDrivenData[1])
        self.loginPage.passwordE().send_keys(getLoginDrivenData[2])
        self.loginPage.getLoginCodeBtnE().click()
        assert self.loginPage.errorMsgE().text == "401"
        self.refreshBrowser()

    @pytest.fixture(params=[("itay1709", "itay.zisman@payboxapp.co", "1234"), ("itay170", "itay.zisman@payboxapp.com", "1234")])
    def getLoginDrivenData(self, request):
        return request.param