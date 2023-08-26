from playwright.sync_api import Page
from pages.CheckBoxPage import CheckBoxPage

class TestCheckBox:

    
    def test_base(self, page: Page):
        checkBoxPage = CheckBoxPage(page)
        checkBoxPage.goto()
        checkBoxPage.checkItem('home')
        checkBoxPage.expandItem('home')
        checkBoxPage.validateResult()
        
        