from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, **kwarg):
        self.page = page

    def goto(self, path):
        self.page.goto(path)