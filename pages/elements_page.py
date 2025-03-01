from .base_page import BasePage

class ElementsPage(BasePage):
    CENTER_TEXT_LOCATOR = (By.CLASS_NAME, "mb-3")

    def get_center_text(self):
        return self.get_text(self.CENTER_TEXT_LOCATOR)
