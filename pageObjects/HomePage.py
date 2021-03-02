from selenium.webdriver.common.by import By


class HomePage:

    #constructor:
    def __init__(self,driver):
        self.driver = driver

    #locators:
    searchInput = (By.ID, "search-input")
    searchBtn = (By.XPATH, "//div[.='Search']/button")
    upperNavigator = (By.XPATH, "//span[@class='text margin-sides']/a")
    entityNavigator = (By.XPATH, "//div[@class='col-md-6']/div[@class='btn-group']/label")
    userSubMenu = (By.XPATH, "//div[@class='row margin-around']/div[@class='col-md-6']/div[1]/div/label")
    groupSubMenu = (By.XPATH, "//div[@class='row margin-around']/div[@class='col-md-6']/div[2]/div/label")
    transactionSubMenu = (By.XPATH, "//div[@class='row margin-around']/div[@class='col-md-6']/div[3]/div/label")
    pofSubMenu = (By.XPATH, "//div[@class='row margin-around']/div[@class='col-md-6']/div[4]/div/label")
    cardSubMenu = (By.XPATH, "//div[@class='row margin-around']/div[@class='col-md-6']/div[5]/div/label")
    userTableData = (By.XPATH, "//table[@st-table='usersTableCopy']/tbody/tr/td")
    groupTableData = (By.XPATH, "//table[@st-table='groupsTableDisplay']/tbody/tr/td")

    #elements:
    def upperNavigatorE(self):
        return self.driver.find_elements(*HomePage.upperNavigator)

    def entityNavigatorE(self):
        return self.driver.find_elements(*HomePage.entityNavigator)

    def userSubMenuE(self):
        return self.driver.find_elements(*HomePage.userSubMenu)

    def groupSubMenuE(self):
        return self.driver.find_elements(*HomePage.groupSubMenu)

    def transactionSubMenuE(self):
        return self.driver.find_elements(*HomePage.transactionSubMenu)

    def pofSubMenuE(self):
        return self.driver.find_elements(*HomePage.pofSubMenu)

    def cardSubMenuE(self):
        return self.driver.find_elements(*HomePage.cardSubMenu)

    def searchInputE(self):
        return self.driver.find_element(*HomePage.searchInput)

    def searchBtnE(self):
        return self.driver.find_element(*HomePage.searchBtn)

    def userTableDataE(self):
        return self.driver.find_elements(*HomePage.userTableData)

    def groupTableDataE(self):
        return self.driver.find_elements(*HomePage.groupTableData)




