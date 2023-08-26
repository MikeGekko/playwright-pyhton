from playwright.sync_api import Page
from pages.TextBoxPage import TextBoxPage


class TestTextBox:

    
    def test_base(self, page: Page, textBoxData):
        textBoxPage = TextBoxPage(page)
        textBoxPage.goto()
        textBoxPage.fillTextBox(**textBoxData)
        textBoxPage.validateResultBox(**textBoxData)
        