from .base_page import BasePage

class MainPage(BasePage):
    FOOTER_LOCATOR = (By.XPATH, "//footer//span")
    ELEMENTS_BUTTON = (By.XPATH, "//h5[text()='Elements']")

    def get_footer_text(self):
        return self.get_text(self.FOOTER_LOCATOR)

    def go_to_elements_page(self):
        self.click_element(self.ELEMENTS_BUTTON)
