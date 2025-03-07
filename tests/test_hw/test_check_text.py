from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text


class MainPage(BasePage):
    FOOTER_LOCATOR = (By.XPATH, "//footer//span")
    ELEMENTS_BUTTON = (By.XPATH, "//h5[text()='Elements']")

    def get_footer_text(self):
        return self.get_text(self.FOOTER_LOCATOR)

    def go_to_elements_page(self):
        self.click_element(self.ELEMENTS_BUTTON)


class ElementsPage(BasePage):
    CENTER_TEXT_LOCATOR = (By.CLASS_NAME, "mb-3")

    def get_center_text(self):
        return self.get_text(self.CENTER_TEXT_LOCATOR)


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_footer_text(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com/")

    footer_text = main_page.get_footer_text()
    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    assert footer_text == expected_text, f"Текст в подвале не совпадает. Ожидалось: {expected_text}, получено: {footer_text}"
    print("Тест пройден успешно! Текст в подвале совпадает.")


def test_elements_page(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com/")
    main_page.go_to_elements_page()

    elements_page = ElementsPage(driver)
    center_text = elements_page.get_center_text()
    expected_text = "Please select an item from left to start practice."

    assert center_text == expected_text, f"Текст по центру страницы не совпадает. Ожидалось: '{expected_text}', получено: '{center_text}'"
    print("Текст по центру страницы совпадает с ожидаемым.")

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()
