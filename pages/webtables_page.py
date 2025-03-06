from selenium.webdriver.common.by import By

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"

    def open(self):
        self.driver.get(self.url)

    def click_add_button(self):
        self.driver.find_element(By.ID, "addNewRecordButton").click()

    def is_registration_form_visible(self):
        return self.driver.find_element(By.ID, "registration-form-modal").is_displayed()

    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()

    def is_form_empty(self):
        first_name = self.driver.find_element(By.ID, "firstName").get_attribute("value")
        last_name = self.driver.find_element(By.ID, "lastName").get_attribute("value")
        return first_name == "" and last_name == ""

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.ID, "age").send_keys(age)
        self.driver.find_element(By.ID, "salary").send_keys(salary)
        self.driver.find_element(By.ID, "department").send_keys(department)

    def get_last_row_data(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        return rows[-1].text

    def click_edit_button(self, row_index):
        edit_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[title='Edit']")
        edit_buttons[row_index].click()

    def click_delete_button(self, row_index):
        delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[title='Delete']")
        delete_buttons[row_index].click()

    def get_row_count(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group"))
