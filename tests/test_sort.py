from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def check_page_availability(func):
    def wrapper(browser):
        try:
            browser.get("https://demoqa.com/webtables")
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rt-table")))
            return func(browser)
        except TimeoutException:
            pytest.skip("Page is not available")

    return wrapper

@check_page_availability
def test_table_sorting(browser):
    headers = {
        "First Name": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(1)",
        "Last Name": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(2)",
        "Age": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(3)",
        "Email": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(4)",
        "Salary": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(5)",
        "Department": "div.rt-th.rt-resizable-header.-cursor-pointer:nth-child(6)"
    }

    for column_name, header_locator in headers.items():
        header = browser.find_element(By.CSS_SELECTOR, header_locator)

        header.click()

        assert "rt-th-rt-sort-asc" in header.get_attribute("class") or "rt-th-rt-sort-desc" in header.get_attribute(
            "class"), \
            f"Sorting failed for column: {column_name}"

        print(f"Sorting for column '{column_name}' is working.")
