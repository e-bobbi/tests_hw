from pages.main_page import MainPage
from pages.elements_page import ElementsPage

def test_footer_text(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com/")

    footer_text = main_page.get_footer_text()
    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    assert footer_text == expected_text, f"Текст в подвале не совпадает. Ожидалось: {expected_text}, получено: {footer_text}"
    print("Тест пройден успешно! Текст в подвале совпадает.")

def test_elements_page_center_text(driver):
    """Проверка текста по центру страницы Elements."""
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com/")
    main_page.go_to_elements_page()

    elements_page = ElementsPage(driver)
    center_text = elements_page.get_center_text()
    expected_text = "Please select an item from left to start practice."

    assert center_text == expected_text, f"Текст по центру страницы не совпадает. Ожидалось: '{expected_text}', получено: '{center_text}'"
    print("Текст по центру страницы совпадает с ожидаемым.")
