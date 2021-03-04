import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

actualUpperNavigator = []
actualEntityNavigator = []
actualSubMenu = []

expectedEntityNavigator = ["User", "Group", "Transaction", "POF User", "Card", "P2P Gr", "Logs"]
expectedUpperNavigator = ["LOG", "ADMINS", "CONF EDITOR", "CS", "BI", "MASAV", "SCRIPTS", "SMP", "FRAUD", "EXTRACT DATA", "MARKETING", "DB EDITOR", "LOGOUT"]


driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\QA\Selenium\Drivers\chromedriver.exe")
driver.get("https://pb-main-dev-bi.payboxapp.com/dashboard/#/login")
driver.maximize_window()

driver.find_element_by_id("username").send_keys("itay1709")
driver.find_element_by_id("email").send_keys("itay.zisman@payboxapp.com")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_xpath("//div[@class='form-actions']/button[1]").click()
time.sleep(3)
driver.find_element_by_id("code").send_keys("123")
driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
time.sleep(3)
upperNavigator = driver.find_elements_by_xpath("//span[@class='text margin-sides']/a")
entityNavigator = driver.find_elements_by_xpath("//div[@class='col-md-6']/div[@class='btn-group']/label")
entityNavigator[0].click()
userInput = driver.find_element_by_id("search-input")
userInput.send_keys("0502142090")
searchBtn = driver.find_element_by_xpath("//div[.='Search']/button")
searchBtn.click()
time.sleep(1)
userTableData = driver.find_elements_by_xpath("//table[@st-table='usersTableCopy']/tbody/tr/td")
userTableData[5].click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
time.sleep(3)
basicActionsBtnE = driver.find_element_by_xpath("//button[text()='Basic Actions']")
basicActionsBtnE.click()
time.sleep(1)
basicActionsList = driver.find_elements_by_xpath("//li[@ng-repeat='obj in basicActions']")
basicActionsList[2].click()
time.sleep(1)
pinCodeInput = driver.find_element_by_xpath("//label[text()='pin']/following-sibling::input")
pinCodeInput.send_keys("1234")




'''
for i in upperNavigator:
    actualUpperNavigator.append(i.text)
assert actualUpperNavigator == expectedUpperNavigator

entityNavigator = driver.find_elements_by_xpath("//div[@class='col-md-6']/div[@class='btn-group']/label")

for i in entityNavigator:
    actualEntityNavigator.append(i.text)
assert actualEntityNavigator == expectedEntityNavigator

entityNavigator[1].click()
userInput = driver.find_element_by_id("search-input")
userInput.send_keys("603bb03b7b3fd0000a6c3168")
subMenu = driver.find_elements_by_xpath("//div[@class='row margin-around']/div[@class='col-md-6']/div[2]/div/label")
subMenu[4].click()
searchBtn = driver.find_element_by_xpath("//div[.='Search']/button")
searchBtn.click()
time.sleep(1)
userTableData = driver.find_elements_by_xpath("//table[@st-table='groupsTableDisplay']/tbody/tr/td")
#entityNavigator[5].click()

for i in userTableData:
    actualSubMenu.append(i.text)
print(actualSubMenu)

num = 10

for i in userTableData:
    actualUpperNavigator.append(i.text)
    num = num-1
    if num == 1:
        break
print(actualUpperNavigator)
print(actualUpperNavigator[0])
'''
