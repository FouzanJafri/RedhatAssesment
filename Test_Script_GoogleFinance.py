import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_page_GoogleFinance import GoogleFinancePage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    
    driver.get("https://www.google.com/finance")
    request.cls.driver = driver
    request.cls.google_finance_page = GoogleFinancePage(driver)
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestGoogleFinance:

    def test_verify_stock_symbols(self):
        # Verify title
        assert "Google Finance" in self.driver.title
        ui_stock_symbols = self.google_finance_page.get_stock_symbols()

        # test data
        test_data = ["NFLX", "MSFT", "TSLA"]

        # Not in test data
        not_in_test_data = list(set(ui_stock_symbols) - set(test_data))
        print("Not in test data:", not_in_test_data)

        # In test data but not in UI
        not_in_ui = list(set(test_data) - set(ui_stock_symbols))
        print("In test data but not in UI:", not_in_ui)