import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setupBrowser")
class BaseClass:
    def logScriptDemo(self):
        fileHandler = logging.FileHandler("logFile.log")  # define the file log name
        fileFormat = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # define the log format
        fileHandler.setFormatter(fileFormat)  # connect the format to the file

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.addHandler(fileHandler)  # method that needs to except as argument the file log name

        logger.setLevel(logging.DEBUG)

        return logger

    def waitUntilXpath(self, text):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, text)))

    def selectByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def switchWindow(self, w):
        childWindow = self.driver.window_handles[w]
        self.driver.switch_to.window(childWindow)

    def refreshBrowser(self):
        self.driver.refresh()

