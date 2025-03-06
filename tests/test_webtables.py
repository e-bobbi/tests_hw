from pages.webtables_page import WebTablesPage

def test_add_button_opens_dialog(browser):
    page = WebTablesPage(browser)
page.open()
    page.click_add_button()
    assert page.is_registration_form_visible() 

def test_empty_form_cannot_be_submitted(browser):
    page = WebTablesPage(browser)
    page.open()
    page.click_add_button()
    assert page.is_form_empty()
    page.submit_form()
    assert page.is_registration_form_visible()

def test_add_record(browser):
    page = WebTablesPage(browser)
    page.open()
    page.click_add_button()
    page.fill_form("Иван", "Иванов", "ivan@example.com", "30", "50000", "Разработка")
    page.submit_form()
    assert not page.is_registration_form_visible()
    assert "Иван Иванов" in page.get_last_row_data()

def test_edit_record(browser):
    page = WebTablesPage(browser)
    page.open()
    page.click_add_button()
    page.fill_form("Иван", "Иванов", "ivan@example.com", "30", "50000", "Разработка")
    page.submit_form()

    page.click_edit_button(0)
    page.fill_form("Петр", "Иванов", "ivan@example.com", "30", "50000", "Разработка")
    page.submit_form()

    assert "Петр Иванов" in page.get_last_row_data()

def test_delete_record(browser):
    page = WebTablesPage(browser)
    page.open()
    page.click_add_button()
    page.fill_form("Иван", "Иванов", "ivan@example.com", "30", "50000", "Разработка")
    page.submit_form()

    initial_row_count = page.get_row_count()
    page.click_delete_button(0)
    assert page.get_row_count() == initial_row_count - 1
