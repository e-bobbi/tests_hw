from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def is_page_available(browser):
    try:
        browser.get("https://demoqa.com/modal-dialogs")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "showSmallModal")))
        return True
    except (TimeoutException, NoSuchElementException):
        return False

@pytest.mark.skipif(not is_page_available(browser()), reason="Page is not available")
def test_modal_dialogs(browser):
    browser.get("https://demoqa.com/modal-dialogs")

    small_modal_button = browser.find_element(By.ID, "showSmallModal")
    small_modal_button.click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm")))
    close_button = browser.find_element(By.ID, "closeSmallModal")
    close_button.click()

    large_modal_button = browser.find_element(By.ID, "showLargeModal")
    large_modal_button.click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    close_button = browser.find_element(By.ID, "closeLargeModal")
    close_button.click()

