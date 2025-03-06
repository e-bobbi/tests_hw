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


def is_page_available(browser):
    try:
        browser.get("https://demoqa.com/alerts")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "timerAlertButton")))
        return True
    except TimeoutException:
        return False


@pytest.mark.skipif(not is_page_available(webdriver.Chrome()), reason="Page is not available")
def test_timer_alert(browser):
    browser.get("https://demoqa.com/alerts")

    timer_alert_button = browser.find_element(By.ID, "timerAlertButton")
    timer_alert_button.click()

    try:
        WebDriverWait(browser, 6).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Alert text: {alert_text}")
        alert.accept()
    except TimeoutException:
        pytest.fail("Alert did not appear within 5 seconds")
