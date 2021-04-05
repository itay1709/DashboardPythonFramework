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


driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\chromedriver.exe")
driver.get("https://pb-main-dev-bi.payboxapp.com/dashboard/#/login")
driver.maximize_window()

#login
driver.find_element_by_id("username").send_keys("itay1709")
driver.find_element_by_id("email").send_keys("itay.zisman@payboxapp.com")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_xpath("//div[@class='form-actions']/button[1]").click()
time.sleep(3)
driver.find_element_by_id("code").send_keys("123")
driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
time.sleep(3)
#login

#navigate to user page
upperNavigator = driver.find_elements_by_xpath("//span[@class='text margin-sides']/a")
entityNavigator = driver.find_elements_by_xpath("//div[@class='col-md-6']/div[@class='btn-group']/label")
entityNavigator[0].click()
userInput = driver.find_element_by_id("search-input")
userInput.send_keys("0502142080")
searchBtn = driver.find_element_by_xpath("//div[.='Search']/button")
searchBtn.click()
time.sleep(1)
userTableData = driver.find_elements_by_xpath("//table[@st-table='usersTableCopy']/tbody/tr/td")
userTableData[5].click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
time.sleep(3)
#navigate to user page

basicActionsBtnE = driver.find_element_by_xpath("//button[text()='More Actions']")
basicActionsBtnE.click()
time.sleep(1)
basicActionsList = driver.find_elements_by_xpath("//li[@ng-repeat='obj in moreActions']")
basicActionsList[0].click()
time.sleep(1)
actionWinOpenCombo = driver.find_element_by_xpath("//select[@ng-model='formData[action.form.f18.key]']")
actionWinOpenCombo.click()
actionWinCombo = driver.find_elements_by_xpath("//select[@ng-model='formData[action.form.f18.key]']/option")
actionWinCombo[2].click()
actionWinOkBtn = driver.find_element_by_xpath("//button[@class='btn btn-success']")
actionWinOkBtn.click()
userDetailsSecondRow = driver.find_elements_by_xpath("//div[@class='panel-body']/div[2]/div/p")
time.sleep(1)
print(userDetailsSecondRow[3].text)




