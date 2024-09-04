from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from seleniumpagefactory.Pagefactory import PageFactory

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # self.page_factory = PageFactory.init_elements(driver, self)

    stock_symbols_locator = (By.XPATH, "//*[@class='sbnBtf']/li/a/div/div/div[1]/div/div/div")

    print(stock_symbols_locator)
    
    # Define actions
    def get_stock_symbols(self):
        return [element.text for element in self.wait.until(EC.presence_of_all_elements_located(self.stock_symbols_locator))]
