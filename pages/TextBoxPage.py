from pages.BasePage import BasePage
from playwright.sync_api import Page, expect

class TextBoxPage(BasePage):
    result_text = None

    def __init__(self, page: Page):
        self.page = page
        self.current_address = page.locator('[id="permanentAddress"]')
        self.permanent_address = page.locator('[id="permanentAddress"]') 
        self.email = page.locator('[id="userEmail"]')
        self.full_name = page.locator('[id="userName"]')
        self.submit_button = page.locator('[id="submit"]')
        self.result_text = page.locator('[class*="border"]')

    
    def goto(self, path='/text-box'): 
        super().goto(path)


    def fillTextBox(self, name, email, curent_address, permanent_address): 
        self.full_name.fill(name)
        self.email.fill(email)
        self.current_address.fill(curent_address)
        self.permanent_address.fill(permanent_address)
        self.submit_button.click()

    def validateResultBox(self, name, email, curent_address, permanent_address):
        expect(self.result_text).to_contain_text(name)
        expect(self.result_text).to_contain_text(email)
        # expect(self.result_text).to_contain_text(curent_address)
        expect(self.result_text).to_contain_text(permanent_address)

