from pages.BasePage import BasePage
from playwright.sync_api import Page, expect

class CheckBoxPage(BasePage):


    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator('[id="result"]')


    def checkBoxItem(self, name):
        return self.page.locator('[for="tree-node-{}"]'.format(name))


    def expandCheckBox(self, name):
        return self.page.locator('xpath=//label[@for="tree-node-{}"]/preceding-sibling::button'.format(name))


    def goto(self, path='/checkbox'): 
        super().goto(path)


    def checkItem(self, name): 
        self.checkBoxItem(name).check()


    def expandItem(self, name): 
        self.expandCheckBox(name).click()

    def validateResult(self): 
        expect(self.result).to_contain_text('homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile')


