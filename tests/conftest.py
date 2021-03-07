import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setupBrowser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\QA\Selenium\Drivers\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\P0022990\Desktop\Personal\QA\Selenium\Drivers\geckodriver.exe")
    driver.get("https://pb-main-dev-bi.payboxapp.com/dashboard/#/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

